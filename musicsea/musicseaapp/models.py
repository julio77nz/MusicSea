from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db import models

class Group(models.Model):
    name = models.TextField(unique=True, primary_key=True)
    genre = models.TextField()
    birthdate = models.DateField()
    bibliography = models.TextField()
    image = models.ImageField(upload_to="media", blank=True, null=True)
    url = models.URLField(blank=True, null=True)
    user = models.ForeignKey(User, default=1)

    def __unicode__(self):
        return u"%s" % self.name

    def get_absolute_url(self):
        return reverse('musicseaapp:groups_detail', kwargs={'pk': self.pk})

class Artist(models.Model):
    name = models.TextField(unique=True, primary_key=True)
    gender = models.TextField()
    birthdate = models.DateField()
    bibliography = models.TextField()
    image = models.ImageField(upload_to="media", blank=True, null=True)
    user = models.ForeignKey(User, default=1)
    group = models.ForeignKey(Group, null=True, related_name='artists')

    def __unicode__(self):
        return u"%s" % self.name

    def get_absolute_url(self):
        return reverse('musicseaapp:artists_detail', kwargs={'pk': self.pk})

class Album(models.Model):
    name = models.TextField(unique=True, primary_key=True)
    release = models.DateField()
    bibliography = models.TextField()
    image = models.ImageField(upload_to="media", blank=True, null=True)
    user = models.ForeignKey(User, default=1)
    group = models.ForeignKey(Group, null=True, related_name='albums')

    def __unicode__(self):
        return u"%s" % self.name

    def get_absolute_url(self):
        return reverse('musicseaapp:albums_detail', kwargs={'pk': self.pk})

class Song(models.Model):
    name = models.TextField(unique=True, primary_key=True)
    lyrics = models.TextField()
    about = models.TextField()
    image = models.ImageField(upload_to="media", blank=True, null=True)
    user = models.ForeignKey(User, default=1)
    album = models.ForeignKey(Album, null=True, related_name='songs')
    group = models.ForeignKey(Group, null=True, related_name='groupsongs')

    def __unicode__(self):
        return u"%s" % self.name

    def get_absolute_url(self):
        return reverse('musicseaapp:songs_detail', kwargs={'pk': self.pk})