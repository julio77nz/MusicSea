from django.shortcuts import render
from django.views.generic import DetailView, ListView
from django.http import HttpResponse
from django.views.generic.base import TemplateResponseMixin
from django.core import serializers
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.edit import DeleteView
from models import *
from django.shortcuts import redirect
from django.core.urlresolvers import reverse, reverse_lazy
from forms import *
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class LoginRequiredMixin(object):
    @method_decorator(login_required())
    def dispatch(self, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(*args, **kwargs)


class CheckIsOwnerMixin(object):
    def get_object(self, *args, **kwargs):
        obj = super(CheckIsOwnerMixin, self).get_object(*args, **kwargs)
        if not obj.user == self.request.user:
            raise PermissionDenied
        return obj


class LoginRequiredCheckIsOwnerUpdateView(LoginRequiredMixin, CheckIsOwnerMixin, UpdateView):
    template_name = 'musicseaapp/form.html'




def mainpage(request):
    return render(request, 'musicseaapp/mainpage.html')


class GroupsList(ListView):
    model = Group
    queryset = Group.objects.all()
    context_object_name = 'groups'
    template_name = 'musicseaapp/groups_list.html'

class ArtistsList(ListView):
    model = Artist
    queryset = Artist.objects.all()
    context_object_name = 'artists'
    template_name = 'musicseaapp/artists_list.html'

class AlbumsList(ListView):
    model = Album
    queryset = Album.objects.all()
    context_object_name = 'albums'
    template_name = 'musicseaapp/albums_list.html'

class SongsList(ListView):
    model = Song
    queryset = Song.objects.all()
    context_object_name = 'songs'
    template_name = 'musicseaapp/songs_list.html'




class GroupsDetail(DetailView):
    model = Group
    template_name = 'musicseaapp/groups_detail.html'

class ArtistsDetail(DetailView):
    model = Artist
    template_name = 'musicseaapp/artists_detail.html'

class AlbumsDetail(DetailView):
    model = Album
    template_name = 'musicseaapp/albums_detail.html'

class SongsDetail(DetailView):
    model = Song
    template_name = 'musicseaapp/songs_detail.html'




class GroupCreate(CreateView):
    model = Group
    template_name = 'musicseaapp/form.html'
    form_class = GroupForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(GroupCreate, self).form_valid(form)

class ArtistCreate(CreateView):
    model = Artist
    template_name = 'musicseaapp/form.html'
    form_class = ArtistForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(ArtistCreate, self).form_valid(form)

class AlbumCreate(CreateView):
    model = Album
    template_name = 'musicseaapp/form.html'
    form_class = AlbumForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AlbumCreate, self).form_valid(form)

class SongCreate(CreateView):
    model = Song
    template_name = 'musicseaapp/form.html'
    form_class = SongForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(SongCreate, self).form_valid(form)



class GroupDelete(LoginRequiredMixin, CheckIsOwnerMixin, DeleteView):
    model = Group
    success_url = reverse_lazy('musicseaapp:groups_list')

class ArtistDelete(LoginRequiredMixin, CheckIsOwnerMixin, DeleteView):
    model = Artist
    success_url = reverse_lazy('musicseaapp:artists_list')

class AlbumDelete(LoginRequiredMixin, CheckIsOwnerMixin, DeleteView):
    model = Album
    success_url = reverse_lazy('musicseaapp:albums_list')

class SongDelete(LoginRequiredMixin, CheckIsOwnerMixin, DeleteView):
    model = Song
    success_url = reverse_lazy('musicseaapp:songs_list')