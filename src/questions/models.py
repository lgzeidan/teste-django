from django.db import models

# Create your models here.
class Title(models.Model):
	title = models.CharField(max_length=120)


class Question(models.Model):
	question = models.CharField(max_length=60)
	answer_1 = models.CharField(max_length=60)
	answer_2 = models.CharField(max_length=60)
	answer_3 = models.CharField(max_length=60, blank=True)
	answer_4 = models.CharField(max_length=60, blank=True)

class Result(models.Model):
	question_1 = models.CharField(max_length=60)
	question_2 = models.CharField(max_length=60)
	question_3 = models.CharField(max_length=60, blank=True)
	question_4 = models.CharField(max_length=60, blank=True)
	question_5 = models.CharField(max_length=60, blank=True)
	question_6 = models.CharField(max_length=60, blank=True)
	question_7 = models.CharField(max_length=60, blank=True)
	question_8 = models.CharField(max_length=60, blank=True)
	question_9 = models.CharField(max_length=60, blank=True)
	question_10 = models.CharField(max_length=60, blank=True)