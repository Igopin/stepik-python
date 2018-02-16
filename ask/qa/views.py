from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.views.decorators.http import require_GET

from qa.models import *

def questions_view(request, questions):
    page = request.GET.get('page', 1)
    paginator = Paginator(questions, 10)
    paginator.baseurl = request.path + '?page='
    page = paginator.page(page)
    return render(request, 'new_questions.html', {
        'questions': page.object_list,
        'paginator': paginator,
        'page': page
    })

@require_GET
def questions_new(request):
    questions = Question.objects.new()
    return questions_view(request, questions)

@require_GET
def questions_popular(request):
    questions = Question.objects.popular()
    return questions_view(request, questions)

@require_GET
def show_question(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    answers = Answer.objects.filter(question=question)

    return render(request, 'question.html', {
        'question': question,
        'answers': answers
    }) 

def test(request):
    return HttpResponse('OK')

def login(request):
    return HttpResponse('LOGIN')


