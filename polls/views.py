from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from .models import Question as Q, Choice

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
	question = Q.objects.get(id=question_id)
	return render(request, "polls/results.html", {'question':question})

def vote(request, question_id):
	question = get_object_or_404(Q, id=question_id)
	try:
		choice = question.choice_set.get(id=request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		return render(request, "polls/detail.html", {
				'question':question,
				'error_msg':"You didn't make a choice!!!"
			})

	else:
		choice.votes += 1
		choice.save()
		return HttpResponseRedirect(reverse("results", args=[question.id,]))


"""
Class based views to achieve the same functionalities
"""

class HomeView(generic.ListView):
	template_name="polls/home.html"
	context_object_name='questions'

	def get_queryset(self):
		"""Return all Question objects"""
		return Q.objects.order_by("-pub_date")

class DetailView(generic.DetailView):
	model = Q
	context_object_name = 'question'
	template_name = "polls/detail.html"

class ResultsView(generic.DetailView):
	model = Q
	context_object_name = 'question'
	template_name = "polls/results.html"