from django import forms
from .models import StudentModel

class StudentForm(forms.ModelForm):
    class Meta:
        model  = StudentModel
        fields = '__all__'
        labels = {
            'roll':"Student Roll",
            'name':"Student Name" 
        }
        widgets = {
            'name': forms.TextInput(),
        }
        
        help_texts = {
            'name': "Write your Full name..."
        }
        
        error_messages = {
            'name': {'required':'Your name is requires'}
        }