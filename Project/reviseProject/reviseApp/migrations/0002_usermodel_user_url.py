# Generated by Django 3.0.5 on 2020-04-15 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviseApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermodel',
            name='user_url',
            field=models.URLField(blank=True),
        ),
    ]
