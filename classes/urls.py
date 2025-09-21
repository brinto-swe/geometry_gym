from rest_framework.routers import DefaultRouter
from .views import FitnessClassViewSet
from django.urls import path, include

router = DefaultRouter()
router.register(r'', FitnessClassViewSet, basename='fitnessclass')

urlpatterns = [
    path('', include(router.urls)),
]
