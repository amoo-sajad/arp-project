from rest_framework import serializers
from .models import Expert, Skillship


class ExpertSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expert
        fields = [
            'user','father_name', 'national_code', 'expert_province', 'expert_city', 'shaba_number',
            'gender', 'military_service', 'married_status', 'expert_lat', 'expert_long'
        ]
        read_only_fields = ['user']


class SkillshipSerializer(serializers.ModelSerializer):
    expert = serializers.CharField(read_only=True)
    
    class Meta:
        model = Skillship
        fields = ['expert', 'skill', 'image_of_evidence', 'description']
