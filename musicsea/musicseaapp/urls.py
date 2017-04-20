from  django.conf.urls import url
from  django.utils import timezone
from  django.views.generic import DetailView, ListView, UpdateView
from  models import *
from  views import *

urlpatterns = [

    url(r'^groups/$',
        GroupsList.as_view(),
        name='groups_list'),

    url(r'^artists/$',
        ArtistsList.as_view(),
        name='artists_list'),

    url(r'^albums/$',
        AlbumsList.as_view(),
        name='albums_list'),

    url(r'^songs/$',
        SongsList.as_view(),
        name='songs_list'),




    url(r'^group/(?P<pk>[a-zA-Z0-9 ]+)/$',
        GroupsDetail.as_view(),
        name='groups_detail'),

    url(r'^artist/(?P<pk>[a-zA-Z0-9 ]+)/$',
        ArtistsDetail.as_view(),
        name='artists_detail'),

    url(r'^album/(?P<pk>[a-zA-Z0-9 ]+)/$',
        AlbumsDetail.as_view(),
        name='albums_detail'),

    url(r'^song/(?P<pk>[a-zA-Z0-9 ]+)/$',
        SongsDetail.as_view(),
        name='songs_detail'),




    url(r'^groups/(?P<pk>[a-zA-Z0-9 ]+)/edit/$',
        UpdateView.as_view(
            model=Group,
            template_name='musicseaapp/form.html',
            form_class=GroupForm),
        name='groups_edit'),

    url(r'^artists/(?P<pk>[a-zA-Z0-9 ]+)/edit/$',
        UpdateView.as_view(
            model=Artist,
            template_name='musicseaapp/form.html',
            form_class=ArtistForm),
        name='artists_edit'),

    url(r'^albums/(?P<pk>[a-zA-Z0-9 ]+)/edit/$',
        UpdateView.as_view(
            model=Album,
            template_name='musicseaapp/form.html',
            form_class=AlbumForm),
        name='albums_edit'),

    url(r'^songs/(?P<pk>[a-zA-Z0-9 ]+)/edit/$',
        UpdateView.as_view(
            model=Song,
            template_name='musicseaapp/form.html',
            form_class=SongForm),
        name='songs_edit'),




    url(r'^groups/create/$',
        GroupCreate.as_view(),
        name='groups_create'),

    url(r'^artists/create/$',
        ArtistCreate.as_view(),
        name='artists_create'),

    url(r'^albums/create/$',
        AlbumCreate.as_view(),
        name='albums_create'),

    url(r'^songs/create/$',
        SongCreate.as_view(),
        name='songs_create'),
]