from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import EnergyConsumption, SmartMeter
from .serializers import EnergyConsumptionSerializer, SmartMeterSerializer
from rest_framework.decorators import action
from django.db.models import Sum, Avg

"""
Views for the energy data API.
"""

class SmartMeterViewSet(viewsets.ModelViewSet):
  """
  A viewset for the SmartMeter model.
  """
  queryset = SmartMeter.objects.all()
  serializer_class = SmartMeterSerializer

  def create(self, request, *args, **kwargs):
    """
    Create a new smart meter record.
    """
    serializer = self.get_serializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    self.perform_create(serializer)
    return Response(serializer.data, status=status.HTTP_201_CREATED)
    # headers = self.get_success_headers(serializer.data)

  @action(detail=True, methods=['post'])
  def deactivate(self, request, pk=None):
    """
    Deactivate a smart meter.
    """
    meter = self.get_object()
    meter.is_active = False
    meter.save()
    return Response({'status': 'meter deactivated'})


class EnergyConsumptionViewSet(viewsets.ModelViewSet):
  """
  A viewset for the EnergyConsumption model.
  """
  queryset = EnergyConsumption.objects.all()
  serializer_class = EnergyConsumptionSerializer

  def create(self, request, *args, **kwargs):
    """
    Create a new energy consumption record.
    """
    serializer = self.get_serializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    self.perform_create(serializer)
    return Response(serializer.data, status=status.HTTP_201_CREATED)
    # headers = self.get_success_headers(serializer.data)

  @action(detail=False, methods=['get'])
  def user_summary(self, request):
    """
    Get the total and average consumption for a user.
    """
    user_id = request.query_params.get('user_id')
    if not user_id:
      return Response({'error': 'User ID is required'}, status=status.HTTP_400_BAD_REQUEST)

    consumption_data = EnergyConsumption.objects.filter(user_id=user_id)
    total_consumption = consumption_data.aggregate(Sum('consumption'))['consumption__sum']
    avg_consumption = consumption_data.aggregate(Avg('consumption'))['consumption__avg']

    return Response({
      'total_consumption': total_consumption,
      'average_consumption': avg_consumption,
    })

  @action(detail=False, methods=['get'])
  def meter_summary(self, request):
    """
    Get the total and average consumption for a meter.
    """
    meter_id = request.query_params.get('meter_id')
    if not meter_id:
      return Response({'error': 'Meter ID is required'}, status=status.HTTP_400_BAD_REQUEST)

    consumption_data = EnergyConsumption.objects.filter(meter_id=meter_id)
    total_consumption = consumption_data.aggregate(Sum('consumption'))['consumption__sum']
    avg_consumption = consumption_data.aggregate(Avg('consumption'))['consumption__avg']

    return Response({
      'total_consumption': total_consumption,
      'average_consumption': avg_consumption,
    })
