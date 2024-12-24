from rest_framework import viewsets, permissions, status
from rest_framework.response import Response

from users.models import EmailVerify
from users.serializers import EmailTokenCreationSerializer

class EmailTokenConfirmationView(viewsets.ModelViewSet):
    serializer_class = EmailTokenCreationSerializer
    queryset = EmailVerify.objects.none()
    http_method_names = ['get', 'post' ,'head', 'options', 'list']
    permission_classes = [permissions.AllowAny]

    def list(self, request, *args, **kwargs):
        return Response(status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        url = kwargs.get('url')
        serializer = self.get_serializer(data=request.data, context={'url': url})
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)