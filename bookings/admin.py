# bookings/admin.py
from django.contrib import admin
from .models import Booking

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('user','fitness_class','status','created_at')
    list_filter = ('status','fitness_class')
