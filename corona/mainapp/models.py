from django.db import models

class Answer(models.Model):
    voher = models.ImageField()
    nachher = models.ImageField()
    solution = models.BooleanField()
    question = models.ForeignKey(Question, related_name='', on_delete=models.CASCADE)


class Question(models.Model):
    pass

class Userscore(models.Model):
    pass
