# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-13 02:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0021_auto_20160312_2033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentarios',
            name='user_relacion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cms.usuario'),
        ),
    ]
