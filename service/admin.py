from django.contrib import admin
from .models import Service, Skill


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    display_fields = ['title']


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    display_fields = ['title', 'caption', 'service']
