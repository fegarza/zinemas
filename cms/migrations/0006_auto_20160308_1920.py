# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-09 01:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0005_auto_20160308_1919'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comentario',
            old_name='user',
            new_name='user_relacion',
        ),
        migrations.RenameField(
            model_name='comentario',
            old_name='videopk',
            new_name='video_relacion',
        ),
        migrations.AlterField(
            model_name='comentario',
            name='contenido',
            field=models.TextField(max_length=600),
        ),
    ]
