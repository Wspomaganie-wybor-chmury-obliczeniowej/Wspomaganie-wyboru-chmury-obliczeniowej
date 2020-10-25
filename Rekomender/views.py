from django.shortcuts import render, redirect
from .createQuestions import CreateQuestion2
from .models import Question2
# Create your views here.
def home(request):
    context = {}
    return render(request, 'Rekomender/home.html', context)

def create2(request):
    if request.method == 'POST':
        question = CreateQuestion2(request.POST)
        if question.is_valid():
            question.save()
            return redirect('home')
    else:
        question = CreateQuestion2()
    context = {'question': question}
    return render(request, 'Rekomender/create2.html', context)

def answers(request):
    context = {}
    return render(request, 'Rekomender/answers.html', context)

def questionnaire(request):
    context = {}
    return render(request, 'Rekomender/questionnaire.html', context)