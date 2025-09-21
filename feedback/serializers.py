# feedback/serializers.py
from rest_framework import serializers
from .models import Feedback

class FeedbackSerializer(serializers.ModelSerializer):
    user_detail = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Feedback
        fields = ('id','user','user_detail','fitness_class','rating','comment','created_at')
        read_only_fields = ('id','created_at','user','user_detail')

    def get_user_detail(self, obj):
        return {'id': obj.user.id, 'username': obj.user.username}
