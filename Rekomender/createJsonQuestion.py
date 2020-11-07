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
                        '"amazon": "' + str(answer[1][1]) + '",' + \
                        '"microsoft":"' + str(answer[1][2]) + '",' + \
                        '"krajowa":"' + str(answer[1][3]) + '",' + \
                        '"ibm":"' + str(answer[1][4]) + '",' + \
                        '"city":"' + str(answer[1][5]) + '",' + \
                        '"task":"' + str(answer[1][6]) + '"}]}'
            first = False
        else:
            question += ',{"text": "' + answer[0] + '",' + \
                        '"weights": [{' + \
                        '"google":"' + str(answer[1][0]) + '",' + \
                        '"amazon":"' + str(answer[1][1]) + '",' + \
                        '"microsoft":"' + str(answer[1][2]) + '",' + \
                        '"krajowa":"' + str(answer[1][3]) + '",' + \
                        '"ibm":"' + str(answer[1][4]) + '",' + \
                        '"city":"' + str(answer[1][5]) + '",' + \
                        '"task":"' + str(answer[1][6]) + '"}]}'
    question += '],' \
                '"flag_if_multiple": "0"}' \
                ']' \
                '}'
    return question
