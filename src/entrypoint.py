import os
import django

# Установка переменной окружения для конфигурации Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

# Инициализация приложений Django
django.setup()

from users.models import User
from config import SUPERUSER_EMAIL, SUPERUSER_PASSWORD

try:
    if not User.objects.filter(email=SUPERUSER_EMAIL).exists():
        User.objects.create_superuser(
            email=SUPERUSER_EMAIL,
            password=SUPERUSER_PASSWORD,
            first_name='Admin',
            last_name='Admin',
            patronymic='Admin',
            email_confirmed=True,
        )
        print(f"Суперпользователь успешно создан.")
    else:
        print(f"Суперпользователь уже существует.")
except Exception as e:
    print(f"Ошибка при создании суперпользователя: {e}")