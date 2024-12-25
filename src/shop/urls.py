from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from rest_framework import routers

from shop.views.views import ProductViewSet

urlpatterns = [
    path('', ProductViewSet.as_view({'post': 'create'}), name='api'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)