from django import forms
from .models import Question

class QuestionForm(forms.Form):
	def __init__(self, *args, **kwargs):
	    super(QuestionForm, self).__init__(*args, **kwargs)
	    queryset = Question.objects.all()
	    i = 1
	    for instance in queryset:
	    	if not instance.answer_4:
	    		if not instance.answer_3:
	    			CHOICES = (('1', instance.answer_1), 
	    					   ('2', instance.answer_2))
	    		else:
	    			CHOICES = (('1', instance.answer_1), 
	    				       ('2', instance.answer_2), 
	    				       ('3', instance.answer_3))
	    	else:
	    		CHOICES = (('1', instance.answer_1), 
	    			       ('2', instance.answer_2), 
	    			       ('3', instance.answer_3), 
	    			       ('4', instance.answer_4))
	    	self.fields['question_%d'%i] = forms.ChoiceField(widget=forms.RadioSelect, choices = CHOICES, label = instance.question)
	    	i+=1