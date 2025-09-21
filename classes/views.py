from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.response import Response
from .models import FitnessClass
from .serializers import FitnessClassSerializer

class FitnessClassViewSet(viewsets.ModelViewSet):
    queryset = FitnessClass.objects.all()
    serializer_class = FitnessClassSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        # Only staff/admin users should be allowed to create (we assume role-check later)
        user = self.request.user
        if not (user.is_authenticated and (getattr(user, 'role', None) in ('staff','admin') or user.is_superuser)):
            from rest_framework.exceptions import PermissionDenied
            raise PermissionDenied("Only staff or admin can create classes.")
        serializer.save()
    
    def perform_update(self, serializer):
        user = self.request.user
        if not (user.is_authenticated and (getattr(user, 'role', None) in ('staff','admin') or user.is_superuser)):
            from rest_framework.exceptions import PermissionDenied
            raise PermissionDenied("Only staff or admin can update classes.")
        serializer.save()

    def perform_destroy(self, instance):
        user = self.request.user
        if not (user.is_authenticated and (getattr(user, 'role', None) in ('staff','admin') or user.is_superuser)):
            from rest_framework.exceptions import PermissionDenied
            raise PermissionDenied("Only staff or admin can delete classes.")
        instance.delete()
