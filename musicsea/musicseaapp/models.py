from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db import models
from datetime import date

class Group(models.Model):
    name = models.TextField()
    genre = models.TextField()
    city = models.TextField(blank=True, null=True)
    province_or_state = models.TextField(blank=True, null=True)
    country = models.TextField(blank=True, null=True)
    birthdate = models.DateField(default=date.today)
    bibliography = models.TextField()
    image = models.ImageField(upload_to="musicsea", blank=True, null=True)
    url = models.URLField(blank=True, null=True)
    user = models.ForeignKey(User, default=1)

    def __unicode__(self):
        return u"%s" % self.name

    def get_absolute_url(self):
        return reverse('musicseaapp:groups_detail', kwargs={'pk': self.pk})

class Artist(models.Model):
    name = models.TextField()
    gender = models.TextField()
    city = models.TextField(blank=True, null=True)
    province_or_state = models.TextField(blank=True, null=True)
    country = models.TextField(blank=True, null=True)
    birthdate = models.DateField(default=date.today)
    bibliography = models.TextField()
    image = models.ImageField(upload_to="musicsea", blank=True, null=True)
    user = models.ForeignKey(User, default=1)
    group = models.ForeignKey(Group, null=True, related_name='artists')

    def __unicode__(self):
        return u"%s" % self.name

    def get_absolute_url(self):
        return reverse('musicseaapp:artists_detail', kwargs={'pk': self.pk})

class Album(models.Model):
    name = models.TextField()
    release = models.DateField(default=date.today)
    bibliography = models.TextField()
    image = models.ImageField(upload_to="musicsea", blank=True, null=True)
    user = models.ForeignKey(User, default=1)
    group = models.ForeignKey(Group, null=True, related_name='albums')

    def __unicode__(self):
        return u"%s" % self.name

    def get_absolute_url(self):
        return reverse('musicseaapp:albums_detail', kwargs={'pk': self.pk})

class Song(models.Model):
    name = models.TextField()
    lyrics = models.TextField()
    about = models.TextField()
    image = models.ImageField(upload_to="musicsea", blank=True, null=True)
    user = models.ForeignKey(User, default=1)
    album = models.ForeignKey(Album, null=True, related_name='songs')
    group = models.ForeignKey(Group, null=True, related_name='groupsongs')

    def __unicode__(self):
        return u"%s" % self.name

    def get_absolute_url(self):
        return reverse('musicseaapp:songs_detail', kwargs={'pk': self.pk})