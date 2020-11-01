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
<<<<<<< HEAD
=======
    #list of services ? 
# class Service(models.Model):
#     name =  models.CharField(max_length=100)
#     weight = models.IntegerField(default=1)
>>>>>>> 45d781d92777623c27661f5e3c767040f59a2211
class Client(models.Model):
    client_name = models.CharField(max_length=50)
    client_experience = models.IntegerField(default=0)
    def __str__(self):
        return self.Client_text
# class VirtualUser(models.Model):
#     name = models.CharField(max_length=50)
class QuestionChoices(models.Model):
    info = JSONField(null=True, blank=True)

<<<<<<< HEAD
    @classmethod
    def create(cls, info):
        question = cls(info=info)
        # do something with the book
        return QuestionChoices

=======
>>>>>>> 45d781d92777623c27661f5e3c767040f59a2211

#przykładowy json, zamiast tworzyć CSV zrobić jsona, łatwiejszy w imporcie
#  "questions":[ 
#  {
#   "question_text": "W jaki sposób chciałbyś się skontaktować z serwisantem/ pomocnikiem do konfiguracji?"
#   "date_added": "random",
#   "Choices": [
#     {
#       "text": "Telefonicznie",   
#     },
#     {
#       "type": "Email",   
#     }
#   ],
#   "flag_if_multiple": 0
# }
# ],
  #check this out !!!!! https://django-import-data.readthedocs.io/en/latest/
<<<<<<< HEAD

  
=======
>>>>>>> 45d781d92777623c27661f5e3c767040f59a2211
