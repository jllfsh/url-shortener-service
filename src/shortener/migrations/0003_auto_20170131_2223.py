# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-31 20:23
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0002_urlshortener_short_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='urlshortener',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2017, 1, 31, 20, 23, 7, 946232, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='urlshortener',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
