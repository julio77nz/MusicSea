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
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.TextField()),
                ('release', models.DateField()),
                ('bibliography', models.TextField()),
                ('image', models.ImageField(null=True, upload_to='media', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.TextField()),
                ('gender', models.TextField()),
                ('birthdate', models.DateField()),
                ('bibliography', models.TextField()),
                ('image', models.ImageField(null=True, upload_to='media', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.TextField()),
                ('genre', models.TextField()),
                ('birthdate', models.DateField()),
                ('bibliography', models.TextField()),
                ('image', models.ImageField(null=True, upload_to='media', blank=True)),
                ('url', models.URLField(null=True, blank=True)),
                ('user', models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.TextField()),
                ('lyrics', models.TextField()),
                ('about', models.TextField()),
                ('image', models.ImageField(null=True, upload_to='media', blank=True)),
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
