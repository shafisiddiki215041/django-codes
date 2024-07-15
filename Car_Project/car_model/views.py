from django.shortcuts import render,redirect
from django.views.generic import ListView, DetailView, UpdateView
from .models  import CarModel, Buy
from .forms import CommentForm, CarForm,Buy_forms
from user.forms import ChangeUserForm
from django.urls import reverse_lazy
# Create your views here.
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator



class CarList(ListView):
    model =CarModel
    template_name = 'home.html'
    context_object_name = 'cars'
  
@login_required
def profile(request):
    purchases = Buy.objects.filter(user=request.user)
    return render(request, 'profile.html', {'purchases': purchases})
    
class details(DetailView):
    model = CarModel
    template_name = 'details.html'
    pk_url_kwarg ='id'
    context_object_name ='post'
    
    def post(self, request, *args, **kwargs):
        comment_form = CommentForm(data = self.request.POST)
        post = self.get_object()
        if comment_form.is_valid():
            new_comment = comment_form.save(commit = False)
            new_comment.car = post
            new_comment.save()
        return self.get(request, *args, **kwargs) 
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.object 
        comments = post.comments.all()
        comment_form = CommentForm()
        context['comments'] = comments
        context['comment_form'] = comment_form
        return context

# class profile_detail_edit(UpdateView):
#     model = User
#     form_class = RegistrationForm
#     template_name = 'profile_detail_edit.html'
#     pk_url_kwarg='id'
#     success_url = reverse_lazy('profile')
    
#     def form_valid(self, form):
#         messages.success(self.request, 'Logged in successfully')
#         return super().form_valid(form)

@login_required
def profile_detail_edit(request):
    if request.method == 'POST':
        profile_form= ChangeUserForm(request.POST, instance=request.user)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, 'Profile Updated Successfully')
            return redirect('profile')
    else:
        profile_form= ChangeUserForm(instance=request.user)
    return render(request,'profile_detail_edit.html',{'form':profile_form})   

@method_decorator(login_required,name='dispatch')
class show_buy_car(DetailView):
    model = CarModel
    template_name = 'profile.html'
    pk_url_kwarg ='id'
   
    def post(self, request, *args, **kwargs):
        print('enter')
        car = self.get_object()
        if car.quantity <= 0:
            messages.error(request, f"{car.car_name} is out of stock.")
            return redirect('profile')
        
        buy_car = Buy_forms(data =request.POST)
       
        if buy_car.is_valid():
            print('enter again')
            new_buy= buy_car.save(commit =False)
            new_buy.user = request.user
            new_buy.car = car
            new_buy.save()
            car.reduce_quantity()
            messages.success(request,'Purchased Successfully')
        print("Purchase successfully.")
        return self.get(request, *args, **kwargs) 
    
     
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # car = self.object
        context['purchases'] = Buy.objects.filter(user=self.request.user)
        return context

# def show_buy_car(request, id):
#     car= CarModel.objects.get(id = id)
#     Buy.objects.create(user=request.user, car=car)
    
# def show_buy_car(request, id):
#     car= CarModel.objects.get(pk =id)
#     print(f"Buying car: {car.id} for user: {request.user.id}")
#     if request.method =='POST':
#         print('enter')
#         buy_car= Buy(requst.POST,car=car)
#         buy_car.car=car
#         buy_car.save()
#         print("Purchase saved successfully.")
#         return redirect('profile')
    
#     purchases = Buy.objects.filter(user=request.user)
#     return render(request,'profile.html',{'purchases': purchases,'car':car})
    
     
    
    
    
    
    