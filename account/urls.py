from django.urls import path
from .views import Signin, Logout, signup

urlpatterns = [
    path('signin', Signin.as_view(), name='signin'),
    path('logout', Logout.as_view(), name='logout'),
    path('signup', signup, name='signup'),
]
