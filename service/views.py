from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAdminUser
from .models import Service, Skill
from .serializers import ServiceSerializer, SkillSerializer


class ServiceCreateAPIView(generics.CreateAPIView):
    serializer_class = ServiceSerializer
    permission_classes = [IsAdminUser]
    authentication_classes = [JWTAuthentication]
    queryset = Service.objects.all()


class SkillCreateAPIView(generics.CreateAPIView):
    serializer_class = SkillSerializer
    permission_classes = [IsAdminUser]
    authentication_classes = [JWTAuthentication]
    queryset = Skill.objects.all()
