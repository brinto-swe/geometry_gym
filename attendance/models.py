# attendance/models.py
from django.db import models
from django.conf import settings
from classes.models import FitnessClass

class Attendance(models.Model):
    ATT_STATUS = (
        ('present','Present'),
        ('absent','Absent'),
        ('late','Late'),
    )
    fitness_class = models.ForeignKey(FitnessClass, on_delete=models.CASCADE, related_name='attendances')
    member = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='attendances')
    status = models.CharField(max_length=20, choices=ATT_STATUS)
    marked_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name='marked_attendances')
    marked_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('fitness_class','member')
        ordering = ['-marked_at']

    def __str__(self):
        return f"{self.member} - {self.fitness_class} : {self.status}"
