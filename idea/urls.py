from django.urls import path
from .views import home, ideas
urlpatterns = [
    path('', home, name='home'),
    path('ideas', ideas, name='ideas')
]
