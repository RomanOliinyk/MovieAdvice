# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-04 09:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recommendation', '0002_movie_genres'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='moviecast',
            name='cast_id',
        ),
    ]
