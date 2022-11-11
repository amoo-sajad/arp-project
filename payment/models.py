from django.db import models
from django.utils.translation import gettext_lazy as _
from expert.models import Expert
from datetime import timedelta
from django.utils import timezone


class PaymentPlan(models.Model):
    title = models.CharField(_('title'), max_length=100, unique=True)
    months = models.PositiveSmallIntegerField(_('months'))
    price = models.IntegerField(_('price'))

    def __str__(self):
        return self.title


class Payment(models.Model):
    expert = models.ForeignKey(Expert, on_delete=models.CASCADE, related_name='payments')
    authority = models.CharField(_('authority'), max_length=200, unique=True)
    payment_plan = models.ForeignKey(PaymentPlan, on_delete=models.CASCADE, related_name='payments')
    code = models.IntegerField(_('code'), null=True, blank=True)
    ref_id = models.IntegerField(_('ref id'), null=True, blank=True)
    card_span = models.CharField(_('card span'), max_length=100, null=True, blank=True)
    card_hash = models.CharField(_('card hash'), max_length=200, null=True, blank=True)
    fee_type = models.CharField(_('fee type'), max_length=100, null=True, blank=True)
    fee = models.IntegerField(_('fee'), null=True, blank=True)
    charged = models.BooleanField(_('charged'), default=False)
    paid_at = models.DateTimeField(_('paid at'), auto_now_add=True)

    def __str__(self):
        return str(self.expert)

    def get_amount(self):
        return self.payment_plan.price

    def charge_expert(self):
        expert = self.expert
        if expert.is_active:
            expert.is_active_expert_expire_time += timedelta(days=self.payment_plan.months*30)
        else:
            expert.is_active_expert_expire_time = timezone.now() + timedelta(
                days=self.payment_plan.months*30)
        self.charged = True
        self.save()
        expert.save()
