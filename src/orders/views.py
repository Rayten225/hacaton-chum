from rest_framework import viewsets, permissions, status  # Импорты для апи
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
import json

from rest_framework.response import Response

#Импорты нашей модели и сериализатора для отправки сообщений
from orders.models import Order
from orders.serialaizer import OrdersCreationSerializer  
  
  
@method_decorator(csrf_exempt, name='dispatch')
class OrdersViewSet(View):
    def post(self, request, format=None, *args, **kwargs):
        serializer = OrdersCreationSerializer(data=json.loads(request.body.decode('utf-8')))
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'status': 'success', 'message': 'Заказ успешно отправлен'}, status=200)
        
        return JsonResponse({'status': 'error', 'message': 'Ошибка заказа'}, status=401)

    # def list(self, request, *args, **kwargs):
    #     return Response(status=status.HTTP_200_OK)