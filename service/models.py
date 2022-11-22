from django.db import models
from django.utils.translation import gettext_lazy as _


class Service(models.Model):
    title = models.CharField(_('عنوان'), max_length=100, unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('سرویس')
        verbose_name_plural = _('سرویس ها')


class Skill(models.Model):
    title = models.CharField(_('عنوان'), max_length=100, unique=True)
    caption = models.TextField(_('توضیحات'), blank=True, null=True)
    service = models.ForeignKey(
        Service, verbose_name='سرویس', related_name='skills', on_delete=models.CASCADE
        )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('مهارت')
        verbose_name_plural = _('مهارت ها')
