from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.views.decorators.http import require_GET
from django.contrib.auth import login

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
        form = AnswerForm()
    elif request.method == "POST":
        form = AnswerForm(request.POST)
        form._user = request.user
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(form.get_question_url())
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
        form._user = request.user
        if form.is_valid():
            question = form.save()
            return HttpResponseRedirect(question.get_url())
    elif request.method == "GET":
        form = AskForm()
    else:
        raise Http404

    return render(request, 'forms/question_add.html', {
        'form': form
    })


def user_login(request):
    if request.method == "GET":
        form = LoginForm()
    elif request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return HttpResponseRedirect('/')
    else:
        raise Http404

    return render(request, 'forms/login.html', {
        'form': form
    })

def user_signup(request):
    if request.method == "GET":
        form = SignUpForm()
    elif request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return HttpResponseRedirect('/')
    else:
        raise Http404

    return render(request, 'forms/sign_up.html', {
        'form': form
    })
