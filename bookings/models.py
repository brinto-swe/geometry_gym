from django.db import models
from django.conf import settings
from classes.models import FitnessClass

User = settings.AUTH_USER_MODEL

class Booking(models.Model):
    STATUS_CHOICES = (
        ('booked','Booked'),
        ('cancelled','Cancelled'),
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='bookings')
    fitness_class = models.ForeignKey(FitnessClass, on_delete=models.CASCADE, related_name='bookings')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='booked')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user','fitness_class')  # prevent duplicate bookings
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.user} -> {self.fitness_class} ({self.status})"
