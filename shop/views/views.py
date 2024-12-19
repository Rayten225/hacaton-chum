from rest_framework import viewsets, permissions #Импорты для апи 

from shop.models import Product  
from shop.serialaizer import ProductCreationSerializer  
  
  
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    http_method_names = ['get', 'post' ,'head', 'options', 'list', 'delete'] 
    permission_classes = [permissions.IsAuthenticated] 
    serializer_class = ProductCreationSerializer
    