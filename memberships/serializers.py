from rest_framework import serializers
from .models import MembershipPlan, Subscription

class MembershipPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = MembershipPlan
        fields = '__all__'
        read_only_fields = ('id','created_at','updated_at')

class SubscriptionSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    plan_detail = MembershipPlanSerializer(source='plan', read_only=True)

    class Meta:
        model = Subscription
        fields = ('id','user','plan','plan_detail','start_date','end_date','active','created_at')
        read_only_fields = ('id','created_at','user','plan_detail')

    def create(self, validated_data):
        request = self.context.get('request')
        user = request.user
        validated_data['user'] = user
        return super().create(validated_data)
