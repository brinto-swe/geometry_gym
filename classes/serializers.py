from rest_framework import serializers
from .models import FitnessClass
from django.conf import settings
from django.contrib.auth import get_user_model

User = get_user_model()

class FitnessClassSerializer(serializers.ModelSerializer):
    instructor_detail = serializers.SerializerMethodField(read_only=True)
    image = serializers.ImageField(required=False)

    class Meta:
        model = FitnessClass
        fields = ('id','title','description','instructor','instructor_detail','capacity','start_time','end_time','image','created_at')
        read_only_fields = ('id','created_at','instructor_detail')

    def get_instructor_detail(self, obj):
        if obj.instructor:
            return {'id': obj.instructor.id, 'username': obj.instructor.username, 'role': getattr(obj.instructor, 'role', None)}
        return None
