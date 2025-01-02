from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import loader
from .models import Question

# Create your views here.

def index(request):
    # latest_question_list = Question.objects.order_by("-pub_date")[:5]
    # output = "<br>".join([q.question_text for q in latest_question_list])
    # return HttpResponse(output)

    backend_list = Question.objects.order_by("-pub_date")[:5]
    template = loader.get_template("polls/index.html")
    context = {
        "frontend_list": backend_list,
    }
    return HttpResponse(template.render(context, request))


def test(request):
    return HttpResponse("<h1>Hello, You are in Polls test.</h1>")


def detail(request, question_id):
    # return HttpResponse("You're looking at question %s." % question_id)
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        # raise Http404("Question does not exist")
        return render(request, "polls/404.html")
    return render(request, "polls/detail.html", {"question": question})


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)