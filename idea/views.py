from django.shortcuts import render, HttpResponse
from account.views import Signin
# Create your views here.


def home(request):
    if request.user.username:
        return ideas(request)
    else:
        return render(request, 'account/signin.html')


def ideas(request):
    return render(request, 'idea/ideas.html', {'ideas': request.user.ideas.all()})
