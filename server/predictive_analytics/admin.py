from django.contrib import admin
from .models import EnergyPrediction
"""
Admin configuration for the EnergyPrediction model.
"""

@admin.register(EnergyPrediction)
class EnergyPredictionAdmin(admin.ModelAdmin):
    """
    Admin configuration for the EnergyPrediction model.
    """
    list_display = ('user', 'timestamp', 'predicted_consumption', 'actual_consumption')
    list_filter = ('user', 'timestamp')
    search_fields = ('user__username',)
