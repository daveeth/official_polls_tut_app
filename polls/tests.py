from django.test import TestCase
from django.urls import reverse
from datetime import timedelta as t_d
from django.utils import timezone as tz
from polls.models import Question as Q


class QuestionModelTests(TestCase):
	def test_was_recently_published_in_the_future(self):
		"""
			Test for the was_recently_published() behavior for the model
			for questions posted in the future
			It should return False for questions published in the future
		"""
		time_published = tz.now() + t_d(seconds=1)
		future_question = Q("test question published in the future")
		future_question.pub_date = time_published
		self.assertIs(future_question.was_recently_published(), False)

	def test_was_recently_published_for_old_question(self):
		"""
			Test for the was_recently_published() behavior for the model 
			for old questions
			It should return False for questions published in the future
		"""
		time_published = tz.now() - t_d(days=1, seconds=1)
		future_question = Q("test question published in the future")
		future_question.pub_date = time_published
		self.assertIs(future_question.was_recently_published(), False)

	def test_was_recently_published_for_recent_questions(self):
		"""
			Test for the was_recently_published() behavior for the model 
			for recent questions
			It should return True for questions published in the future
		"""
		time_published = tz.now() - t_d(hours=23, minutes=59, seconds=59)
		future_question = Q("test question published in the future")
		future_question.pub_date = time_published
		self.assertIs(future_question.was_recently_published(), True)

def create_question(question_text, days):
	"""
	Create a question with the given `question_text` and published the
	given number of `days` offset to now (negative for questions published
	in the past, positive for questions that have yet to be published).
	"""
	return Q.objects.create(question_text=question_text, 
		pub_date = tz.now() + t_d(days) )

class QuestionHomeViewTests(TestCase):
	
	def test_no_questions(self):
		"""
		If no questions exist, an appropriate message is displayed.
		"""
		response = self.client.get(reverse('home'))
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, "No polls are available yet!!!")
		self.assertQuerysetEqual(response.context['questions'], [])

	def test_future_questions(self):
		create_question("Future Question", 3)
		response = self.client.get(reverse('home'))
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, "No polls are available yet!!!")
		self.assertQuerysetEqual(response.context['questions'], [])

	def test_past_questions(self):
		past_question = create_question("Past Question", -1)
		response = self.client.get(reverse('home'))
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, "Past Question")
		self.assertQuerysetEqual(response.context['questions'], [past_question])

	def test_future_and_past_questions(self):
		future_question = create_question("Future Question", 3)
		past_question = create_question("Past Question", -3)
		response = self.client.get(reverse('home'))
		self.assertEqual(Q.objects.count(), 2)
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, "Past Question")
		self.assertQuerysetEqual(response.context['questions'], [past_question])

	def test_multiple_past_questions(self):
		past_question_1 = create_question("Past Question 1", -1)
		past_question_2 = create_question("Past Question 2", -2)
		past_question_3 = create_question("Past Question 3", -3)
		question_count = Q.objects.count()
		response = self.client.get(reverse('home'))
		self.assertIs(question_count, 3)
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, "Past Question 1")
		self.assertQuerysetEqual(response.context['questions'], 
			[
				past_question_1, past_question_2, past_question_3
			])
	def test_multiple_future_questions(self):
		future_question_1 = create_question("Future Question 1", 1)
		future_question_2 = create_question("Future Question 2", 2)
		future_question_3 = create_question("Future Question 3", 3)
		question_count = Q.objects.count()
		response = self.client.get(reverse('home'))
		self.assertIs(question_count, 3)
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, "No polls")
		self.assertQuerysetEqual(response.context['questions'], [])