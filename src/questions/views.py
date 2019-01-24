from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.staticfiles import finders

from .forms import QuestionForm
from .models import Question, Result, Title

# Create your views here.
def home_view(request):
	my_form = QuestionForm()
	questions = Question.objects.all()
	my_images = []
	for i in range(questions.count()): 
		if finders.find('question_' + str(i+1) + '.png'):  
			my_images.append('question_' + str(i+1) + '.png')
		elif finders.find('question_' + str(i+1) + '.jpg'):  
			my_images.append('question_' + str(i+1) + '.jpg')
		else:
			my_images.append('error.png')
	if request.method == "POST":
		my_form = QuestionForm(request.POST)
		if my_form.is_valid():
			Result.objects.create(**my_form.cleaned_data)
			my_form = QuestionForm()
	my_title = Title.objects.get(id=1)

	context = { 'form': my_form,
				'title': my_title.title,
				'images': my_images,
				}
	return render(request, "home.html", context)


def result_view(request):
	my_title = Title.objects.get(id=1)
	queryset = Result.objects.all()
	questions = Question.objects.all()
	m_question = []
	question = [[0, 0, 0, 0] for foo in range(10)]
	for instance in queryset:
		if instance.question_1:
			question[0][int(instance.question_1) - 1] += 1
		if instance.question_2:
			question[1][int(instance.question_2) - 1] += 1
		if instance.question_3:
			question[2][int(instance.question_3) - 1] += 1
		if instance.question_4:
			question[3][int(instance.question_4) - 1] += 1
		if instance.question_5:
			question[4][int(instance.question_5) - 1] += 1
		if instance.question_6:
			question[5][int(instance.question_6) - 1] += 1
		if instance.question_7:
			question[6][int(instance.question_7) - 1] += 1
		if instance.question_8:
			question[7][int(instance.question_8) - 1] += 1
		if instance.question_9:
			question[8][int(instance.question_9) - 1] += 1
		if instance.question_10:
			question[9][int(instance.question_10) - 1] += 1
	for i in range(9):
		if max(question[i]) != 0:
			m_question.append(question[i].index(max(question[i])) + 1)
	match_results = []
	for i in range(0, len(m_question)):
		if m_question[i] == 1:
			match_results.append(questions[i].answer_1)
		elif m_question[i] == 2:
			match_results.append(questions[i].answer_2)
		elif m_question[i] == 3:
			match_results.append(questions[i].answer_3)
		elif m_question[i] == 4:
			match_results.append(questions[i].answer_4)
	context = { 'result': match_results,
				'title': my_title.title,
				'question': questions,
				'count': queryset.count() }
	return render(request, "result.html", context)