from django.contrib import admin
from .models import Service, Skill


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['title', 'caption', 'service']
