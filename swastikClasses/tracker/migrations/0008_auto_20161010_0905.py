# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-10-10 09:05
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0007_auto_20161010_0847'),
    ]

    operations = [
        migrations.RenameField(
            model_name='time',
            old_name='Rooms',
            new_name='rooms',
        ),
    ]
