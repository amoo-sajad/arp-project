from django.urls import path
from .views import ExpertSignUpAPIView, AddSkillAPIView

urlpatterns = [
    path('signup/', ExpertSignUpAPIView.as_view(), name='expert-signup'),
    path('skill/add/', AddSkillAPIView.as_view(), name='skill-add'),
]
