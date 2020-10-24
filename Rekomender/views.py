from django.shortcuts import render

# Create your views here.
def base(request):
    context = {}
    return render('Rekomender/base.html', context)

def create(request):
    context = {}
    return render('Rekomender/create.html', context)

def answers(request):
    context = {}
    return render('Rekomender/answers.html', context)

def questionnaire(request):
    context = {}
    return render('Rekomender/questionnaire.html', context)