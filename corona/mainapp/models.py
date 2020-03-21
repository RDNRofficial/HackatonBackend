from django.db import models

class Answer(models.Model):
    voher = ImageField()
    nachher = ImageField()
    solution = BooleanField()
    question = models.ForeignKey(Question, related_name='', on_delete=models.CASCADE)


class Question(models.Model):


class Userscore(models.Model):

