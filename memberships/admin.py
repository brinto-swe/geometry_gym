from django.contrib import admin
from .models import MembershipPlan, Subscription

@admin.register(MembershipPlan)
class MembershipPlanAdmin(admin.ModelAdmin):
    list_display = ('name','price','duration_days','created_at')

@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('user','plan','start_date','end_date','active')
    list_filter = ('active','plan')
