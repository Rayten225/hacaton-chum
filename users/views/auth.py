from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
import json

@method_decorator(csrf_exempt, name='dispatch')
class LoginView(View):
    def post(self, request, *args, **kwargs):
         data = json.loads(request.body)
         email = data.get('email')
         password = data.get('password')
         user = authenticate(request, email=email, password=password)
         if user:
             login(request, user)
             return JsonResponse({'status': 'success', 'message': 'Вы успешно вошли в систему'}, status=200)
         else:
             return JsonResponse({'status': 'error', 'message': 'Неверные учетные данные'}, status=401)

@method_decorator(csrf_exempt, name='dispatch')
class LogoutView(View):
    def post(self, request, *args, **kwargs):
        try:
            logout(request)
            return JsonResponse({'status': 'success', 'message': 'Вы успешно вышли из системы'}, status=200)
        except:
            return JsonResponse({'status': 'error', 'message': 'Вы не авторизованы'}, status=401)
