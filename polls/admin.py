from django.contrib import admin
from .models import Question, Choice

# Register your models here.

class ChoiceInline(admin.TabularInline):
	model = Choice
	extra = 3

class QuestionAdmin(admin.ModelAdmin):
	fields = ['pub_date', 'question_text',]
	inlines = [ChoiceInline,]
	list_display=['question_text', 'pub_date', 'is_published']
	search_fields=['question_text', 'pub_date']


admin.site.register(Question, QuestionAdmin)

