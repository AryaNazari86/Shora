from django.db import models
# Create your models here.


class Article(models.Model):
    subject = models.CharField(max_length=25)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True, null=True)
    image = models.ImageField(
        upload_to='images/articles/')
