from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, phone_number, first_name, last_name, user_province, user_city, password):
        if not phone_number:
            raise ValueError('enter phone number!')
        user = self.model(
            phone_number=phone_number,
            first_name=first_name,
            last_name=last_name,
            user_province=user_province,
            user_city=user_city
            )
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, phone_number, first_name, last_name, user_province, user_city, password):
        user = self.create_user(phone_number, first_name, last_name, user_province, user_city, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user
