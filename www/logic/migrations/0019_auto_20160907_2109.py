# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-07 21:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logic', '0018_auto_20160907_2001'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='share',
            name='last_share_uuid',
        ),
        migrations.AddField(
            model_name='share',
            name='last_share_id',
            field=models.IntegerField(default=0),
        ),
    ]
