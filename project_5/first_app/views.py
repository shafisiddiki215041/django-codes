from django.shortcuts import render
from  . forms import contactForm, StudentData, PasswordMatching

def home(request):
    return render(request, 'home.html')


def about(request):
    if  request.method == 'POST':
        print(request.POST)
        name = request.POST.get('username') 
        email = request.POST.get('email')
        select = request.POST.get('select')
        return render(request, 'about.html',{'name':name,'email':email,'select':select})
    return render(request, 'about.html')

def submitform(request):
    
    return render(request, 'form.html')

def DjangoForm(request):
    if request.method == 'POST':
        form = contactForm(request.POST,request.FILES)
        if form.is_valid():
            # file = form.cleaned_data['file']
            # with open('./first_app/uploads/' + file.name, 'wb+') as destination:
            #     for chunk in file.chunks():
            #         destination.write(chunk)
            print(form.cleaned_data)
    else: 
        form =contactForm()    
    return render(request,'django_form.html',{'form':form})

def studentForm(request):
    if request.method == 'POST':
        form = StudentData(request.POST,request.FILES)
        if form.is_valid():
            print(form.cleaned_data)
            form  = StudentData()
    else: 
        form  = StudentData()
    return render(request,'django_form.html',{'form':form})

def PasswordValidation(request):
    if request.method == 'POST':
        form = PasswordMatching(request.POST,request.FILES)
        if form.is_valid():
            print(form.cleaned_data)
            form  = PasswordMatching()
    else: 
        form  = PasswordMatching()
    return render(request,'django_form.html',{'form':form})