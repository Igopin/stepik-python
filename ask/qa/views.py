from django.http import HttpResponse 

def test(request):
    return HttpResponse('OK')

def login(request):
    return HttpResponse('LOGIN')

