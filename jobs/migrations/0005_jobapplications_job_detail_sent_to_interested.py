# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-03 11:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0004_auto_20160803_1140'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobapplications',
            name='job_detail_sent_to_interested',
            field=models.NullBooleanField(),
        ),
    ]
