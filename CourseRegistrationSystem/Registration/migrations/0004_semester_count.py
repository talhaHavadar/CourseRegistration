# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-17 14:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Registration', '0003_auto_20160517_1420'),
    ]

    operations = [
        migrations.AddField(
            model_name='semester',
            name='count',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]