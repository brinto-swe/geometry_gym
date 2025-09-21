# payments/models.py
from django.db import models
from django.conf import settings
from memberships.models import MembershipPlan

class Payment(models.Model):
    STATUS_CHOICES = (
        ('pending','Pending'),
        ('success','Success'),
        ('failed','Failed'),
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='payments')
    plan = models.ForeignKey(MembershipPlan, on_delete=models.SET_NULL, null=True, related_name='payments')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    transaction_id = models.CharField(max_length=200, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.user} - {self.amount} ({self.status})"
