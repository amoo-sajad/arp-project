from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _
from datetime import datetime, timedelta


class User(AbstractBaseUser, PermissionsMixin):
    phone_number = models.IntegerField(_('phone number'), unique=True)
    frist_name = models.CharField(_('first name'), max_length=100)
    last_name = models.CharField(_('last name'), max_length=100)
    email = models.EmailField(_('email'), blank=True, null=True)
    city = models.CharField(_('city'), max_length=100)
    birthday = models.DateField(_('birthday'), blank=True, null=True)
    otp_password = models.CharField(_('otp password'), max_length=6, blank=True, null=True)
    otp_time_created = models.DateTimeField(_('otp created time'), auto_now_add=True)
    otp_expire_time = models.DateTimeField(
        _('otp expire time'), default=datetime.now() + timedelta(minutes=2)
        )
    count_receive_services = models.PositiveIntegerField(_('count receive services'), default=0)
    is_active_customer = models.BooleanField(_('is active customer'), default=True)
    is_expert = models.BooleanField(_('is expert'), default=False)
    wallet_balance = models.IntegerField(_('wallet balance'), default=0)
    created_at = models.DateTimeField(_('created at'), auto_now_add=True)
    updated_at = models.DateTimeField(_('updated at'), auto_now=True)

    USERNAME_FIELD = 'phone_number'


    def __str__(self):
        return self.get_full_name()

    def get_full_name(self):
        return self.frist_name.strip() + ' ' + self.last_name.strip()

    def deposit(self, amount):
        self.wallet_balance = self.wallet_balance + amount
        return True

    def spent(self, amount):
        if amount > self.wallet_balance:
            return False
        else:
            self.wallet_balance = self.wallet_balance - amount
            return True

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
