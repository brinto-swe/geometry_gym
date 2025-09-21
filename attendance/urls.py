# attendance/urls.py
from rest_framework.routers import DefaultRouter
from .views import AttendanceViewSet
from django.urls import path, include

router = DefaultRouter()
router.register(r'', AttendanceViewSet, basename='attendance')

urlpatterns = [
    path('', include(router.urls)),
]
