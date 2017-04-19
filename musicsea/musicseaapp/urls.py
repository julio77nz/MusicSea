from  django.conf.urls import url
from  django.utils import timezone
from  django.views.generic import DetailView, ListView, UpdateView
from  models import Group, Artist
from  forms import GroupForm, ArtistForm
from  views import GroupCreate, ArtistCreate, GroupDetail

urlpatterns = [



    #  Group  details,  ex.:  /musicseaapp/groups/1/
    url(r'^groups/(?P<pk>\d+)/$',
        GroupDetail.as_view(),
        name='group_detail'),

    #  Group  artist  details,  ex:  /musicseaapp/groups/1/artists/1/
    url(r'^groups/(?P<pkr>\d+)/artists/(?P<pk>\d+)/$',
        DetailView.as_view(
            model=Artist,
            template_name='musicseaapp/artist_detail.html'),
        name='artist_detail'),

    #  Create  a  groups,  /musicseaapp/groups/create/
    url(r'^groups/create/$',
        GroupCreate.as_view(),
        name='group_create'),

    #  Edit  group  details,  ex.:  /musicseapp/groups/1/edit/
    url(r'^groups/(?P<pk>\d+)/edit/$',
        UpdateView.as_view(
            model=Group,
            template_name='musicseaapp/form.html',
            form_class=GroupForm),
        name='group_edit'),

    #  Create  a  group  artist,  ex.:  /musicseaapp/groups/1/artists/create/
    url(r'^groups/(?P<pk>\d+)/artists/create/$',
        ArtistCreate.as_view(),
        name='artist_create'),

    #  Edit  group  artist  details,  ex.:  /musicseaapp/groups/1/artists/1/edit/
    url(r'^groups/(?P<pkr>\d+)/artists/(?P<pk>\d+)/edit/$',
        UpdateView.as_view(
            model=Artist,
            template_name='musicseaapp/form.html',
            form_class=ArtistForm),
        name='artist_edit'),
]