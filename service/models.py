from django.db import models
from django.utils.translation import gettext_lazy as _


class Service(models.Model):
    title = models.CharField(_('title'), max_length=100)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('service')
        verbose_name_plural = _('services')


class Skill(models.Model):
    title = models.CharField(_('title'), max_length=100)
    caption = models.TextField(_('caption'), blank=True, null=True)
    service = models.ForeignKey(Service, related_name='skills', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('skill')
        verbose_name_plural = _('skills')
