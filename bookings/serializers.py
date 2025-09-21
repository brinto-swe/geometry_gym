# bookings/serializers.py
from rest_framework import serializers
from .models import Booking
from classes.serializers import FitnessClassSerializer

class BookingSerializer(serializers.ModelSerializer):
    user_detail = serializers.SerializerMethodField(read_only=True)
    class_detail = FitnessClassSerializer(source='fitness_class', read_only=True)

    class Meta:
        model = Booking
        fields = ('id','user','user_detail','fitness_class','class_detail','status','created_at')
        read_only_fields = ('id','created_at','user','user_detail','class_detail')

    def get_user_detail(self, obj):
        user = obj.user
        return {'id': user.id, 'username': user.username}
