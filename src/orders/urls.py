from django.urls import path, include

from orders.views import OrdersViewSet


urlpatterns = [
    path('', OrdersViewSet.as_view(), name='orders'),
]