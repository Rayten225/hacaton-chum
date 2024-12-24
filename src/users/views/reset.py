from django.core.validators import validate_email
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response

from users.models import PasswordReset
from users.serializers import PasswordResetRequestSerializer, PasswordResetVerifySerializer


class ResetPasswordRequestView(viewsets.ModelViewSet):
    serializer_class = PasswordResetRequestSerializer
    queryset = PasswordReset.objects.none()
    http_method_names = ['get', 'post' ,'head', 'options', 'list']
    permission_classes = [permissions.AllowAny]

    def list(self, request, *args, **kwargs):
        return Response(status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ResetPasswordConfrimView(viewsets.ModelViewSet):
    serializer_class = PasswordResetVerifySerializer
    queryset = PasswordReset.objects.none()
    http_method_names = ['get', 'post', 'head', 'options', 'list']
    permission_classes = [permissions.AllowAny]

    def list(self, request, *args, **kwargs):
        return Response(status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        url = kwargs.get('url')
        serializer = self.get_serializer(data=request.data, context={'url': url})
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)