import json


def createQuestion(question, answers):
    question = '{ "question":[' \
               '{' \
               ' "questiontext": "' + question + \
               '", "date_added": "random",' \
               '"Choices": ['
    first = True
    for answer in answers:
        if first:
            question += '{"text": "' + answer[0] + '",' + \
                        '"weights": [{' + \
                        '"google": "' + str(answer[1][0]) + '",' + \
                        '"desgoogle": "' + str(answer[2][0]) + '",' + \
                        '"amazon": "' + str(answer[1][1]) + '",' + \
                        '"desamazon": "' + str(answer[2][1]) + '",' + \
                        '"microsoft":"' + str(answer[1][2]) + '",' + \
                        '"desmicrosoft": "' + str(answer[2][2]) + '",' + \
                        '"krajowa":"' + str(answer[1][3]) + '",' + \
                        '"deskrajowa": "' + str(answer[2][3]) + '",' + \
                        '"ibm":"' + str(answer[1][4]) + '",' + \
                        '"desibm": "' + str(answer[2][4]) + '",' + \
                        '"city":"' + str(answer[1][5]) + '",' + \
                        '"descity": "' + str(answer[2][5]) + '",' + \
                        '"task":"' + str(answer[1][6])  + '",' + \
                        '"destask": "' + str(answer[2][6]) + '"}]}'
            first = False
        else:
            question += ',{"text": "' + answer[0] + '",' + \
                        '"weights": [{' + \
                        '"google": "' + str(answer[1][0]) + '",' + \
                        '"desgoogle": "' + str(answer[2][0]) + '",' + \
                        '"amazon": "' + str(answer[1][1]) + '",' + \
                        '"desamazon": "' + str(answer[2][1]) + '",' + \
                        '"microsoft":"' + str(answer[1][2]) + '",' + \
                        '"desmicrosoft": "' + str(answer[2][2]) + '",' + \
                        '"krajowa":"' + str(answer[1][3]) + '",' + \
                        '"deskrajowa": "' + str(answer[2][3]) + '",' + \
                        '"ibm":"' + str(answer[1][4]) + '",' + \
                        '"desibm": "' + str(answer[2][4]) + '",' + \
                        '"city":"' + str(answer[1][5]) + '",' + \
                        '"descity": "' + str(answer[2][5]) + '",' + \
                        '"task":"' + str(answer[1][6])  + '",' + \
                        '"destask": "' + str(answer[2][6]) + '"}]}'
    question += '],' \
                '"flag_if_multiple": "0"}' \
                ']' \
                '}'
    return question