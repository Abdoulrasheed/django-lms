# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-04-04 19:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0004_auto_20180404_2011'),
    ]

    operations = [
        migrations.AddField(
            model_name='instructor',
            name='position',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
