# reports/urls.py
from django.urls import path
from .views import MembershipReportView, AttendanceReportView, FeedbackReportView, PaymentsReportView

urlpatterns = [
    path('memberships/', MembershipReportView.as_view(), name='report-memberships'),
    path('attendance/', AttendanceReportView.as_view(), name='report-attendance'),
    path('feedback/', FeedbackReportView.as_view(), name='report-feedback'),
    path('payments/', PaymentsReportView.as_view(), name='report-payments'),
]
