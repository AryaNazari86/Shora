from django.urls import path
from .views import Signin

urlpatterns = [
    path('SignIn', Signin.as_view(), name='signin'),
]
