from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from project import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/user/', include('users.urls')),
    path('', include('admin_panel.urls')),
    path('api/shop', include('shop.urls')),
    path('api/orders', include('orders.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)