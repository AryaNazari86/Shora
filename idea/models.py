from django.db import models
from tinymce.models import HTMLField

# Create your models here.


class Idea(models.Model):
    subject = models.CharField(max_length=25)
    body = HTMLField('Body', null=False, blank=False, default='Nothing')
    author = models.ForeignKey('account.User', on_delete=models.CASCADE)
    IDEA_TYPES = [
        ('idea', 'ایده'),
        ('offer', 'پیشنهاد'),
        ('comment', 'انتقاد'),
    ]
    type = models.CharField(
        max_length=7,
        choices=IDEA_TYPES,
        default='idea',
    )
