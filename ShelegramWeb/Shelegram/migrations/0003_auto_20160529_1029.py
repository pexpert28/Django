# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-29 10:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shelegram', '0002_auto_20160529_1014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shelegramuser',
            name='picture',
            field=models.ImageField(blank=True, default='/static/media/images/avatars/default.png', upload_to='/static/media/images/avatars/'),
        ),
    ]