# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-09 01:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0006_auto_20160308_1920'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comentario',
            old_name='contenido',
            new_name='cont',
        ),
    ]
