# coding=utf-8
from datetime import datetime, timedelta

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage
from django.http import Http404
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views.decorators.http import require_GET

# Create your views here.
from qa.forms import AskForm, AnswerForm, SignupForm
from qa.models import Question


def paginate(request, qs):
    try:
        limit = int(request.GET.get('limit', 10))
    except ValueError:
        limit = 10
    if limit > 100:
        limit = 10
    try:
        page = int(request.GET.get('page', 1))
    except ValueError:
        raise Http404
    paginator = Paginator(qs, limit)
    try:
        page = paginator.page(page)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)
    return paginator, page


@require_GET
def test(request, *args, **kwargs):
    return HttpResponse('OK')


@require_GET
def home(request):
    questions = Question.objects.new()
    paginator, page = paginate(request, questions)
    paginator.baseurl = '/?page='
    return render(request, 'home.html', {
        'questions': page.object_list,
        'paginator': paginator,
        'page': page,
    })


@require_GET
def popular(request):
    questions = Question.objects.popular()
    paginator, page = paginate(request, questions)
    paginator.baseurl = '/popular/?page='
    return render(request, 'home.html', {
        'questions': page.object_list,
        'paginator': paginator,
        'page': page,
    })


@login_required
def question_detail(request, id):
    if request.method == "POST":
        return HttpResponse('OK')
    question = get_object_or_404(Question, pk=id)
    answers = question.answer_set.all()
    form = AnswerForm(initial={'question': str(id)})
    return render(request, 'question_detail.html', {
        'question': question,
        'answers': answers,
        'form': form,
        # 'id_question': id
    })


@login_required
def ask(request):
    if request.method == "POST":
        form = AskForm(request.POST)
        if form.is_valid():
            form._user = request.user
            question = form.save()
            url = question.get_url()
            return HttpResponseRedirect(url)
    else:
        form = AskForm()
    return render(request, 'ask.html', {
        'form': form
    })


@login_required
def answer(request, id):
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            form._user = request.user
            answer = form.save()
            q_id = answer.question_id
            question = get_object_or_404(Question, pk=q_id)
            return HttpResponseRedirect(question.get_url())
        else:
            # form = AnswerForm()
            question = get_object_or_404(Question, pk=id)
            answers = question.answer_set.all()
            return render(request, 'question_detail.html', {
                'form': form,
                'question': question,
                'answers': answers,
            })


def user_signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})


# def user_login(request):
#     next = request.GET.get('next', "")
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             if user is not None:
#                 login(request, user)
#                 return HttpResponseRedirect('/' + next)
#     form = LoginForm()
#     return render(request, 'login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('login')
