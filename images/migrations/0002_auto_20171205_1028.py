# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-05 07:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='location',
            field=models.CharField(default='Nairobi', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.CharField(default='gitu', max_length=30),
            preserve_default=False,
        ),
    ]