# Generated by Django 3.1.7 on 2021-11-25 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('idea', '0007_idea_date_added'),
    ]

    operations = [
        migrations.AddField(
            model_name='idea',
            name='progress',
            field=models.CharField(choices=[('در حال انتظار', 'در حال انتظار'), ('در حال بررسی', 'در حال بررسی'), ('به نتیجه رسیده', 'به نتیجه رسیده')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='idea',
            name='type',
            field=models.CharField(choices=[('ایده', 'ایده'), ('پیشنهاد', 'پیشنهاد'), ('انتقاد', 'انتقاد')], max_length=7),
        ),
    ]
