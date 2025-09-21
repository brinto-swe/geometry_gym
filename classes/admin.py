from django.contrib import admin
from .models import FitnessClass

@admin.register(FitnessClass)
class FitnessClassAdmin(admin.ModelAdmin):
    list_display = ('title','instructor','start_time','end_time','capacity')
    list_filter = ('instructor','start_time')
