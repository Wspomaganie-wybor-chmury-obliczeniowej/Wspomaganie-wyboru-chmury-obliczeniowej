from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import Client, Cloud, Question, Choice, QuestionChoices
from django.core.paginator import Paginator
import json
# Create your views here.
def base(request):
    #include multiple choise 
    html = "<html><body>It is now </body></html>"
    json_data2 = '{ "question": [{"questiontext":"W jaki sposób chciałbyś się skontaktować z serwisantem pomocnikiem do konfiguracji?","date_added":"random","Choices":[{"text":"Telefonicznie"},{"text":"Email"}],"flagifmultiple":"0"},{"questiontext":"Jak bardzo zależy ci na szybkiej odpowiedzi serwisanta?","date_added":"random","Choices":[{"text":"Dont Care"},{"text":"Expresowo"}],"flagifmultiple":"0"} ]}'
    json_data = json.loads(json_data2)

    questionList = []
    ChoicesList = []

    # for elem in range(0,len(json_data["question"])):
    #     questionList.append(json_data["question"][elem]["questiontext"])
    #     ChoicesList.append(json_data["question"][elem]["Choices"])
    #     for text in json_data["question"][elem]["Choices"]:
    #         print(text["text"])
    #     print("stwrozyc graficzne pytanie")  
    #print ([item["text"] for innerlist in ChoicesList for item in innerlist])

    # for item in questionList:
    #     #print([item["text"] for item in questionList[item]["Choices"]])
    #     print ([item["text"] for innerlist in ChoicesList for item in innerlist])
    
    # template = loader.get_template('Rekomender/base.html')
    # context = {
    #     'latest_question_list': latest_question_list,
    # }
    # return HttpResponse(template.render(context, request))

    #return render(request, 'Rekomender/base.html', context)
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
    context = {}
    return render('Rekomender/create.html', context)

def answers(request):
    context = {}
    response = "You're looking at the results of question %s."
    return render('Rekomender/answers.html', context)

def questionnaire(request):
   

    list_object = []
    json_data_from_db = QuestionChoices.objects.all() 
    for item in json_data_from_db:
        list_object.append(item.info)
    data = list_object[0]
    json_data = json.loads(data)

    page = request.GET.get('page', 1)
    paginator = Paginator(json_data["question"], 1)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    # users = paginator.page(paginator.num_pages)
    
    #page_obj = paginator.get_page(page_number)
    context = {
        'json_data' : json_data["question"]
    }

    return render(request,'Rekomender/questionnaire.html',context)



#     {% if latest_question_list %}
#     <ul>
#     {% for question in latest_question_list %}
#         <li><a href="/polls/{{ question.id }}/">{{ question.question_text }}</a></li>
#     {% endfor %}
#     </ul>
# {% else %}
#     <p>No polls are available.</p>
# {% endif %}
