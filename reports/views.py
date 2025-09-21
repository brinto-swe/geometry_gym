# reports/views.py (full with imports)
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.db.models import Count, Avg, Sum, Q
from memberships.models import MembershipPlan
from attendance.models import Attendance
from feedback.models import Feedback
from payments.models import Payment

class MembershipReportView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        if not (getattr(user,'role',None) in ('admin',) or user.is_superuser):
            return Response({'detail':'Only admin can view reports.'}, status=403)
        plans = MembershipPlan.objects.annotate(subscriptions_count=Count('subscriptions')).values('id','name','price','duration_days','subscriptions_count')
        return Response({'plans': list(plans)})

class AttendanceReportView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        if not (getattr(user,'role',None) in ('admin',) or user.is_superuser):
            return Response({'detail':'Only admin can view reports.'}, status=403)
        by_class = Attendance.objects.values('fitness_class__id','fitness_class__title').annotate(present_count=Count('id', filter=Q(status='present')), total=Count('id'))
        return Response({'attendance_by_class': list(by_class)})

class FeedbackReportView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        if not (getattr(user,'role',None) in ('admin',) or user.is_superuser):
            return Response({'detail':'Only admin can view reports.'}, status=403)
        avg_rating = Feedback.objects.aggregate(avg_rating=Avg('rating'))
        top_classes = Feedback.objects.values('fitness_class__id','fitness_class__title').annotate(avg=Avg('rating'), count=Count('id')).order_by('-avg')[:10]
        return Response({'avg_rating': avg_rating,'top_classes': list(top_classes)})

class PaymentsReportView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        if not (getattr(user,'role',None) in ('admin',) or user.is_superuser):
            return Response({'detail':'Only admin can view reports.'}, status=403)
        payments_by_status = Payment.objects.values('status').annotate(total=Count('id'))
        total_revenue = Payment.objects.filter(status='success').aggregate(total=Sum('amount'))
        return Response({'payments_by_status': list(payments_by_status), 'total_revenue': total_revenue})
