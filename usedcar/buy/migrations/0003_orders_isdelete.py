# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-08-29 11:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buy', '0002_auto_20180824_1035'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='isDelete',
            field=models.BooleanField(default=False, verbose_name='是否删除'),
        ),
    ]