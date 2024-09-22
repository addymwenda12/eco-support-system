from django.db import models
from django.contrib.auth.models import User
"""
Module to store energy consumption predictions.
"""

class EnergyPrediction(models.Model):
  """
  A model to store energy consumption predictions.
  """
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  timestamp = models.DateTimeField(auto_now_add=True)
  predicted_consumption = models.FloatField()
  actual_consumption = models.FloatField(null=True, blank=True)
  # meter = models.ForeignKey('energy_data.SmartMeter', on_delete=models.CASCADE)

  def __str__(self):
    """
    Return a string representation of the EnergyPrediction model.
    """
    return f"{self.user.username} - {self.timestamp} - Predicted: {self.predicted_consumption}, Actual: {self.actual_consumption} kWh"

