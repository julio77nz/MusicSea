from django.contrib.auth.models import User
from django.db import models

class Group(models.Model):
    name = models.TextField()
    genre = models.TextField()
    birthdate = models.DateField()
    bibliography = models.TextField()
    image = models.TextField()
    user = models.ForeignKey(User, default=1)

    def __unicode__(self):
        return u"%s" % self.name

class Artist(models.Model):
    name = models.TextField()
    gender = models.TextField()
    birthdate = models.DateField()
    bibliography = models.TextField()
    image = models.TextField()
    user = models.ForeignKey(User, default=1)
    group = models.ForeignKey(Group, null=True, related_name='artists')

    def __unicode__(self):
        return u"%s" % self.name

class Album(models.Model):
    name = models.TextField()
    release = models.DateField()
    bibliography = models.TextField()
    image = models.TextField()
    user = models.ForeignKey(User, default=1)
    group = models.ForeignKey(Group, null=True, related_name='albums')

    def __unicode__(self):
        return u"%s" % self.name

class Song(models.Model):
    name = models.TextField()
    lyrics = models.TextField()
    about = models.TextField()
    image = models.TextField()
    user = models.ForeignKey(User, default=1)
    album = models.ForeignKey(Album, null=True, related_name='songs')
    group = models.ForeignKey(Group, null=True, related_name='groupsongs')

    def __unicode__(self):
        return u"%s" % self.name