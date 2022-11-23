from django.urls import path
from .views import (
    ServiceListAPIView, 
    SkillListAPIView,
)

urlpatterns = [
    path('services/', ServiceListAPIView.as_view(), name='services'),
    path('skills/', SkillListAPIView.as_view(), name='skills')
]
