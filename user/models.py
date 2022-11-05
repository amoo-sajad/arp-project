from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _
from datetime import datetime, timedelta
from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    phone_number = models.CharField(_('phone number'), unique=True, max_length=11)
    first_name = models.CharField(_('first name'), max_length=100)
    last_name = models.CharField(_('last name'), max_length=100)
    email = models.EmailField(_('email'), blank=True, null=True)
    user_province = models.CharField(_('province'), max_length=100)
    user_city = models.CharField(_('city'), max_length=100)
    birthday = models.DateField(_('birthday'), blank=True, null=True)
    count_receive_services = models.PositiveIntegerField(_('count receive services'), default=0)
    is_active_customer = models.BooleanField(_('is active customer'), default=True)
    is_expert = models.BooleanField(_('is expert'), default=False)
    is_staff = models.BooleanField(_('is staff'), default=False)
    wallet_balance = models.IntegerField(_('wallet balance'), default=0)
    user_lat = models.DecimalField(_('user lat'), max_digits=9, decimal_places=6, null=True, blank=True)
    user_long = models.DecimalField(_('user long'), max_digits=9, decimal_places=6, null=True, blank=True)
    created_at = models.DateTimeField(_('created at'), auto_now_add=True)
    updated_at = models.DateTimeField(_('updated at'), auto_now=True)

    USERNAME_FIELD = 'phone_number'
    EMAIL_FIELD = 'email'
    objects = UserManager()


    def __str__(self):
        return self.get_full_name()

    def get_full_name(self):
        return self.first_name.strip() + ' ' + self.last_name.strip()

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
