# Generated by Django 3.1.7 on 2021-11-25 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('idea', '0005_auto_20211125_1730'),
    ]

    operations = [
        migrations.AlterField(
            model_name='idea',
            name='type',
            field=models.CharField(choices=[('ایده', 'ایده'), ('پیشنهاد', 'پیشنهاد'), ('انتقاد', 'انتقاد')], default='idea', max_length=7),
        ),
    ]
