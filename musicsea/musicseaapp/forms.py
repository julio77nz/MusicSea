from  django.forms import ModelForm
from  models import Group, Artist


class GroupForm(ModelForm):
    class Meta:
        model = Group
        exclude = ('user', 'date',)


class ArtistForm(ModelForm):
    class Meta:
        model = Artist
        exclude = ('user', 'date', 'group',)