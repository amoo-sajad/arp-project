from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
from datetime import datetime
from django.utils.translation import gettext_lazy as _
from service.models import Skill

User = get_user_model()


class Expert(models.Model):
    user = models.OneToOneField(User, verbose_name='کاربر', on_delete=models.CASCADE)
    national_code = models.CharField(_('کد ملی'), max_length=10)
    father_name = models.CharField(_('نام پدر'), max_length=26)
    expert_province = models.CharField(_('استان'), max_length=100)
    expert_city = models.CharField(_('شهر'), max_length=100)
    MALE = 1
    FEMALE = 2
    GENDER_CHOICE = [
        (MALE, 'MALE'),
        (FEMALE, 'FEMALE')
    ]
    gender = models.PositiveSmallIntegerField(_('جنسیت'), choices=GENDER_CHOICE)
    WOMEN = 1
    DONE = 2
    EXEMPT = 3
    SUBJECT = 4
    MILITARY_SERVICE_CHOICES = [
        (WOMEN, 'WOMEN'),
        (DONE, 'DONE'),
        (EXEMPT, 'EXEMPT'),
        (SUBJECT, 'SUBJECT')
    ]
    military_service = models.PositiveSmallIntegerField(
        _('سربازی'), choices=MILITARY_SERVICE_CHOICES
        )
    SINGLE = 1
    MARRIED = 2
    MARRIED_CHOICES = [
        (SINGLE, 'SINGLE'),
        (MARRIED, 'MARRIED')
    ]
    married_status = models.PositiveSmallIntegerField(_('وضعیت تاهل'), choices=MARRIED_CHOICES)
    is_active_expert_expire_time = models.DateTimeField(_('تاریخ غیرفعال شدن اکانت'), default=timezone.now)
    expert_lat = models.DecimalField(_('expert lat'), max_digits=9, decimal_places=6)
    expert_long = models.DecimalField(_('expert long'), max_digits=9, decimal_places=6)
    skills = models.ManyToManyField(
        Skill, verbose_name='مهارت ها', related_name='experts', through='Skillship'
        )
    created_at = models.DateTimeField(_('created_at'), auto_now_add=True)
    updated_at = models.DateTimeField(_('updated_at'), auto_now=True)

    def __str__(self):
        return self.user.get_full_name()

    def count_skills(self):
        pass

    def skills_list(self):
        pass

    @property
    def is_active(self):
        now = timezone.now()
        return self.is_active_expert_expire_time > now

    class Meta:
        verbose_name = _('متخصص')
        verbose_name_plural = _('متخصصان')


class Skillship(models.Model):
    expert = models.ForeignKey(Expert, verbose_name='متخصص', on_delete=models.CASCADE)
    skill = models.ForeignKey(Skill, verbose_name='مهارت', on_delete=models.CASCADE)
    image_of_evidence = models.ImageField(_('تصویر مدرک'), upload_to='evidences')
    description = models.TextField(_('توضیحات'))

    class Meta:
        verbose_name = _('تخصص')
        verbose_name_plural = _('تخصص ها')

