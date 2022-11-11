from django.contrib import admin
from .models import PaymentPlan, Payment


@admin.register(PaymentPlan)
class PaymentPlanAdmin(admin.ModelAdmin):
    display_fields = ['title', 'price']


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    display_fields = ['expert', 'amount', 'ref_id', 'paid_at']
