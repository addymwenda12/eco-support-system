from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from energy_data.views import EnergyConsumptionViewSet, SmartMeterViewSet
"""
URLs for the energy data API.
"""

router = DefaultRouter()
router.register(r'energy_consumption', EnergyConsumptionViewSet)
router.register(r'smart_meter', SmartMeterViewSet)

urlpatterns = [
  path('admin/', admin.site.urls),
  path('api/', include(router.urls)),
]

