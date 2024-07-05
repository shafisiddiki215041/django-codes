from django.shortcuts import render, redirect
from . import forms, models
# Create your views here.
def add_task(request):
    if request.method == 'POST':
        task = forms.TaskForm(request.POST)
        if task.is_valid():
            task.save()
            return redirect('show_task')
    else:
        task = forms.TaskForm()
    return render(request,'add_task.html',{'form':task})


def edit(request, id):
    edit = models.TaskModel.objects.get(pk=id)
    editNow= forms.TaskForm(instance=edit)
    
    # print(post.title)
    if request.method == 'POST':
        editNow= forms.TaskForm(request.POST,instance=edit)
        if editNow.is_valid():
            editNow.save()
            return redirect('show_task')
    return render(request,'add_task.html',{'form':editNow})

def delete(request, id):
    delete = models.TaskModel.objects.get(pk=id)
    delete.delete()
    return redirect('show_task')