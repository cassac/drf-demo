# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-04 19:06
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20160304_1904'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Pictures',
            new_name='Picture',
        ),
    ]
