from  django.forms import ModelForm
from  models import *


class GroupForm(ModelForm):
    class Meta:
        model = Group
        exclude = ('user',)

class ArtistForm(ModelForm):
    class Meta:
        model = Artist
        exclude = ('user',)

class AlbumForm(ModelForm):
    class Meta:
        model = Album
        exclude = ('user',)

class SongForm(ModelForm):
    class Meta:
        model = Song
        exclude = ('user',)