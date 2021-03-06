# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-09-08 19:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fobi', '0004_auto_20160906_1513'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formelement',
            name='plugin_uid',
            field=models.CharField(editable=False, max_length=255, unique=True, verbose_name='Plugin UID'),
        ),
        migrations.AlterField(
            model_name='formelemententry',
            name='plugin_uid',
            field=models.CharField(max_length=255, verbose_name='Plugin name'),
        ),
    ]
