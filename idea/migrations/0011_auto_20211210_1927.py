# Generated by Django 3.1.7 on 2021-12-10 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('idea', '0010_idea_respond'),
    ]

    operations = [
        migrations.AlterField(
            model_name='idea',
            name='respond',
            field=models.TextField(blank=True, null=True),
        ),
    ]
