# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-02-26 15:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mgmt', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='field',
            name='alias',
            field=models.CharField(max_length=20, null=True, verbose_name='别名'),
        ),
    ]
