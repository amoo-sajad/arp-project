from django.urls import path
from .views import (
    ServiceCreateAPIView, 
    SkillCreateAPIView, 
    ServiceListAPIView, 
    SkillListAPIView,
    ServiceDestroyAPIView,
    SkillDestroyAPIView
)

urlpatterns = [
    path('services/', ServiceListAPIView.as_view(), name='services'),
    path('skills/', SkillListAPIView.as_view(), name='skills'),
    path('new-service/', ServiceCreateAPIView.as_view(), name='new-service'),
    path('new-skill/', SkillCreateAPIView.as_view(), name='new-skill'),
    path('delete-service/<int:id>/', ServiceDestroyAPIView.as_view(), name='skills'),
    path('delete-skill/<int:id>/', SkillDestroyAPIView.as_view(), name='skills'),
]
