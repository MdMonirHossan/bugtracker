from django.urls import path
from .views import UserRegistrationView

# Url patterns for user module
urlpatterns = [
    path('user/register', UserRegistrationView.as_view(), name='user_register'),
]