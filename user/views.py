from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import AllowAny
from .serializers import UserSignUpSerializer, UserSerializer
from .permissions import IsOwnerOrAdmin
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()


class SignUpAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [AllowAny]
    serializer_class = UserSignUpSerializer

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = self.perform_create(serializer)
        refresh = RefreshToken.for_user(user)
        return Response({
            'phone_number': user.phone_number, 
            'access': str(refresh.access_token), 
            'refresh': str(refresh)})


class UserRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    permission_classes = [IsOwnerOrAdmin]
    authentication_classes = [JWTAuthentication]
    serializer_class = UserSerializer
    lookup_field = 'phone_number'
    lookup_url_kwarg = 'phone_number'
