# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-09 01:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0013_ok'),
    ]

    operations = [
        migrations.CreateModel(
            name='comentarios',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cont', models.TextField(max_length=600, null=True)),
                ('video_relacion', models.CharField(max_length=1900)),
                ('user_relacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cms.usuario')),
            ],
        ),
        migrations.DeleteModel(
            name='comentario',
        ),
        migrations.DeleteModel(
            name='ok',
        ),
    ]
