# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicseaapp', '0003_auto_20170419_0431'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='group',
            field=models.ForeignKey(related_name='groupsongs', to='musicseaapp.Group', null=True),
        ),
    ]
