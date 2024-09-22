from django.db import models
from django.contrib.auth.models import User

class EnergyConsumption(models.Model):
  """
  A model representing the energy consumption data for a user.
  """
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  timestamp = models.DateTimeField()
  consumption = models.FloatField()

  class Meta:
    """
    Meta options for the EnergyConsumption model.
    """
    ordering = ['-timestamp']

class SmartMeter(models.Model):
  """
  A model representing a smart meter.
  """
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  meter_id = models.CharField(max_length=100, unique=True)
  last_reading = models.DateTimeField(null=True, blank=True)
