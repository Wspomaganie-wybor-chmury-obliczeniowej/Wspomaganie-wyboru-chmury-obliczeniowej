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
            question += '{"text": "' + answer + '" }'
            first = False
        else:
            question += ',{"text": "' + answer + '" }'
    question += '],' \
                '"flag_if_multiple": "0"}' \
                ']' \
                '}'
    return question
