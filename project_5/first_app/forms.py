from django import forms
from django.core import validators
#widget = field to html index...

class contactForm(forms.Form):
    name = forms.CharField(label='Full Name: ', initial="Shafi", help_text="Maximum width 70 character", required=False, widget=forms.Textarea(attrs={"id":'text_area','class':'class1 class2', 'placeholder':'Enter Your name..'}))
    # file = forms.FileField()
    email = forms.EmailField(label='UserEmail')
    # weight = forms.FloatField()
    # balance = forms.DecimalField()
    age = forms.CharField(widget=forms.NumberInput)
    check = forms.BooleanField()
    birtday = forms.CharField(widget=forms.DateInput(attrs={'type':'date'}))
    appointment = forms.CharField(widget=forms.DateInput(attrs={'type':'datetime-local'}))
    CHOICES = [('S','Small'),('M','Medium'),('L','Large')]
    size = forms.CharField( widget=forms.RadioSelect(choices=CHOICES))
    meals = [('P','pepporoni'),('M','Mashroom'),('B','Beef')]
    pizza = forms.MultipleChoiceField(choices=meals, widget=forms.CheckboxSelectMultiple)
    
    
# class StudentData(forms.Form):
        # name = forms.CharField(widget=forms.TextInput)
        # email = forms.CharField(widget=forms.EmailInput)
        # age = forms.CharField()
        # def clean_name(self):
        #     valname = self.cleaned_data["name"]
        #     if len(valname) < 10:
        #          raise forms.ValidationError("Enter a name at leaset 10 character")
        #     return valname
            
        # def clean_email(self):
        #     vemail = self.cleaned_data['email']
            
        #     if '.com' not in vemail:
        #         raise forms.ValidationError('Your Email must contain .com')
        #     return vemail
        # def clean(self):
        #     cleaned_data = super().clean()
        #     vname = self.cleaned_data['name']
        #     vemail = self.cleaned_data['email']
        #     if len(vname) < 10:
        #          raise forms.ValidationError('Enter a name at least 10 character')
        #     if '.com' not in vemail:
        #         raise forms.ValidationError('Your Email must contain .com')


def len_check(value):
    if len(value)<10:
        raise forms.ValidationError("Enter a name at least 10 character")
    
class StudentData(forms.Form):
        name = forms.CharField(validators=[validators.MinLengthValidator(10,message="Enter a name at least 10 character")])
        text = forms.CharField(widget=forms.TextInput, validators= [len_check])
        email = forms.CharField(widget=forms.EmailInput)
        age = forms.IntegerField(validators=[validators.MaxValueValidator(34,message="must be 34 and down"),validators.MinValueValidator(24,message="must be 24 and above")])
        file = forms.FileField(validators=[validators.FileExtensionValidator(allowed_extensions=['pdf'],message='File extension must be ended with .pdf')])
        
        
class PasswordMatching(forms.Form):
    name = forms.CharField(widget=forms.TextInput)
    password = forms.CharField(widget=forms.PasswordInput)
    Confirm_password = forms.CharField(widget=forms.PasswordInput)
    
    def clean(self):
        cleaned_data = super().clean()
        val_pass = self.cleaned_data['password']
        val_conpass = self.cleaned_data['Confirm_password']
        val_name = self.cleaned_data['name']
        if val_pass != val_conpass:
            raise forms.ValidationError("Password Doesn't match")
        if len(val_name)<15:
            raise forms.ValidationError('character must be 15 character')