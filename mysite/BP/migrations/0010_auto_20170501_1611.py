# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-01 21:11
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('BP', '0009_auto_20170501_1547'),
    ]

    operations = [
        migrations.AddField(
            model_name='posting',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]