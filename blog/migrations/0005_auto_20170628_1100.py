# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-06-28 09:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20170628_1052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='illustration',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]
