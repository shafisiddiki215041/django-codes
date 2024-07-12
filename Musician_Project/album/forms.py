from django import forms
from .models import AlbumEntry


class AlbumForm(forms.ModelForm):
    class Meta:
        model =AlbumEntry
        fields = '__all__'