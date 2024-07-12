from django.shortcuts import render
from datetime import datetime, timedelta
from django.http import HttpResponse

# Create your views here.
def home(request):
    response =  render(request,'home.html')
    response.set_cookie('name','rahim')
    # response.set_cookie('name','karim', max_age=10)
    response.set_cookie('name','karim', expires=datetime.utcnow()+timedelta(days=7))
    return response

def get_cookie(request):
    name = request.COOKIES.get('name')
    print(name)
    return render(request,'get_cookies.html',{'name':name})

def delete_cookie(request):
    respond = render(request,'delete.html')
    respond.delete_cookie('name')
    return respond
     
def set_session(request):
    # data ={
    #     'name':'rahim',
    #     'age':'23',
    #     'language':'Bangla',
    # }
    # print(request.session.get_session_cookie_age())
    # print(request.session.get_expiry_date())
    # request.session.update(data)
    request.session['name']='karim'
    return render(request,'home.html')


def get_session(request):
    if 'name' in request.session:
         name = request.session.get('name','Guest')
         request.session.modified =True
         return render(request,'get_session.html',{'name': name})
    else:
        return HttpResponse('Your sesssin has been expired. Log in again....')
    # age = request.session.get('age')
    # print(name)
    # #,'age': age
    
    
def delete_session(reqeust):
    # del reqeust.session['name']
    reqeust.session.flush()
    # reqeust.session.clear_expired()
    return render(reqeust,'delete.html')