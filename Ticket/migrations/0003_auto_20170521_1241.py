# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-21 17:41
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Ticket', '0002_auto_20170520_0513'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Action',
            new_name='Activity',
        ),
    ]
