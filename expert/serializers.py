from rest_framework import serializers
from .models import Expert


class ExpertSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expert
        fields = [
            'user','father_name', 'expert_province', 'expert_city', 'shaba_number', 'gender', 
            'military_service', 'married_status', 'expert_lat', 'expert_long', 'skills'
            ]
        read_only_fields = ['user']
