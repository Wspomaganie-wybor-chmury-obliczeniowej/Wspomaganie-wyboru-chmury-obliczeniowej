from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse
from .models import Client, Cloud, Question, Choice, QuestionChoices, user
from .createJsonQuestion import createQuestion
import json


def base(request):
    context = {
    }
    return render(request, 'Rekomender/home.html', context)


def home(request):
    context = {
    }
    return render(request, 'Rekomender/home.html', context)


def create(request):
    if request.method == 'POST':
        question = request.POST.get('question')
        answers = []
        for i in range(1, 6):
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
            if answer[0] is None:
                answers.remove(answer)
        for answer in answers:
            if answer[0] == "":
                answers.remove(answer)
        for answer in answers:
            if answer[0] == "":
                answers.remove(answer)  # robione dwa reazy dla pewności, jedno przejście nie usuwa ostatniego
        sample = QuestionChoices()

        sample.info = createQuestion(question, answers)
        sample.save()
    context = {}
    return render(request, 'Rekomender/create.html', context)


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
    try:
        request.session['selectedChoices']
    except:
        request.session['selectedChoices'] = ""
    print('Amazon: ', request.session['amazon'])
    print('microsoft: ',request.session['microsoft'])
    print('google: ',request.session['google'])
    print('krajowa: ',request.session['krajowa'])
    print('ibm: ',request.session['ibm'])
    print('city: ',request.session['city'])
    print('task: ',request.session['task'])
    print(request.session['selectedChoices'])
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
        if 'next' in request.POST:
            next_question_id = int(question_id) + 1
            if next_question_id >= len(list_object):
                return redirect('answers')
        elif 'previous' in request.POST:
            next_question_id = int(question_id) - 1
            if next_question_id < 0:
                next_question_id = 0
        return redirect('questionnaire', next_question_id)
    context = {
        'json_data': json_data["question"],
        'question_id': int(question_id)
    }
    return render(request, 'Rekomender/questionnaire.html', context)


def answers(request):
    winners = []
    winners.append(int(request.session['amazon']))
    winners.append(int(request.session['microsoft']))
    winners.append(int(request.session['google']))
    winners.append(int(request.session['krajowa']))
    winners.append(int(request.session['ibm']))
    winners.append(int(request.session['city']))
    winners.append(int(request.session['task']))
    winnerTemp = max(winners)
    winner = ""
    for i in range(0,len(winners)):
        if winners[i] == winnerTemp:
            winnerTemp = i
            break
    if winnerTemp == 0:
        winner = 'amazon'
    elif winnerTemp == 1:
        winner = 'microsoft'
    elif winnerTemp == 2:
        winner = 'google'
    elif winnerTemp == 3:
        winner = 'krajowa'
    elif winnerTemp == 4:
        winner = 'ibm'
    elif winnerTemp == 5:
        winner = 'city'
    elif winnerTemp == 6:
        winner = 'task'
    answers = request.session['selectedChoices']
    answers = answers.split('##')
    del answers[-1]  # usuwamy ostatni bo zawsze jest to pusty element
    list_object = []
    json_data_from_db = QuestionChoices.objects.all()
    for item in json_data_from_db:
        list_object.append(item.info)
    counter = 0
    to_print = []
    for question in list_object:
        temp = json.loads(question)
        for choice in temp['question'][0]['Choices']:
            if choice['text'] == answers[counter]:
                temp = [temp['question'][0]['questiontext'], answers[counter], choice['weights'][0]['des' + winner]]
                to_print.append(temp)
    context = {
        'winner': winner,
        'to_print': to_print
    }
    request.session['amazon'] = 0
    request.session['microsoft'] = 0
    request.session['google'] = 0
    request.session['krajowa'] = 0
    request.session['ibm'] = 0
    request.session['city'] = 0
    request.session['task'] = 0
    request.session['selectedChoices'] = ""
    return render(request, 'Rekomender/answers.html', context)
