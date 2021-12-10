# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2021-10-09 21:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("workflow", "0044_auto_20211002_1733"),
    ]

    operations = [
        migrations.AddField(
            model_name="state",
            name="is_allow_skip",
            field=models.BooleanField(default=False, verbose_name="是否允许在单据处理人为空时跳过"),
        ),
    ]
