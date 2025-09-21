from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, SAFE_METHODS
from .models import MembershipPlan, Subscription
from .serializers import MembershipPlanSerializer, SubscriptionSerializer

class MembershipPlanViewSet(viewsets.ModelViewSet):
    queryset = MembershipPlan.objects.all().order_by('price')
    serializer_class = MembershipPlanSerializer

    def get_permissions(self):
        # safe methods allowed for anyone; modify requires staff/admin
        if self.request.method in SAFE_METHODS:
            from rest_framework.permissions import AllowAny
            return [AllowAny()]
        # restrict to staff/admin (or superuser)
        from rest_framework.permissions import IsAuthenticated
        return [IsAuthenticated()]

    def perform_create(self, serializer):
        # further check role if required (only staff/admin allowed)
        user = self.request.user
        if not (user.is_authenticated and (getattr(user,'role',None) in ('staff','admin') or user.is_superuser)):
            from rest_framework.exceptions import PermissionDenied
            raise PermissionDenied("Only staff/admin can create membership plans.")
        serializer.save()

class SubscriptionViewSet(viewsets.ModelViewSet):
    queryset = Subscription.objects.all().select_related('plan','user')
    serializer_class = SubscriptionSerializer

    def get_permissions(self):
        # must be authenticated for all subscription actions
        from rest_framework.permissions import IsAuthenticated
        return [IsAuthenticated()]

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated and (getattr(user,'role',None) in ('staff','admin') or user.is_superuser):
            return Subscription.objects.all()
        return Subscription.objects.filter(user=user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
