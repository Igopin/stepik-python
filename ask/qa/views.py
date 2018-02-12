from django.http import HttpResponse 

def test(request):
    return HttpResponse('OK')

def login(request):
    return HttpResponse('LOGIN')

def question(request, question_id):
    return HttpResponse('Question #' + str(question_id))

