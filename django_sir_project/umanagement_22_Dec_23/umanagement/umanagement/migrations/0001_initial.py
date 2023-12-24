# Generated by Django 4.2.8 on 2023-12-21 11:58

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100, unique=True)),
                ('password', models.CharField(max_length=20)),
                ('mobile', models.CharField(max_length=10)),
                ('address', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=10)),
                ('dob', models.CharField(max_length=10)),
                ('date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date published')),
                ('status', models.IntegerField(default=0)),
                ('role', models.CharField(default='user', max_length=10)),
            ],
        ),
    ]
