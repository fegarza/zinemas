# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-09 01:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0004_auto_20160308_1918'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentario',
            name='contenido',
            field=models.CharField(max_length=600),
        ),
    ]
