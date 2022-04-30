from django.urls import path
from .views import (homepage,detail,
	results,vote, HomeView, DetailView, ResultsView)


urlpatterns = [
	path('', homepage, name="home"),
	path('polls/', HomeView.as_view(), name="index"),
	path('polls/<int:pk>/', DetailView.as_view(), name="detail"),
	path('polls/<int:pk>/results/', ResultsView.as_view(), name="results"),
	path('polls/<int:question_id>/vote/', vote, name="vote"),
]