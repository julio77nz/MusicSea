from  django.forms import ModelForm
from  models import *


class GroupForm(ModelForm):
    class Meta:
        model = Group
        exclude = ()

class ArtistForm(ModelForm):
    class Meta:
        model = Artist
        exclude = ()

class AlbumForm(ModelForm):
    class Meta:
        model = Album
        exclude = ()

class SongForm(ModelForm):
    class Meta:
        model = Song
        exclude = ()