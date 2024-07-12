from django.shortcuts import render
from django.views.generic import CreateView,UpdateView,DeleteView
from . import models, forms
from django.urls import reverse_lazy
# Create your views here.


class AlbumCreate(CreateView):
    model = models.AlbumEntry
    form_class = forms.AlbumForm
    template_name = 'add_album.html'
    success_url = reverse_lazy('profile')
