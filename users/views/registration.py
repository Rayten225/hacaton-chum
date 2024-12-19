# from rest_framework import viewsets, permissions, status
# from rest_framework.response import Response
# from django.views.decorators.csrf import csrf_exempt
# from django.utils.decorators import method_decorator

from users.models import User
from users.serializers import UserRegistrationsSerializer

# @method_decorator(csrf_exempt, name='dispatch')
# class UserRegistrationView(viewsets.ModelViewSet):
#     serializer_class = UserRegistrationsSerializer
#     queryset = User.objects.none()
#     http_method_names = ['get', 'post' ,'head', 'options', 'list']
#     permission_classes = (permissions.AllowAny,)
#     authentications_classes = []
#     def list(self, request, *args, **kwargs):
#         if request.user.is_authenticated:
#             serializer = self.get_serializer(request.user)
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(status=status.HTTP_400_BAD_REQUEST)

#     def create(self, request, *args, **kwargs):
        
#         serializer = self.get_serializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

from django.contrib.auth import authenticate, login, logout
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
