from django.urls import path, include
from rest_framework import routers

from shop.views.views import ProductViewSet  


# router.register(r'register', UserRegistrationView, basename='register')

urlpatterns = [
    path('', ProductViewSet.as_view({'post': 'create'}), name='api'),
]