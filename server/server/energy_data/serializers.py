from rest_framework import serializers
from .models import EnergyConsumption, SmartMeter
"""
Serializers for the energy data API.
"""


class EnergyConsumptionSerializer(serializers.ModelSerializer):
  """
  Serializer for the EnergyConsumption model.
  """
  class Meta:
    model = EnergyConsumption
    fields = '__all__'

class SmartMeterSerializer(serializers.ModelSerializer):
  """
  Serializer for the SmartMeter model.
  """
  class Meta:
    model = SmartMeter
    fields = '__all__'

