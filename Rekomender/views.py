from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse
from .models import Client, Cloud, Question, Choice, QuestionChoices, user
from .createJsonQuestion import createQuestion
from django.core.paginator import Paginator
import json

# Create your views here.
def base(request):
    context = {
    }
    return render(request, 'Rekomender/home.html', context)

def home(request):
    context = {
    }
    return render(request, 'Rekomender/home.html', context)

# def ImportQuestionChoices():
#     QuestionChoices QC
#     json_data = {"questions":[{"question_text": "W jaki sposób chciałbyś się skontaktować z serwisantem/ pomocnikiem do konfiguracji?","date_added": "random","Choices": [{"text": "Telefonicznie",},{"type": "Email",}],"flag_if_multiple": 0}]}"
#     QC.info = json.loads(json_data)
#     QC.save()
#     print(json_data.question[0].question_text)
#{"questions":[{"question_text": "W jaki sposób chciałbyś się skontaktować z serwisantem/ pomocnikiem do konfiguracji?","date_added": "random","Choices": [{"text": "Telefonicznie",},{"type": "Email",}],"flag_if_multiple": 0}]}
def create(request):
    if request.method == 'POST':
        question = request.POST.get('question')
        answers = []
        for i in range(1,6): 
            answer = []
            weights = []
            description = []
            answer.append(request.POST.get('option' + str(i)))
            description.append(request.POST.get('descriptiongoogle' + str(i)))
            description.append(request.POST.get('descriptionamazon' + str(i)))
            description.append(request.POST.get('descriptionmicrosoft' + str(i)))
            description.append(request.POST.get('descriptionkrajowa' + str(i)))
            description.append(request.POST.get('descriptionibm' + str(i)))
            description.append(request.POST.get('descriptioncity' + str(i)))
            description.append(request.POST.get('descriptiontask' + str(i)))
            weights.append(request.POST.get('google' + str(i)))
            weights.append(request.POST.get('amazon' + str(i)))
            weights.append(request.POST.get('microsoft' + str(i)))
            weights.append(request.POST.get('krajowa' + str(i)))
            weights.append(request.POST.get('ibm' + str(i)))
            weights.append(request.POST.get('city' + str(i)))
            weights.append(request.POST.get('task' + str(i)))       
            answer.append(weights)
            answer.append(description)
            answers.append(answer)
        for answer in answers:
            if answer[0] == "":
                answers.remove(answer)
        for answer in answers:
            if answer[0] == "":
                answers.remove(answer) #robione dwa reazy dla pewności, jedno przejście nie usuwa ostatniego
        sample = QuestionChoices()
        
        print(answers)
        sample.info = createQuestion(question,answers)
        print('create complete')
        sample.save()
    context = {}
    return render(request,'Rekomender/create.html', context)

def answers(request):
    context = {}
    response = "You're looking at the results of question %s."
    return render( 'Rekomender/answers.html', context)

def questionnaire(request, question_id):
    try:
        request.session['amazon']
    except:
        request.session['amazon'] = 0
        request.session['microsoft'] = 0
        request.session['google'] = 0
        request.session['krajowa'] = 0
        request.session['ibm'] = 0
        request.session['city'] = 0
        request.session['task'] = 0
        
        request.session['selectedChoices'] = ""
        # request.session['microsoft_des'] = ""
        # request.session['google_des'] = ""
        # request.session['krajowa_des'] = ""
        # request.session['ibm_des'] = ""
        # request.session['city_des'] = ""
        # request.session['task_des'] = ""
    print(request.session['amazon'])
    print(request.session['selectedChoices'])
    #print(request.session['amazon_des'])
    print(request.session['microsoft'])
    #print(request.session['microsoft_des'])
    print(request.session['google'])
    print(request.session['krajowa'])
    print(request.session['ibm'])
    print(request.session['city'])
    print(request.session['task'])
    list_object = []
    json_data_from_db = QuestionChoices.objects.all()
    for item in json_data_from_db:
        list_object.append(item.info)
    json_data = json.loads(list_object[int(question_id)])
    if request.method == "POST":
        next_question_id = 0
        answer = request.POST.get('question')
        for choice in json_data['question'][0]['Choices']:
            if choice['text'] == answer:
                request.session['amazon'] += int(choice['weights'][0]['amazon'])
                request.session['microsoft'] += int(choice['weights'][0]['microsoft'])
                request.session['google'] += int(choice['weights'][0]['google'])
                request.session['krajowa'] += int(choice['weights'][0]['krajowa'])
                request.session['ibm'] += int(choice['weights'][0]['ibm'])
                request.session['city'] += int(choice['weights'][0]['city'])
                request.session['task'] += int(choice['weights'][0]['task'])

                request.session['selectedChoices'] += choice['text'] + "##"
                # request.session['microsoft_des'] += choice['weights'][0]['desmicrosoft']
                # request.session['google_des'] += choice['weights'][0]['desgoogle']
                # request.session['krajowa_des'] += choice['weights'][0]['deskrajowa']
                # request.session['ibm_des'] += choice['weights'][0]['desibm']
                # request.session['city_des'] += choice['weights'][0]['descity']
                # request.session['task_des'] += choice['weights'][0]['destask']
        if 'next' in request.POST:
            next_question_id = int(question_id)+1
            if next_question_id >= len(list_object):
                next_question_id = len(list_object)-1
        elif 'previous' in request.POST:
            next_question_id = int(question_id)-1
            if next_question_id <0:
                next_question_id = 0
        return redirect('questionnaire', next_question_id)
    context = {
        'json_data': json_data["question"],
        'question_id': int(question_id)
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