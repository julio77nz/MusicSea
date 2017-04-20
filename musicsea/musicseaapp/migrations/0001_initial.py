# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('name', models.TextField(unique=True, serialize=False, primary_key=True)),
                ('release', models.DateField()),
                ('bibliography', models.TextField()),
                ('image', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('name', models.TextField(unique=True, serialize=False, primary_key=True)),
                ('gender', models.TextField()),
                ('birthdate', models.DateField()),
                ('bibliography', models.TextField()),
                ('image', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('name', models.TextField(unique=True, serialize=False, primary_key=True)),
                ('genre', models.TextField()),
                ('birthdate', models.DateField()),
                ('bibliography', models.TextField()),
                ('image', models.TextField()),
                ('url', models.URLField(null=True, blank=True)),
                ('user', models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('name', models.TextField(unique=True, serialize=False, primary_key=True)),
                ('lyrics', models.TextField()),
                ('about', models.TextField()),
                ('image', models.TextField()),
                ('album', models.ForeignKey(related_name='songs', to='musicseaapp.Album', null=True)),
                ('group', models.ForeignKey(related_name='groupsongs', to='musicseaapp.Group', null=True)),
                ('user', models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='artist',
            name='group',
            field=models.ForeignKey(related_name='artists', to='musicseaapp.Group', null=True),
        ),
        migrations.AddField(
            model_name='artist',
            name='user',
            field=models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='album',
            name='group',
            field=models.ForeignKey(related_name='albums', to='musicseaapp.Group', null=True),
        ),
        migrations.AddField(
            model_name='album',
            name='user',
            field=models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL),
        ),
    ]
