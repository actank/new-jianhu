# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-05 17:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logic', '0010_beinterested_be_interested_uuid'),
    ]

    operations = [
        migrations.AddField(
            model_name='share',
            name='job_id',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
