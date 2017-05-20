# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-07 00:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Enterprise', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alternative',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Poll',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True, null=True)),
                ('alternative', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Poll.Alternative')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Enterprise.Employee')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('statement', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='alternative',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Poll.Question'),
        ),
    ]