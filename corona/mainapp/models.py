from django.db import models

class Question(models.Model):
    frage = models.CharField(max_length=100)
    background = models.ImageField()
    audio = models.CharField(max_length=100) #TODO


class Answer(models.Model):
    voher = models.ImageField()
    nachher = models.ImageField()
    solution = models.BooleanField()
    question = models.ForeignKey(Question, related_name='question', on_delete=models.CASCADE)
    x = models.IntegerField()
    y = models.IntegerField()

class Userscore(models.Model):
    score = models.IntegerField()
    username = models.CharField(max_length=30 ,unique=True)
