# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-13 02:33
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0019_auto_20160312_1650'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, unique=True),
        ),
    ]
