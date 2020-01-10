# Generated by Django 2.2.4 on 2019-12-14 12:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=264, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Website',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('webName', models.CharField(max_length=264, unique=True)),
                ('url', models.URLField(unique=True)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Record')),
            ],
        ),
    ]
