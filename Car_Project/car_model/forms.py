from django import forms
from .models import CarModel, Comments, Buy

class CarForm(forms.ModelForm):
    class Meta:
        model = CarModel
        fields = '__all__'
        

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['name','email','body']
        
        
class Buy_forms(forms.ModelForm):
    class Meta:
        model = Buy
        fields = []
        
    