# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicseaapp', '0002_auto_20170419_0419'),
    ]

    operations = [
        migrations.RenameField(
            model_name='song',
            old_name='bibliography',
            new_name='about',
        ),
    ]
