from django import forms
from .models import MusicianDetails


class MusicianForm(forms.ModelForm):
    class Meta:
        model = MusicianDetails
        fields ="__all__"
        