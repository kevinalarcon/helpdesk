# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-05-11 23:07
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Enterprise', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='correo',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='name',
        ),
        migrations.AddField(
            model_name='employee',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
