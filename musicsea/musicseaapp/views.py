from django.shortcuts import render

from  django.core.urlresolvers import reverse
from  django.http import HttpResponseRedirect
from  django.shortcuts import get_object_or_404
from  django.views.generic import DetailView
from  django.views.generic.edit import CreateView
from  models import Group, Artist
from  forms import GroupForm, ArtistForm


class GroupDetail(DetailView):
    model = Group
    template_name = 'musicseaapp/group_detail.html'

    def get_context_data(self, **kwargs):
        context = super(GroupDetail, self).get_context_data(**kwargs)
        return context

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
        form.instance.group = Group.objects.get(id=self.kwargs['pk'])
        return super(ArtistCreate, self).form_valid(form)

