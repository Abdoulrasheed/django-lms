# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-04-04 19:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0005_instructor_position'),
    ]

    operations = [
        migrations.AddField(
            model_name='instructor',
            name='head_shot',
            field=models.ImageField(blank=True, null=True, upload_to=b''),
        ),
    ]
