# Generated by Django 3.0.5 on 2020-04-17 16:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reviseApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='school',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='students', to='reviseApp.School'),
        ),
    ]
