# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-19 15:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_activity_person_limit'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='activity',
            options={'verbose_name_plural': 'activities'},
        ),
    ]
