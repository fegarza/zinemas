# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-09 01:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0010_comentarios'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comentarios',
            name='user_relacion',
        ),
        migrations.DeleteModel(
            name='comentarios',
        ),
    ]
