# attendance/admin.py
from django.contrib import admin
from .models import Attendance

@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('member','fitness_class','status','marked_by','marked_at')
    list_filter = ('status','fitness_class')
