from django.shortcuts import render,redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from album.models import AlbumEntry
from django.views.generic import ListView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

def home(request):
    albums = AlbumEntry.objects.all()
    return render(request,'home.html',{'albums':albums})

# def profile(request):
#     album = AlbumEntry.objects.all()
#     return render(request,'profile.html',{'albums':album})

@method_decorator(login_required,name='dispatch')
class MusicianListView(ListView):
    model = AlbumEntry
    template_name = 'profile.html'
    context_object_name = 'albums'


class LoginViewOn(LoginView):
    template_name = 'login.html'
    
    def get_success_url(self):
        return reverse_lazy('profile')
    def form_valid(self, form):
        messages.success(self.request, 'Logged in successfully')
        return super().form_valid(form)
    def form_invalid(self, form):
        messages.success(self.request, 'Logged in information incorrect')
        return super().form_invalid(form)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["type"] = 'Login'
        return context
    
class UserLogOut(LogoutView):
    def form_valid(self, form):
        messages.success(self.request, 'Logged out successfully')
        return super().form_valid(form)
    def get_success_url(self):
        return reverse_lazy('login')