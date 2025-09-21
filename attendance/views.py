# attendance/views.py
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Attendance
from .serializers import AttendanceSerializer

class AttendanceViewSet(viewsets.ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        # staff/admin see all; members see their own attendance
        if user.is_authenticated and (getattr(user,'role',None) in ('staff','admin') or user.is_superuser):
            return Attendance.objects.all()
        return Attendance.objects.filter(member=user)

    def create(self, request, *args, **kwargs):
        # Expect payload: fitness_class, member, status
        user = request.user
        # only staff/admin allowed to mark attendance
        if not (user.is_authenticated and (getattr(user,'role',None) in ('staff','admin') or user.is_superuser)):
            return Response({'detail':'Only staff or admin can mark attendance.'}, status=status.HTTP_403_FORBIDDEN)

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(marked_by=user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
