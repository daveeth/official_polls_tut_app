from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponse
from .models import Question as Q

# Create your views here.

def homepage(request):
	questions = Q.objects.order_by("-pub_date")[:5]
	context = {'questions':questions}
	return render(request, "polls/home.html", context)

def detail(request, question_id):
	"""
		try:
			question = Q.objects.get(id=question_id)
		except Q.DoesNotExist:
			raise Http404("<h1>Question Not Found !!!</h1>")
	"""
	question = get_object_or_404(Q, id=question_id)
	return render(request, "polls/detail.html", {'question':question})

def results(request, question_id):
	return HttpResponse(f"<h2>You're looking at the results of {question_id}</h2>")

def vote(request, question_id):
	return HttpResponse(f"<h2>You're voting for the question {question_id}!</h2>")