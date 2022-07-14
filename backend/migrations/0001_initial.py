# Generated by Django 4.0.3 on 2022-03-27 01:23

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(default=None, max_length=50, unique=True)),
                ('address', models.CharField(default=None, max_length=50)),
                ('pis', models.CharField(default=None, max_length=12, unique=True)),
                ('is_active', models.BooleanField(default=True)),
                ('hired_at', models.DateTimeField(default=None)),
                ('created_at', models.DateTimeField(default=datetime.datetime(2022, 3, 27, 1, 23, 9, 595237, tzinfo=utc))),
                ('user', models.CharField(max_length=50, unique=True)),
                ('password', models.CharField(max_length=30)),
                ('updated_at', models.DateTimeField(default=None)),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(default=datetime.datetime(2022, 3, 27, 1, 23, 9, 592238, tzinfo=utc))),
                ('updated_at', models.DateTimeField(default=None)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('age', models.IntegerField(default=None)),
                ('email', models.CharField(default=None, max_length=50, unique=True)),
                ('address', models.CharField(default=None, max_length=150)),
                ('rg', models.CharField(default=None, max_length=12, unique=True)),
                ('pis', models.CharField(default=None, max_length=12, unique=True)),
                ('is_active', models.BooleanField(default=True)),
                ('nationality', models.CharField(max_length=50)),
                ('salary', models.FloatField(default=None)),
                ('phone', models.CharField(default=None, max_length=20, unique=True)),
                ('sex', models.CharField(default=None, max_length=20)),
                ('created_at', models.DateTimeField(default=datetime.datetime(2022, 3, 27, 1, 23, 9, 593237, tzinfo=utc))),
                ('hired_at', models.DateTimeField(default=None)),
                ('updated_at', models.DateTimeField(default=None)),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.role')),
            ],
        ),
    ]
