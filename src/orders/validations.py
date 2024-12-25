import re
from rest_framework import serializers
from users.models import User, EmailVerify, PasswordReset

# Валидация регистрации
def custom_validate_order(data):
    return 
    # email = data.get('email')
    # if not email:
    #     raise serializers.ValidationError({'email': 'Пожалуйста, заполните поле почты.'})
    # if User.objects.filter(email=email).exists():
    #     raise serializers.ValidationError({'email': 'Эта почта уже используется.'})
    # custom_validate_email(email)

    # password = data.get('password')
    # if not password:
    #     raise serializers.ValidationError({'password': 'Пожалуйста, заполните поле пароля.'})
    # custom_validate_password(password)

    # last_name = data.get('last_name')
    # if not last_name:
    #     raise serializers.ValidationError({'last_name': 'Пожалуйста, заполните поле фамилии.'})
    # custom_validate_last_name(last_name)

    # first_name = data.get('first_name')
    # if not first_name:
    #     raise serializers.ValidationError({'first_name': 'Пожалуйста, заполните поле имени.'})
    # custom_validate_first_name(first_name)

    # number = data.get('number')
    # if number:
    #     custom_validate_number(number)
    # print(data)
