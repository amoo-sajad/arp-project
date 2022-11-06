from rest_framework import generics
from .serializers import ExpertSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Expert
from django.contrib.auth import get_user_model

User = get_user_model()


class ExpertSignUpAPIView(generics.CreateAPIView):
    serializer_class = ExpertSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    queryset = Expert.objects.all()

    def perform_create(self, serializer):
        user = User.objects.get(phone_number=self.request.user.phone_number)
        user.is_expert = True
        user.save()
        serializer.save(user=self.request.user)
