# Generated by Django 4.0.3 on 2022-04-10 05:46

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0012_alter_advertence_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertence',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 10, 5, 46, 8, 387413, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 10, 5, 46, 8, 327413, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='manager',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 10, 5, 46, 8, 328413, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='role',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 10, 5, 46, 8, 327413, tzinfo=utc), null=True),
        ),
        migrations.CreateModel(
            name='PresenceControl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=None, null=True)),
                ('is_present_morning', models.BooleanField(default=None, null=True)),
                ('is_present_afternoon', models.BooleanField(default=None, null=True)),
                ('note', models.CharField(max_length=250, null=True)),
                ('employee', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='backend.employee')),
                ('manager', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='backend.manager')),
            ],
        ),
    ]
