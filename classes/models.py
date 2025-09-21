# classes/models.py
from django.db import models
from django.conf import settings
from cloudinary.models import CloudinaryField

User = settings.AUTH_USER_MODEL

class FitnessClass(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True)
    instructor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='instructed_classes')
    capacity = models.PositiveIntegerField(default=20)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    image = CloudinaryField('image', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['start_time']

    def __str__(self):
        return f"{self.title} ({self.start_time:%Y-%m-%d %H:%M})"
