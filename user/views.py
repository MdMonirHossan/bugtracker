from rest_framework import generics, permissions
from rest_framework.permissions import AllowAny
from .serializers import UserRegistrationSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class UserRegistrationView(generics.CreateAPIView):
    serializer_class = UserRegistrationSerializer
    permission_classes = (AllowAny,)

    def create(self, request, *args, **kwargs):
        '''
            Register a new user with minimal fields.
            serializers: UserRegistrationSerializer
            permission: AllowAny
        '''
        return super().create(request, *args, **kwargs)