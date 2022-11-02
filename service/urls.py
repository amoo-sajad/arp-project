from django.urls import path
from .views import ServiceCreateAPIView, SkillCreateAPIView

urlpatterns = [
    path('new-service/', ServiceCreateAPIView.as_view(), name='new-service'),
    path('new-skill/', SkillCreateAPIView.as_view(), name='new-skill'),
]