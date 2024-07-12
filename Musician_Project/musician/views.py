from django.shortcuts import render
from django.views.generic import CreateView,UpdateView,DeleteView,DetailView,ListView
from . import models, forms
from django.urls import reverse_lazy
from album.models import AlbumEntry
from album.forms import AlbumForm
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
# Create your views here.

@method_decorator(login_required,name='dispatch')
class AddMusician_create(CreateView):
    model = models.MusicianDetails
    form_class = forms.MusicianForm
    template_name ='add_musician.html'
    success_url = reverse_lazy('profile')

@method_decorator(login_required,name='dispatch')    
class edit_musician(UpdateView):
    model = models.MusicianDetails
    form_class = forms.MusicianForm
    template_name ='edit_musician.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('profile')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["type"] = 'Musician'
        return context
    
  
@method_decorator(login_required,name='dispatch')  
class edit_album(UpdateView):
    model = AlbumEntry
    form_class =AlbumForm
    template_name ='edit_musician.html'
    pk_url_kwarg ='id'
    success_url = reverse_lazy('profile')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["type"] = 'Album'
        return context
    

@method_decorator(login_required,name='dispatch')  
class delete(DeleteView):
    model = AlbumEntry
    template_name = 'delete.html'
    success_url = reverse_lazy('profile')
    pk_url_kwarg = 'id'