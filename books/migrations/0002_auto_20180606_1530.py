# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-06 15:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publisher',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]
