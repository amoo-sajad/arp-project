from django.urls import path
from .views import SignUpAPIView, UserRetrieveUpdateDestroyAPIView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('signup/', SignUpAPIView.as_view(), name='signup'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('<int:phone_number>/', UserRetrieveUpdateDestroyAPIView.as_view(), name='user')
]
