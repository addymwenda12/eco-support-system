from django.db import models
from django.contrib.auth.models import User

class EnergyConsumption(models.Model):
  """
  A model representing the energy consumption data for a user.
  """
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  timestamp = models.DateTimeField()
  consumption = models.FloatField()
  meter = models.ForeignKey('SmartMeter', on_delete=models.CASCADE)
  cost = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

  class Meta:
    """
    Meta options for the EnergyConsumption model.
    """
    ordering = ['-timestamp']

  def __str__(self):
    """
    Return a string representation of the EnergyConsumption model.
    """
    return f"{self.user.username} - {self.timestamp} - {self.consumption} kWh"

class SmartMeter(models.Model):
  """
  A model representing a smart meter.
  """
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  meter_id = models.CharField(max_length=100, unique=True)
  last_reading = models.DateTimeField(null=True, blank=True)
  is_active = models.BooleanField(default=True)
  installation_date = models.DateField()

  def __str__(self):
    """
    Return a string representation of the SmartMeter model.
    """
    return f"Meter {self.meter_id} - {self.user.username}"
