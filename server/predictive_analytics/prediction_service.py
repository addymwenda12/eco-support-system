from sklearn.linear_model import LinearRegression
from energy_data.models import EnergyConsumption
from datetime import timedelta
import numpy as np
"""
Module to handle the prediction of energy consumption.
"""


def predict_energy_consumption(meter_id, prediction_date):
  """
  Predict the energy consumption for a given user and date.
  """
  # Get the last 30 days of energy consumption data
  end_date = prediction_date - timedelta(days=1)
  start_date = end_date - timedelta(days=30)

  consumption_data = EnergyConsumption.objects.filter(
    meter__meter_id=meter_id,
    timestamp__range=(start_date, end_date)
  ).order_by('timestamp')

  if consumption_data.count() < 7:
    return None

  # Convert the consumption data to a numpy array
  x = np.array(range(consumption_data.count())).reshape(-1, 1)
  y = np.array([data.consumption for data in consumption_data])

  # Create a linear regression model and train it
  model = LinearRegression()
  model.fit(x, y)

  # Predict the consumption for the next day
  next_day = np.array([[consumption_data.count()]])
  predicted_consumption = model.predict(next_day)[0]

  return max(0, predicted_consumption) # Ensure the prediction is not negative
