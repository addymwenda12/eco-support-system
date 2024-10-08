from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import EnergyPrediction
from .serializers import EnergyPredictionSerializer
from .prediction_service import predict_energy_consumption
from datetime import datetime
"""
View for the EnergyPrediction model.
"""

class EnergyPredictionViewSet(viewsets.ModelViewSet):
  """
  Viewset for the EnergyPrediction model.
  """
  queryset = EnergyPrediction.objects.all()
  serializer_class = EnergyPredictionSerializer

  @action(detail=False, methods=['post'])
  def predict(self, request):
    """
    Predict the energy consumption for a given user and date.
    """
    meter_id = request.data.get('meter_id')
    prediction_date_str = request.data.get('prediction_date')
    
    if not meter_id or not prediction_date_str:
      return Response({'error': 'meter_id and prediction_date are required'}, status=status.HTTP_400_BAD_REQUEST)
    
    try:
      prediction_date = datetime.strptime(prediction_date_str, '%Y-%m-%d').date()
    except ValueError:
      return Response({'error': 'Invalid date format. Please use YYYY-MM-DD'}, status=status.HTTP_400_BAD_REQUEST)

    predicted_consumption = predict_energy_consumption(meter_id, prediction_date)
    if predicted_consumption is None:
      return Response({'error': 'Not enough data to make a prediction'}, status=status.HTTP_400_BAD_REQUEST)
    
    prediction = EnergyPrediction.objects.create(
      meter_id=meter_id,
      timestamp=prediction_date,
      predicted_consumption=predicted_consumption
    )

    serializer = self.get_serializer(prediction)
    return Response(serializer.data, status=status.HTTP_201_CREATED)

  @action(detail=False, methods=['get'])
  def user_predictions(self, request):
    """
    Get the predictions for a given user.
    """
    meter_id = request.query_params.get('meter_id')
    if not meter_id:
      return Response({'error': 'Meter ID is required'}, status=status.HTTP_400_BAD_REQUEST)

    predictions = EnergyPrediction.objects.filter(meter_id=meter_id).order_by('-timestamp')[:7]  # Last 7 predictions
    serializer = self.get_serializer(predictions, many=True)
    return Response(serializer.data)