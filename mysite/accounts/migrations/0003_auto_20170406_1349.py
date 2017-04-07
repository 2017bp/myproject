# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-06 18:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_user_date_joined'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='first_name',
            field=models.CharField(default='Derek', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='last_name',
            field=models.CharField(default='Yu', max_length=30),
            preserve_default=False,
        ),
    ]
