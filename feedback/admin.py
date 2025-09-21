# feedback/admin.py
from django.contrib import admin
from .models import Feedback

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('user','fitness_class','rating','created_at')
    list_filter = ('rating','fitness_class')
