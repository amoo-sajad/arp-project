from django.contrib import admin
from .models import Expert


@admin.register(Expert)
class ExpertAdmin(admin.ModelAdmin):
    list_display = ['user', 'father_name', 'gender', 'is_active']
