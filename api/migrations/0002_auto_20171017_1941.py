# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-17 19:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transport',
            name='cost_in_credits',
            field=models.IntegerField(),
        ),
    ]
