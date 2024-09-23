from django.contrib import admin
from .models import EnergyConsumption, SmartMeter
"""
Admin classes for the energy data models.
"""

@admin.register(EnergyConsumption)
class EnergyConsumptionAdmin(admin.ModelAdmin):
    """
    Admin class for the EnergyConsumption model.
    """
    list_display = ('user', 'timestamp', 'consumption', 'meter', 'cost')
    list_filter = ('user', 'meter', 'timestamp')
    search_fields = ('user__username', 'meter__meter_id')

@admin.register(SmartMeter)
class SmartMeterAdmin(admin.ModelAdmin):
    """
    Admin class for the SmartMeter model.
    """
    list_display = ('meter_id', 'user', 'last_reading', 'is_active', 'installation_date')
    list_filter = ('is_active', 'installation_date')
    search_fields = ('meter_id', 'user__username')

