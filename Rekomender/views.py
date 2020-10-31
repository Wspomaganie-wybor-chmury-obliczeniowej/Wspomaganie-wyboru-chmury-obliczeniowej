from django.shortcuts import render
from django.template import loader
from .models import Client, Cloud, Question, Choice, QuestionChoices
import json
# Create your views here.
def base(request):
    # latest_question_list = Question.objects
    # template = loader.get_template('Rekomender/base.html')
    # context = {
    #     'latest_question_list': latest_question_list,
    # }
    # return HttpResponse(template.render(context, request))

    #include multiple choise 
    x =  '{ "name":"John", "age":30, "city":"New York"}'
    #json_data2 = '{"question_text": "W jaki sposób chciałbyś się skontaktować z serwisantem/ pomocnikiem do konfiguracji?","date_added": "random","Choices": [{"text": "Telefonicznie",},{"type": "Email",}],"flag_if_multiple": "0"}'
    #json_data = json.loads("{'questions':[{'question_text': 'W jaki sposób chciałbyś się skontaktować z serwisantem/ pomocnikiem do konfiguracji?','date_added': 'random','Choices': [{'text': 'Telefonicznie',},{'type': 'Email',}],'flag_if_multiple': 0}]}")
    #json_data = json.loads(json_data2)
    #print(json_data["questions"])
    question_list = Question.objects.all()
    choices_list = Choice.objects.all()  
    context = {'latest_question_list': latest_question_list}
    return render(request, 'Rekomender/base.html', context)

# def ImportQuestionChoices():
#     QuestionChoices QC
#     json_data = {"questions":[{"question_text": "W jaki sposób chciałbyś się skontaktować z serwisantem/ pomocnikiem do konfiguracji?","date_added": "random","Choices": [{"text": "Telefonicznie",},{"type": "Email",}],"flag_if_multiple": 0}]}"
#     QC.info = json.loads(json_data)
#     QC.save()
#     print(json_data.question[0].question_text)
#{"questions":[{"question_text": "W jaki sposób chciałbyś się skontaktować z serwisantem/ pomocnikiem do konfiguracji?","date_added": "random","Choices": [{"text": "Telefonicznie",},{"type": "Email",}],"flag_if_multiple": 0}]}
def create(request):
    context = {}
    return render('Rekomender/create.html', context)

def answers(request):
    context = {}
    response = "You're looking at the results of question %s."
    return render('Rekomender/answers.html', context)

def questionnaire(request):
    context = {}
    return render('Rekomender/questionnaire.html', context)
