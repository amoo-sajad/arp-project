from django.db import models
from django.contrib.auth import get_user_model
from datetime import datetime, timedelta
from django.utils.translation import gettext_lazy as _
from service.models import Skill

User = get_user_model()

class Expert(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_active_expert = models.BooleanField(_('is active expert'), default=False)
    expert_province = models.CharField(_('expert province'), max_length=100)
    expert_city = models.CharField(_('expert city'), max_length=100)
    ready_to_serve = models.BooleanField(_('ready to serve'), default=False)
    ready_to_serve_expire_time = models.DateTimeField(
        _('ready to serve expire time'), default=datetime.now() + timedelta(weeks=4)
        )
    father_name = models.CharField(_('father name'), max_length=26)
    shaba_numer = models.CharField(_('shaba number'), max_length=24)
    MALE = 1
    FEMALE = 2
    GENDER_CHOICE = [
        (MALE, 'MALE'),
        (FEMALE, 'FEMALE')
    ]
    gender = models.IntegerField(_('gender'), choices=GENDER_CHOICE)
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
    military_service = models.IntegerField(_('military service'), choices=MILITARY_SERVICE_CHOICES)
    SINGLE = 1
    MARRIED = 2
    MARRIED_CHOICES = [
        (SINGLE, 'SINGLE'),
        (MARRIED, 'MARRIED')
    ]
    married_status = models.IntegerField(_('married status'), choices=MARRIED_CHOICES)
    expert_lat = models.DecimalField(_('expert lat'), max_digits=9, decimal_places=6)
    expert_long = models.DecimalField(_('expert long'), max_digits=9, decimal_places=6)
    skills = models.ManyToManyField(Skill, related_name='experts', through='Skillship')
    total_profit = models.IntegerField(_('total profit'), default=0)
    expert_balance = models.IntegerField(_('expert balance'), default=0)
    count_complete_services = models.PositiveIntegerField(_('count complete services'), default=0)
    created_at = models.DateTimeField(_('created at'), auto_now_add=True)
    updated_at = models.DateTimeField(_('updated at'), auto_now=True)

    def __str__(self):
        return self.user.get_full_name()

    def count_skills(self):
        pass

    def skills_list(self):
        pass

    def withdraw(self, amount):
        if self.expert_balance < amount:
            return False
        else:
            self.expert_balance = self.expert_balance - amount
            return True

    class Meta:
        verbose_name = _('expert')
        verbose_name_plural = _('experts')


class Skillship(models.Model):
    expert = models.ForeignKey(Expert, on_delete=models.CASCADE)
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    years_of_experience = models.PositiveSmallIntegerField(
        _('years of experience'), blank=True, null=True
        )
    image_of_evidence = models.ImageField(
        _('image of eviddence'), upload_to='evidences', blank=True, null=True
        )
    description = models.TextField(_('description'))
