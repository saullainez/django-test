from rest_framework import generics, permissions, mixins
from rest_framework.response import Response
from .serializer import UserSerializer
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny

class RegisterApi(generics.GenericAPIView):
    permission_classes = [AllowAny]
    def post(self, request, *args,  **kwargs):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user,    context=self.get_serializer_context()).data,
            "message": "Usuario creado exitosamente. Ahora proceda a iniciar sesión ",
        })
