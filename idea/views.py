from django.shortcuts import render, HttpResponse, redirect
from account.views import Signin
from .models import Idea
from article.models import Article

# Create your views here.


def home(request):
    return render(request, 'home.html', {'articles': Article.objects.all()})


def ideas(request):
    return render(request, 'idea/ideas.html', {'ideas': request.user.ideas.all()})


def idea_preview(request, id):
    if not request.user.username:
        return redirect('account/signin')

    idea = Idea.objects.filter(id=id).first()

    print(idea.respond)

    return render(request, 'idea/idea_preview.html', {'idea': idea})


def add_idea(request):
    if request.method == 'GET':
        return render(request, 'idea/add_idea.html')
    else:
        subject = request.POST['subject']
        if subject == '':
            subject = 'چرا هیچی ننوشتی؟'
        body = request.POST['body']
        author = request.user
        idea_type = request.POST['type']
        if idea_type == 'نوع ایده‌ی خود را انتخاب کنید':
            idea_type = 'ایده'
        progress = 'در حال انتظار'
        Idea.objects.create(subject=subject, body=body,
                            author=author, type=idea_type, progress=progress)
        return redirect('ideas')
