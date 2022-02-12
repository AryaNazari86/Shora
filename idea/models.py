from django.db import models
from tinymce.models import HTMLField
from django.urls import reverse

# Create your models here.


class Idea(models.Model):
    subject = models.CharField(max_length=25)
    body = HTMLField('Body', null=False, blank=False, default='Nothing')
    author = models.ForeignKey(
        'account.User', on_delete=models.CASCADE, related_name='ideas')
    date_added = models.DateTimeField(auto_now_add=True, null=True)
    IDEA_TYPES = [
        ('ایده', 'ایده',),
        ('پیشنهاد', 'پیشنهاد'),
        ('انتقاد', 'انتقاد'),
    ]
    type = models.CharField(
        max_length=7,
        choices=IDEA_TYPES,
    )
    PROGRESS_SESSIONS = [
        ('در حال انتظار', 'در حال انتظار'),
        ('در حال بررسی', 'در حال بررسی'),
        ('به نتیجه رسیده', 'به نتیجه رسیده')
    ]
    progress = models.CharField(
        max_length=20,
        choices=PROGRESS_SESSIONS,
        default='در حال انتظار'
    )

    respond = models.TextField(null=True, blank=True)

    def get_absolute_url(self):
        return reverse("idea_preview", kwargs={"id": self.id})
