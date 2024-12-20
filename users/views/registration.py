from users.models import User
from users.serializers import UserRegistrationsSerializer
from django.contrib.auth import logout
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
import json

@method_decorator(csrf_exempt, name='dispatch')
class UserRegistrationView(View):
    def post(self, request, format=None, *args, **kwargs):
        serializer = UserRegistrationsSerializer(data=json.loads(request.body.decode('utf-8')))
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'status': 'success', 'message': 'Вы успешно зарегались в систему'}, status=200)
        return JsonResponse({'status': 'error', 'message': 'Неверные учетные данные'}, status=401)
             

@method_decorator(csrf_exempt, name='dispatch')
class LogoutView(View):
    def post(self, request, *args, **kwargs):
        try:
            logout(request)
            return JsonResponse({'status': 'success', 'message': 'Вы успешно вышли из системы'}, status=200)
        except:
            return JsonResponse({'status': 'error', 'message': 'Вы не авторизованы'}, status=401)
