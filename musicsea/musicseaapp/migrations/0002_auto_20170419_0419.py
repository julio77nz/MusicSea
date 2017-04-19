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
            name='bibliography',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='artist',
            name='bibliography',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='group',
            name='bibliography',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='song',
            name='bibliography',
            field=models.TextField(),
        ),
    ]
