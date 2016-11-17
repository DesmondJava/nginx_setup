from django.core.paginator import Paginator, EmptyPage
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.decorators.http import require_GET


# Create your views here.
from qa.models import Question, Answer


@require_GET
def test(request, *args, **kwargs):
    return HttpResponse('OK')


@require_GET
def index(request):
    questions = Question.objects.new()
    try:
        limit = int(request.GET.get('limit', 10))
    except ValueError:
        limit = 10
    if limit > 100:
        limit = 0
    try:
        page = int(request.GET.get('page', 1))
    except ValueError:
        raise Http404
    paginator = Paginator(questions, limit)
    paginator.baseurl = '/?page='
    try:
        page = paginator.page(page)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)
    return render(request, 'questions.html', {
        'questions': page.object_list,
        'paginator': paginator,
        'page': page,
    })


@require_GET
def popular_page(request):
    questions = Question.objects.popular()
    try:
        limit = int(request.GET.get('limit', 10))
    except ValueError:
        limit = 10
    if limit > 100:
        limit = 0
    try:
        # page = int(page)
        page = int(request.GET.get('page', 1))
    except ValueError:
        raise Http404
    paginator = Paginator(questions, limit)
    paginator.baseurl = '/popular/?page='
    try:
        page = paginator.page(page)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)
    return render(request, 'questions.html', {
        'questions': page.object_list,
        'paginator': paginator,
        'page': page,
    })


    # limit = request.GET.get('limit', 10)
    # try:
    #     page = int(page)
    # except ValueError:
    #     page = 1
    # if page > 100:
    #     page = 1
    # paginator = Paginator(questions, limit)
    # paginator.baseurl = '/?page='
    # page = paginator.page(page)  # Page
    # return render(request, 'questions.html', {
    #     'questions': page.object_list,
    #     'paginator': paginator, 'page': page,
    # })




    # questions = Question.objects.popular()
    # limit = request.GET.get('limit', 10)
    # try:
    #     page = int(page)
    # except ValueError:
    #     page = 1
    # if page > 100:
    #     page = 1
    # paginator = Paginator(questions, limit)
    # paginator.baseurl = 'popular/?page='
    # page = paginator.page(page)  # Page
    # return render(request, 'questions.html', {
    #     'questions': page.object_list,
    #     'paginator': paginator, 'page': page,
    # })


@require_GET
def question(request, id):
    question = get_object_or_404(Question, pk=id)
    answers = question.answer_set.all()
    # answers = Answer.objects.filter(question=id)
    return render(request, 'question.html', {
        'question': question,
        'title': question.title,
        'text': question.text,
        'answers': answers.all()[:],
    })
