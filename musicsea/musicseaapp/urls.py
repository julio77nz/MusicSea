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

    url(r'^group/(?P<pk>[a-zA-Z0-9 ]+)/$',
        GroupsDetail.as_view(),
        name='groups_detail'),

    url(r'^artist/(?P<pk>[a-zA-Z0-9 ]+)/$',
        ArtistsDetail.as_view(),
        name='artists_detail'),

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

    url(r'^groups/create/$',
        GroupCreate.as_view(),
        name='groups_create'),

    url(r'^artists/create/$',
        ArtistCreate.as_view(),
        name='artists_create'),
]