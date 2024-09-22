from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import EnergyConsumption, SmartMeter
from .serializers import EnergyConsumptionSerializer, SmartMeterSerializer
"""
Views for the energy data API.
"""


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
