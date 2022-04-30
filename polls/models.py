from django.db import models
from datetime import timedelta as delta_t
from django.utils.timezone import now
from django.contrib import admin

# Create your models here.

class Question(models.Model):
	question_text = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')

	def __str__(self):
		return self.question_text

	def was_recently_published(self):
		this_time = now()
		return this_time-delta_t(days=1) <= self.pub_date <= this_time

	@admin.display(
		boolean=True,
		description="Published?" 
	)
	def is_published(self):
		return self.pub_date<=now()

class Choice(models.Model):
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	choice_text = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)

	def __str__(self):
		return self.choice_text
