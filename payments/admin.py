# payments/admin.py
from django.contrib import admin
from .models import Payment

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('user','plan','amount','status','transaction_id','created_at')
    list_filter = ('status','plan')
