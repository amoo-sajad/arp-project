from rest_framework import serializers
from .models import Service, Skill


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['title']


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ['title', 'caption', 'service']
