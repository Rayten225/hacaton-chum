from django.urls import path

from admin_panel.views.admin_login import admin_login
from admin_panel.views.admin_main import admin_main
from admin_panel.views.user import account

urlpatterns = [
    path('', admin_main, name='admin-main'),
    path('login', admin_login, name='admin-login'),
    path('account', account, name='account'),
]

