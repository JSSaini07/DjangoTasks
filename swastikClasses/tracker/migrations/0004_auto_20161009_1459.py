# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-10-09 14:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0003_auto_20161009_1427'),
    ]

    operations = [
        migrations.AlterField(
            model_name='time',
            name='date',
            field=models.DateField(),
        ),
    ]
