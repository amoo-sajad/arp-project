from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.management.commands.createsuperuser import Command
from django.contrib.auth import get_user_model

User = get_user_model()


class Command(Command):
    def handle(self, *args, **options):
        phone_number = input('phone_number: ')
        first_name = input('first_name: ')
        last_name = input('last_name: ')
        user_province = input('user_province: ')
        user_city = input('user_city: ')
        password = input('password: ')
        try:
            User.objects.create_superuser(
                phone_number, first_name, last_name, user_province, user_city, password
            )
        except ValueError:
            raise CommandError('insert phone_number and password correctly')
