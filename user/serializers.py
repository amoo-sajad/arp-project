from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = [
            'phone_number', 'first_name', 'last_name', 'email', 'user_province', 'user_city', 'password'
            ]

    def create(self, validated_data):
        user = User.objects.create_user(
            phone_number=validated_data['phone_number'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            user_province=validated_data['user_province'],
            user_city=validated_data['user_city'],
            password=validated_data['password'],
            )
        user.email = validated_data['email']
        user.save()
        
        return user
