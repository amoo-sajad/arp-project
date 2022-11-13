from django.contrib import admin
from .models import Expert, Skillship


@admin.register(Expert)
class ExpertAdmin(admin.ModelAdmin):
    list_display = ['user', 'father_name', 'gender', 'is_active']


@admin.register(Skillship)
class SkillshipAdmin(admin.ModelAdmin):
    list_display = ['expert', 'skill', 'image_of_evidence', 'description']
