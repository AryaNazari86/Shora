from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
# Create your views here.
User = get_user_model()


class Signin(LoginView):
    redirect_field_name = 'idea/ideas.html'
    template_name = 'account/signin.html'


class Logout(LogoutView):
    template_name = 'account/signin.html'


def signup(request):

    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        password = (request.POST['password'])
        User.objects.create_user(
            username=username, first_name=first_name, last_name=last_name, password=password)
        return redirect('signin')
    else:
        return render(request, 'account/signup.html')
