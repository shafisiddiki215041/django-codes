from django import forms
from . models import Task_Category

class Task_cat_Form(forms.ModelForm):
    class Meta:
        model = Task_Category
        fields = '__all__'
        