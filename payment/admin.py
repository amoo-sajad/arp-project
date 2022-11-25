from django.contrib import admin
from .models import PaymentPlan, Payment


@admin.register(PaymentPlan)
class PaymentPlanAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'months']


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ['expert', 'get_price', 'ref_id', 'paid_at']

    @admin.display(ordering='payment_plan__price', description='price')
    def get_price(self, obj):
        return obj.payment_plan.price
