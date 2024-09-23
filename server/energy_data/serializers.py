from rest_framework import serializers
from .models import EnergyConsumption, SmartMeter
"""
Serializers for the energy data API.
"""


class SmartMeterSerializer(serializers.ModelSerializer):
  """
  Serializer for the SmartMeter model.
  """
  class Meta:
    model = SmartMeter
    fields = ['id', 'user', 'meter_id', 'last_reading', 'is_active', 'installation_date']


class EnergyConsumptionSerializer(serializers.ModelSerializer):
  """
  Serializer for the EnergyConsumption model.
  """
  meter = SmartMeterSerializer(read_only=True)

  class Meta:
    model = EnergyConsumption
    fields = ['id', 'user', 'timestamp', 'consumption', 'meter', 'cost']
