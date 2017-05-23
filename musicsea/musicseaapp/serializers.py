from  rest_framework.fields  import  CharField
from  rest_framework.relations  import  HyperlinkedRelatedField,  HyperlinkedIdentityField
from  rest_framework.serializers  import  HyperlinkedModelSerializer
from models import *

class GroupSerializer(HyperlinkedModelSerializer):
    uri = HyperlinkedIdentityField(view_name='musicseaapp:group-detail')
    artists = HyperlinkedRelatedField(many=True, read_only=True,
                                    view_name='musicseaapp:artist-detail')
    albums = HyperlinkedRelatedField(many=True, read_only=True,
                                    view_name='musicseaapp:album-detail')
    groupsongs = HyperlinkedRelatedField(many=True, read_only=True,
                                        view_name='musicseaapp:song-detail')
    user = CharField(read_only=True)

    class Meta:
        model = Group
        fields = ('uri', 'name', 'genre', 'city', 'province_or_state', 'country', 'birthdate', 'bibliography',
                  'image','artists','albums','groupsongs', 'url', 'user')

class ArtistSerializer(HyperlinkedModelSerializer):
    uri = HyperlinkedIdentityField(view_name='musicseaapp:artist-detail')
    group = HyperlinkedRelatedField(view_name='musicseaapp:group-detail', read_only=True)
    user = CharField(read_only=True)

    class Meta:
        model = Artist
        fields = ('uri', 'name', 'group', 'gender', 'city', 'province_or_state', 'country', 'birthdate', 'bibliography',
                  'image', 'user')

class AlbumSerializer(HyperlinkedModelSerializer):
    uri = HyperlinkedIdentityField(view_name='musicseaapp:album-detail')
    group = HyperlinkedRelatedField(view_name='musicseaapp:group-detail', read_only=True)
    songs = HyperlinkedRelatedField(many=True, read_only=True,
                                        view_name='musicseaapp:song-detail')
    user = CharField(read_only=True)

    class Meta:
        model = Album
        fields = ('uri', 'name', 'group', 'songs', 'release', 'bibliography', 'image', 'user')


class SongSerializer(HyperlinkedModelSerializer):
    uri = HyperlinkedIdentityField(view_name='musicseaapp:album-detail')
    group = HyperlinkedRelatedField(view_name='musicseaapp:group-detail', read_only=True)
    album = HyperlinkedRelatedField(view_name='musicseaapp:album-detail', read_only=True)
    user = CharField(read_only=True)

    class Meta:
        model = Song
        fields = ('uri', 'name', 'album', 'group', 'lyrics', 'about', 'image', 'user')