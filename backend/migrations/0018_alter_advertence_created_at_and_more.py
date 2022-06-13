# Generated by Django 4.0.3 on 2022-06-11 02:30

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0017_alter_advertence_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertence',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 11, 2, 30, 13, 946846, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 11, 2, 30, 13, 862325, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='role',
            field=models.CharField(default=None, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='manager',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 11, 2, 30, 13, 864320, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='merit',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 11, 2, 30, 13, 955828, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='role',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 11, 2, 30, 13, 862325, tzinfo=utc), null=True),
        ),
    ]
