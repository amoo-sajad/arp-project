from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAdminUser, AllowAny
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
        return Skill.objects.filter(service=service)


class ServiceDestroyAPIView(generics.DestroyAPIView):
    serializer_class = ServiceSerializer
    permission_classes = [IsAdminUser]
    authentication_classes = [JWTAuthentication]
    queryset = Service.objects.all()

    def get_object(self):
        service = self.request.GET.get('service', '')
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset, title=service)
        self.check_object_permissions(self.request, obj)
        return obj


class SkillDestroyAPIView(generics.DestroyAPIView):
    serializer_class = SkillSerializer
    permission_classes = [IsAdminUser]
    authentication_classes = [JWTAuthentication]
    queryset = Skill.objects.all()

    def get_object(self):
        skill = self.request.GET.get('skill', '')
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset, title=skill)
        self.check_object_permissions(self.request, obj)
        return obj
