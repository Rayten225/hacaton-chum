from django.urls import path, include
from rest_framework import routers

from users.views.auth import LoginView, LogoutView
from users.views.registration import UserRegistrationView
from users.views.token import EmailTokenConfirmationView
from users.views.reset import ResetPasswordRequestView, ResetPasswordConfrimView

router = routers.DefaultRouter()

router.register(r'reset/password', ResetPasswordRequestView, basename='reset-password-create')

urlpatterns = [
    path('', include(router.urls)),
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('verify/<str:url>/', EmailTokenConfirmationView.as_view({'post': 'create'}), name='verify'),
    path('reset/password/confirm/<str:url>/', ResetPasswordConfrimView.as_view({'post': 'create'}), name='reset-password-verify'),
]