from django.http import HttpResponse


def Home(request):
    return HttpResponse('This is homepage')
    
def contact(request):
    return HttpResponse('This is contact page')