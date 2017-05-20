# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-07 00:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Service', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.IntegerField()),
                ('dni', models.IntegerField()),
                ('name', models.CharField(max_length=20)),
                ('phone', models.IntegerField(blank=True, null=True)),
                ('correo', models.CharField(max_length=250)),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Enterprise.Area')),
            ],
        ),
        migrations.CreateModel(
            name='Technical',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField()),
                ('boss', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='boss', to='Enterprise.Employee')),
                ('employee', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Enterprise.Employee')),
                ('services', models.ManyToManyField(to='Service.Service')),
            ],
        ),
    ]