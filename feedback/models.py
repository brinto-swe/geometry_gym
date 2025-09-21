# feedback/models.py
from django.db import models
from django.conf import settings
from classes.models import FitnessClass

class Feedback(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='feedbacks')
    fitness_class = models.ForeignKey(FitnessClass, on_delete=models.CASCADE, related_name='feedbacks')
    rating = models.PositiveSmallIntegerField()  # 1-5
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.user} -> {self.fitness_class} ({self.rating})"
