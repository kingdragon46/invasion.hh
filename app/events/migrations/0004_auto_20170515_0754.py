# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-15 07:54
from __future__ import unicode_literals

from django.db import migrations, models
import events.models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_auto_20170515_0746'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invader',
            name='payment_reference',
            field=models.CharField(default=events.models.create_payment_reference, max_length=40),
        ),
    ]