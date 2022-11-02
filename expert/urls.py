from django.urls import path
from .views import ExpertSignUpAPIView

urlpatterns = [
    path('signup/', ExpertSignUpAPIView.as_view(), name='expert-signup'),
]
