from rest_framework import generics
from .serializers import ExpertSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Expert


class ExpertSignUpAPIView(generics.CreateAPIView):
    serializer_class = ExpertSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    queryset = Expert.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
