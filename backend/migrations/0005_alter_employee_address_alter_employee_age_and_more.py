# Generated by Django 4.0.3 on 2022-04-09 20:01

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0004_alter_employee_created_at_alter_employee_role_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='address',
            field=models.CharField(default=None, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='age',
            field=models.IntegerField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 9, 20, 1, 39, 431429, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='email',
            field=models.CharField(default=None, max_length=50, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='is_active',
            field=models.BooleanField(default=True, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='nationality',
            field=models.CharField(default=None, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='phone',
            field=models.CharField(default=None, max_length=20, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='pis',
            field=models.CharField(default=None, max_length=12, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='rg',
            field=models.CharField(default=None, max_length=12, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='salary',
            field=models.FloatField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='sex',
            field=models.CharField(default=None, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='manager',
            name='address',
            field=models.CharField(default=None, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='manager',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 9, 20, 1, 39, 431429, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='manager',
            name='email',
            field=models.CharField(default=None, max_length=50, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='manager',
            name='hired_at',
            field=models.DateTimeField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='manager',
            name='is_active',
            field=models.BooleanField(default=True, null=True),
        ),
        migrations.AlterField(
            model_name='manager',
            name='pis',
            field=models.CharField(default=None, max_length=12, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='manager',
            name='updated_at',
            field=models.DateTimeField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='role',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 9, 20, 1, 39, 431429, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='role',
            name='is_active',
            field=models.BooleanField(default=True, null=True),
        ),
        migrations.AlterField(
            model_name='role',
            name='updated_at',
            field=models.DateTimeField(default=None, null=True),
        ),
    ]
