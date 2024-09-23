from rest_framework import serializers
from .models import EnergyPrediction
"""
Serializer for the EnergyPrediction model.
"""

class EnergyPredictionSerializer(serializers.ModelSerializer):
  """
  Serializer for the EnergyPrediction model.
  """
  class Meta:
    model = EnergyPrediction
    fields = '__all__'
