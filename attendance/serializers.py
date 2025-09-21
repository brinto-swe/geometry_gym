from rest_framework import serializers
from .models import Attendance

class AttendanceSerializer(serializers.ModelSerializer):
    member_detail = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Attendance
        fields = (
            'id', 'fitness_class', 'member', 'member_detail','status', 'marked_by', 'marked_at'
        )
        read_only_fields = ('id', 'marked_by', 'marked_at', 'member_detail')

    def get_member_detail(self, obj):
        return {
            'id': obj.member.id,
            'username': obj.member.username
        }
