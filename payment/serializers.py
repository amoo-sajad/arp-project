from rest_framework import serializers
from .models import Payment, PaymentPlan


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ['expert', 'payment_plan', 'code', 'ref_id', 'authority']


class PaymentPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentPlan
        fields = ['id', 'title', 'months', 'price']
        read_only_fields = ['id']
