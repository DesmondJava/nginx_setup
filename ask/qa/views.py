# coding=utf-8

from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_GET

from qa.forms import AskForm, AnswerForm, SignupForm
from qa.models import Question
from qa.utils.ajax import HttpResponseAjax, HttpResponseAjaxError, login_required_ajax
from qa.utils.viewhelpers import paginate


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


@login_required_ajax
def rating(request):
    if request.method == 'GET':
        if 1 == 1:
            question = get_object_or_404(Question, pk=1)
            question.rating += 1
            return HttpResponseAjax(comment_id="success")
        else:
            return HttpResponseAjaxError(
                code="bad_params",
                message="test",
            )


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


def user_logout(request):
    logout(request)
    return redirect('login')


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

