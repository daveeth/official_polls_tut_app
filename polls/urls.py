from django.urls import path
from .views import homepage,detail,results,vote

urlpatterns = [
	path('', homepage, name="home"),
	path('polls/', homepage, name="home"),
	path('polls/<int:question_id>', detail, name="detail"),
	path('polls/<int:question_id>/results/', results, name="results"),
	path('polls/<int:question_id>/vote/', vote, name="vote"),
]