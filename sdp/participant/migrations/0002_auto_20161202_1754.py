# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-02 09:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('participant', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='finish_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
