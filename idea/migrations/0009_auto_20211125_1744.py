# Generated by Django 3.1.7 on 2021-11-25 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('idea', '0008_auto_20211125_1743'),
    ]

    operations = [
        migrations.AlterField(
            model_name='idea',
            name='progress',
            field=models.CharField(choices=[('در حال انتظار', 'در حال انتظار'), ('در حال بررسی', 'در حال بررسی'), ('به نتیجه رسیده', 'به نتیجه رسیده')], default='در حال انتظار', max_length=20),
        ),
    ]