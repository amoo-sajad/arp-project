from django.db import models
from django.contrib.auth import get_user_model
from service.models import Skill
from expert.models import Expert
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class Order(models.Model):
    user = models.ForeignKey(User, related_name='order', on_delete=models.CASCADE)
    skill = models.ForeignKey(Skill, related_name='order', on_delete=models.CASCADE)
    caption = models.TextField(_('caption'), blank=True, null=True)
    price = models.IntegerField(_('price'), blank=True, null=True)

    def __str__(self):
        return self.user.get_full_name()

    class Meta:
        verbose_name = _('order')
        verbose_name_plural = _('orders')
