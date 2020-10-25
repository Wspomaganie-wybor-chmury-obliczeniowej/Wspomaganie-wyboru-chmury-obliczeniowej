from django.forms import ModelForm

from .models import Question2


class CreateQuestion2(ModelForm):
    class Meta:
        model = Question2
        fields = ['question', 'answer1', 'answer1_AWS',
                  'answer1_Azure', 'answer1_City', 'answer1_Google',
                  'answer1_IBM', 'answer1_Krajowa', 'answer1_TASK', 'answer2', 'answer2_AWS',
                  'answer2_Azure', 'answer2_City', 'answer2_Google',
                  'answer2_IBM', 'answer2_Krajowa', 'answer2_TASK']
