# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-05-05 17:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0028_remove_video_vistas'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='vistas',
            field=models.IntegerField(default=0),
        ),
    ]
