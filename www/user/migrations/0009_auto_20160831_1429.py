# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-31 14:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_auto_20160831_1246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myrecommend',
            name='audio_for_qian',
            field=models.CharField(default='', max_length=40),
        ),
        migrations.AlterField(
            model_name='myrecommend',
            name='audio_for_zhu',
            field=models.CharField(default='', max_length=40),
        ),
    ]
