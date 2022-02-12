from django.urls import path
from .views import home, ideas, idea_preview, add_idea
urlpatterns = [
    path('', home, name='home'),
    path('ideas', ideas, name='ideas'),
    path('idea_preview/<int:id>/', idea_preview, name='idea_preview'),
    path('add_idea/', add_idea, name='add_idea')
]
