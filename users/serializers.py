from django.core.mail import EmailMessage
from django.shortcuts import get_object_or_404
from rest_framework import serializers

from config import URL
from users.models import User, EmailVerify, PasswordReset
from users.validations import custom_validate_register, custom_validate_token, custom_validate_reset_request_password, \
    custom_validate_reset_verify_password


class UserCurrentSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'last_name', 'first_name', 'number', 'password']


class UserRegistrationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'password', 'last_name', 'first_name', 'number']
        extra_kwargs = {
            "email": {
                "error_messages": {"required": "Укажите ваш email.", "blank": "Пожалуйста, заполните поле почты."}},
            "password": {
                "error_messages": {"required": "Введите пароль.", "blank": "Пожалуйста, заполните поле пароля."}},
            "last_name": {
                "error_messages": {"required": "Введите фамилию.", "blank": "Пожалуйста, заполните поле фамилии."}},
            "first_name": {
                "error_messages": {"required": "Введите имя.", "blank": "Пожалуйста, заполните поле имени."}},
            "number": {
                "error_messages": {"required": "Введите телефон.", "blank": "Пожалуйста, заполните поле телефона."}},
        }

    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password'],
            last_name=validated_data.get('last_name', ''),
            first_name=validated_data.get('first_name', ''),
            number=validated_data.get('number', ''),
            is_active=False
        )
        token = EmailVerify.objects.create(user=user)
        EmailMessage(
            'Подтверждение почты', 
            f'URL: {URL}verify/{token.url}\n{token.code}',
            to=[user.email]
        ).send()
        return user

    def validate(self, data):
        custom_validate_register(data)
        return data

class EmailTokenCreationSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmailVerify
        fields = ['code', 'url']
        extra_kwargs = {
            "code": {
                "error_messages": {"required": "Невалидный код.", "blank": "Пожалуйста, заполните поле кода."}},
            "url": {
                "error_messages": {"required": "Невалидный URL.", "blank": "Пожалуйста, заполните поле URL."}},
        }

    def create(self, validated_data):
        url = self.context.get('url')
        token = EmailVerify.objects.get(url=url)
        user = token.user
        user.email_confirmed = True
        user.is_active = True
        user.save()
        token.delete()
        return user

    def validate(self, data):
        url = self.context.get('url')
        custom_validate_token(data, url)
        return data

class PasswordResetRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = PasswordReset
        fields = ['email']
        extra_kwargs = {
            "email": {
                "error_messages": {"required": "Невалидный код.", "blank": "Пожалуйста, заполните поле email."}},
        }


    def create(self, validated_data):
        reset = PasswordReset.objects.create(email=validated_data['email'])
        EmailMessage(
            'Сброс пароля',
            f'URL: {URL}reset/password/confrim/{reset.url}\n{reset.code}',
            to=[reset.email]
        ).send()
        return reset

    def validate(self, data):
        custom_validate_reset_request_password(data)
        return data

class PasswordResetVerifySerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, error_messages={
        "required": "Невалидный URL.",
        "blank": "Пожалуйста, заполните поле password."
    })

    class Meta:
        model = PasswordReset
        fields = ['code', 'password']
        extra_kwargs = {
            "code": {
                "error_messages": {"required": "Невалидный код.", "blank": "Пожалуйста, заполните поле кода."}},
        }

    def validate(self, data):
        url = self.context.get('url')
        custom_validate_reset_verify_password(data, url)
        return data

    def create(self, validated_data):
        reset = get_object_or_404(PasswordReset, url=validated_data['url'])
        user = get_object_or_404(User, email=reset.email)
        user.set_password(validated_data['password'])
        user.save()
        reset.delete()
        return user