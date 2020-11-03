from django.shortcuts import render,get_object_or_404
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from .models import Client, Cloud, Question, Choice, QuestionChoices
from django.core.paginator import Paginator
from .createJsonQuestion import createQuestion
from django.urls import reverse
import json
# Create your views here.
def base(request):
    #include multiple choise 
    html = "<html><body>It is now </body></html>"
    json_data2 = '{ "question": [{"questiontext":"W jaki sposób chciałbyś się skontaktować z serwisantem pomocnikiem do konfiguracji?","date_added":"random","Choices":[{"text":"Telefonicznie"},{"text":"Email"}],"flagifmultiple":"0"},{"questiontext":"Jak bardzo zależy ci na szybkiej odpowiedzi serwisanta?","date_added":"random","Choices":[{"text":"Dont Care"},{"text":"Expresowo"}],"flagifmultiple":"0"} ]}'
    json_data = json.loads(json_data2)

    questionList = []
    ChoicesList = []
    return HttpResponse(html)

def home(request):
    json_data2 = '{ "question": [{"questiontext":"W jaki sposób chciałbyś się skontaktować z serwisantem pomocnikiem do konfiguracji?","date_added":"random","Choices":[{"text":"Telefonicznie"},{"text":"Email"}],"flagifmultiple":"0"},{"questiontext":"Jak bardzo zależy ci na szybkiej odpowiedzi serwisanta?","date_added":"random","Choices":[{"text":"Dont Care"},{"text":"Expresowo"}],"flagifmultiple":"0"} ]}'
    json_data = json.loads(json_data2)
   
    #QuestionChoices.objects.all().delete() do usuwania wszystkich elementow !%!
    #zapis do bazy danych 
    #sample = QuestionChoices()
    #sample.info = json_data2
    #sample.save()
    
    list_object = []
    json_data_from_db = QuestionChoices.objects.all() 
    for item in json_data_from_db:
        list_object.append(item.info)
    data = list_object[0]
    json_data = json.loads(data)

    context = {
        'json_data' : json_data["question"]
    }
    # for questionList in json_data["question"]:
    #     print(questionList)
    #     for choice in questionList["Choices"]:
    #         print(choice)
    return render(request, 'Rekomender/home.html', context)

def create(request):
    if request.method == 'POST':
        question = request.POST.get('question')
        answers = []
        answers.append(request.POST.get('option1'))
        answers.append(request.POST.get('option2'))
        answers.append(request.POST.get('option3'))
        answers.append(request.POST.get('option4'))
        answers.append(request.POST.get('option5'))
        while("" in answers):
            answers.remove("")
        sample = QuestionChoices()
        sample.info = createQuestion(question,answers)
        sample.save()
    context = {}
    return render(request,'Rekomender/create.html', context)

def answers(request,question_id):
    list_object = []
    json_data_from_db = QuestionChoices.objects.all()
    for item in json_data_from_db:
        list_object.append(item.info)
    json_data = json.loads(list_object[int(question_id)])
    context = {
                'json_data': json_data["question"],
                'question_id': question_id
            }
    return render(request, 'Rekomender/answers.html', context)

def questionnaire(request,question_id):
   

    # list_object = []
    # json_data_from_db = QuestionChoices.objects.all() 
    # for item in json_data_from_db:
    #     list_object.append(item.info)
    # data = list_object[0]
    # json_data = json.loads(data)

    # page = request.GET.get('page', 1)
    # paginator = Paginator(json_data["question"], 1)

    # page_number = request.GET.get('page')
    # page_obj = paginator.get_page(page_number)
    # # users = paginator.page(paginator.num_pages)
    
    # #page_obj = paginator.get_page(page_number)
    # context = {
    #     'json_data' : json_data["question"]
    # }

    # return render(request,'Rekomender/questionnaire.html',context)
    list_object = []
    json_data_from_db = QuestionChoices.objects.all()
    for item in json_data_from_db:
        list_object.append(item.info)
    json_data = json.loads(list_object[int(question_id)])
    if request.method == "POST":
        next_question_id = 0
        if 'next' in request.POST:
            next_question_id = int(question_id)+1
            if next_question_id >= len(list_object):
                next_question_id = len(list_object)-1
            context = {
                'json_data': json_data["question"],
                'question_id': next_question_id
            }
        elif 'previous' in request.POST:
            next_question_id = int(question_id)-1
            if next_question_id <0:
                next_question_id = 0
            context = {
                'json_data': json_data["question"],
                'question_id': next_question_id
            }
        return render('questionnaire', next_question_id)
    #paginator = Paginator(json_data["question"], 1)

    #page_number = request.GET.get('page')
    #page_obj = paginator.get_page(page_number)
    # users = paginator.page(paginator.num_pages)
    
    #page_obj = paginator.get_page(page_number)
    context = {
        'json_data': json_data["question"],
        'question_id': question_id
    }

    return render(request,'Rekomender/questionnaire.html',context)

def vote(request, question_id):
    list_object = []
    json_data_from_db = QuestionChoices.objects.all()
    for item in json_data_from_db:
        list_object.append(item.info)
    json_data = json.loads(list_object[int(question_id)])
    
    try:
        selected_choice = json_data.get(pk=request.POST['choice'])
        print(selected_choice)
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'Rekomender/questionnaire.html', {
            'question': json_data["question"],
            'question_id': question_id,
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('Rekomender:answers', args=(question_id,)))