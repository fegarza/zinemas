# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-05-15 03:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0036_auto_20160511_1904'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='descripcion',
        ),
    ]
