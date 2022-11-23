from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAdminUser, AllowAny
from .models import Service, Skill
from .serializers import ServiceSerializer, SkillSerializer
from django.shortcuts import get_object_or_404


class ServiceListAPIView(generics.ListAPIView):
    serializer_class = ServiceSerializer
    permission_classes = [AllowAny]
    authentication_classes = [JWTAuthentication]
    queryset = Service.objects.all()


class SkillListAPIView(generics.ListAPIView):
    serializer_class = SkillSerializer
    permission_classes = [AllowAny]
    authentication_classes = [JWTAuthentication]

    def get_queryset(self):
        service = self.request.GET.get('service', '')
        if service:
            return Skill.objects.filter(service=service)
        return Skill.objects.all()
