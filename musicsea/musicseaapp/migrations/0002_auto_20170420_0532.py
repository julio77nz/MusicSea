# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicseaapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='image',
            field=models.ImageField(null=True, upload_to='media', blank=True),
        ),
        migrations.AlterField(
            model_name='artist',
            name='image',
            field=models.ImageField(null=True, upload_to='media', blank=True),
        ),
        migrations.AlterField(
            model_name='group',
            name='image',
            field=models.ImageField(null=True, upload_to='media', blank=True),
        ),
        migrations.AlterField(
            model_name='song',
            name='image',
            field=models.ImageField(null=True, upload_to='media', blank=True),
        ),
    ]
