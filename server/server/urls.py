"""
URL configuration for server project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from energy_data.views import EnergyConsumptionViewSet, SmartMeterViewSet
from predictive_analytics.views import EnergyPredictionViewSet
from customer_support.views import ChatSessionViewSet
from notifications.views import NotificationViewSet
"""
URLs for the energy data API.
"""

router = DefaultRouter()
router.register(r'energy_consumption', EnergyConsumptionViewSet)
router.register(r'smart_meter', SmartMeterViewSet)
router.register(r'energy_prediction', EnergyPredictionViewSet)
router.register(r'chat_sessions', ChatSessionViewSet)
router.register(r'notifications', NotificationViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
