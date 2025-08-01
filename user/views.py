from rest_framework import generics
from rest_framework.permissions import AllowAny
from .serializers import UserRegistrationSerializer

# Create your views here.

class UserRegistrationView(generics.CreateAPIView):
    '''
        User Register view
    ''' 
    serializer_class = UserRegistrationSerializer
    permission_classes = (AllowAny,)

    def create(self, request, *args, **kwargs):
        '''
            Register a new user with minimal fields.
            serializers: UserRegistrationSerializer
            permission: AllowAny
        '''
        return super().create(request, *args, **kwargs)