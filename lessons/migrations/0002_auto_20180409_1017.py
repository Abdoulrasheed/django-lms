# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-09 09:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='instructor',
            name='google_plus',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='instructor',
            name='pinterest',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
