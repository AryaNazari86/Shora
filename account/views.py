from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
# Create your views here.


class Signin(LoginView):
    redirect_field_name = 'idea/ideas.html'
    template_name = 'account/signin.html'


class Logout(LogoutView):
    template_name = 'account/signout.html'
