# bookings/views.py
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Booking
from .serializers import BookingSerializer
from classes.models import FitnessClass

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        # staff/admin can view all bookings
        if user.is_authenticated and (getattr(user,'role',None) in ('staff','admin') or user.is_superuser):
            return Booking.objects.all()
        return Booking.objects.filter(user=user)

    def create(self, request, *args, **kwargs):
        user = request.user
        fitness_class_id = request.data.get('fitness_class')
        if not fitness_class_id:
            return Response({'detail':'fitness_class field is required.'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            fitness_class = FitnessClass.objects.get(pk=fitness_class_id)
        except FitnessClass.DoesNotExist:
            return Response({'detail':'Fitness class not found.'}, status=status.HTTP_404_NOT_FOUND)

        # check if user already booked
        if Booking.objects.filter(user=user, fitness_class=fitness_class, status='booked').exists():
            return Response({'detail':'You already have a booking for this class.'}, status=status.HTTP_400_BAD_REQUEST)

        # capacity check
        current_booked = Booking.objects.filter(fitness_class=fitness_class, status='booked').count()
        if current_booked >= fitness_class.capacity:
            return Response({'detail':'Class is fully booked.'}, status=status.HTTP_400_BAD_REQUEST)

        booking = Booking.objects.create(user=user, fitness_class=fitness_class)
        serializer = self.get_serializer(booking)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def perform_destroy(self, instance):
        # allow user to cancel their booking (mark cancelled)
        user = self.request.user
        if instance.user != user and not (getattr(user,'role',None) in ('staff','admin') or user.is_superuser):
            from rest_framework.exceptions import PermissionDenied
            raise PermissionDenied("You cannot cancel this booking.")
        instance.status = 'cancelled'
        instance.save()
