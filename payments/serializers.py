# payments/serializers.py
from rest_framework import serializers
from .models import Payment

class PaymentSerializer(serializers.ModelSerializer):
    user_detail = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Payment
        fields = ('id','user','user_detail','plan','amount','status','transaction_id','created_at')
        read_only_fields = ('id','created_at','user','user_detail')

    def get_user_detail(self, obj):
        return {'id': obj.user.id, 'username': obj.user.username}
