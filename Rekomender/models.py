from django.db import models
from jsonfield import JSONField
# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)  

    def __str__(self):
        return self.choice_text  

class Cloud(models.Model):
    provider_name = models.CharField(max_length=50) # wszystko z tabelki
    def __str__(self):
        return self.Cloud_text

class user(models.Model):
    id = models.IntegerField(primary_key=1)
    amazon = models.IntegerField(default=0)
    google = models.IntegerField(default=0)
    microsoft = models.IntegerField(default=0)
    krajowa = models.IntegerField(default=0)
    ibm = models.IntegerField(default=0)
    city = models.IntegerField(default=0)
    task = models.IntegerField(default=0)            
    #list of services ? 
# class Service(models.Model):
#     name =  models.CharField(max_length=100)
#     weight = models.IntegerField(default=1)
class Client(models.Model):
    client_name = models.CharField(max_length=50)
    client_experience = models.IntegerField(default=0)
    def __str__(self):
        return self.Client_text
# class VirtualUser(models.Model):
#     name = models.CharField(max_length=50)
class QuestionChoices(models.Model):
    info = JSONField(null=True, blank=True)

    @classmethod
    def create(cls, info):
        question = cls(info=info)
        # do something with the book
        return QuestionChoices


#przykładowy json, zamiast tworzyć CSV zrobić jsona, łatwiejszy w imporcie
#  "questions":[ 
#  {
#   "question_text": "W jaki sposób chciałbyś się skontaktować z serwisantem/ pomocnikiem do konfiguracji?"
#   "date_added": "random",
#   "Choices": [
#     {
#       "text": "Telefonicznie",
#       "AnswerDescription": [
#       {
#           "Google": "nie mam pomysłu dlaczego",
#       },
#       {
#           "Amazon": "Amazon rządzi",
#       },
#       {
#           "Microsoft": "Great, ale wysokie koszty",
#       },
#       {
#           "Krajowa": "Krajowy dostawca, jako nieliczny umożliwia konakt w języku polskim",
#       },
#       {
#           "IBM": "Słaby zasięg",
#       },
#       {
#           "City": "Długi czas oczekiwania na połączenie ",
#       },
#       {
#           "TASK": "Lokalny dostawca, jako nieliczny umożliwia konakt w języku polskim",
#       }
#       ],AnswerDescription
   #     "weights": [
#       {
#           "Google": 1,
#            "desGoogle": "nie mam pomysłu dlaczego",
#       },
#       {
#           "Amazon": 1,
#            "desAmazon": "Amazon rządzi",
#       },
#       {
#           "Microsoft": 1,
#            "desMicrosoft": "Great, ale wysokie koszty",
#       },
#       {
#           "Krajowa": 1,
#            "desKrajowa": "Krajowy dostawca, jako nieliczny umożliwia konakt w języku polskim",

#       },
#       {
#           "IBM": 1,
#            "desIBM": "Słaby zasięg",
#       },
#       {
#           "City": 1,
 #           "desCity": "Długi czas oczekiwania na połączenie ",
#       },
#       {
#           "TASK": 1,
  #          "desTASK": "Lokalny dostawca, jako nieliczny umożliwia konakt w języku polskim",
#       }
#       ],
#     },
#     {
#       "type": "Email",
#       "weights": [
#       {
#           "Google": 1,
#       },
#       {
#           "Amazon": 1,
#       },
#       {
#           "Microsoft": 1,
#       },
#       {
#           "Krajowa": 1,
#       },
#       {
#           "IBM": 1,
#       },
#       {
#           "City": 1,
#       },
#       {
#           "TASK": 1,
#       }
#       ],
#     }
#   ],
#   "flag_if_multiple": 0
# }
# ],

  
