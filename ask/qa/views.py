from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.views.decorators.http import require_GET

from qa.models import *
from qa.forms import *

def questions_view(request, questions):
    page = request.GET.get('page', 1)
    paginator = Paginator(questions, 10)
    paginator.baseurl = request.path + '?page='
    page = paginator.page(page)
    return render(request, 'questions.html', {
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

def show_question(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    answers = Answer.objects.filter(question=question)
    
    if request.method == "GET":
        form = AnswerForm(question=question)
    elif request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save()
            print(answer)
            url = question.get_url()
            return HttpResponseRedirect(url)
    else:
        raise Http404

    return render(request, 'question.html', {
        'question': question,
        'answers': answers,
        'form': form
    })


def question_add(request):
    if request.method == "POST":
        form = AskForm(request.POST)
        if form.is_valid():
            question = form.save()
            url = question.get_url()
            return HttpResponseRedirect(url)
    elif request.method == "GET":
        form = AskForm()
    else:
        raise Http404

    return render(request, 'forms/question_add.html', {
        'form': form
    })


def test(request):
    return HttpResponse('OK')

def login(request):
    return HttpResponse('LOGIN')


