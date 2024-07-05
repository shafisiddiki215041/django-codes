from django.shortcuts import render, redirect
from TaskModel.models import TaskModel

def show_task(request):
    
    data = TaskModel.objects.all()
    return render(request,'show_task.html',{'task':data})


# def edit_post(request, id):
#     post = models.Post.objects.get(pk=id)
#     post_form= forms.PostForm(instance=post)
    
#     # print(post.title)
#     if request.method == 'POST':
#         post_form= forms.PostForm(request.POST,instance=post)
#         if post_form.is_valid():
#             post_form.save()
#             return redirect('homepage')
#     return render(request,'add_post.html',{'form':post_form})


def delete_post(request, id):
    post = models.Post.objects.get(pk =id)
    post.delete()
    return redirect('homepage')