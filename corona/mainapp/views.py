from django.shortcuts import render
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView, ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import *
from .models import *

class ListAnswer(ListCreateAPIView):
    serializer_class = AnswerSerializer
    queryset = Answer.objects.get_queryset()

class ListQuestion(ListCreateAPIView):
    serializer_class = QuestionSerializer
    queryset = Question.objects.get_queryset()

class ListExplanations(ListCreateAPIView):
    serializer_class = ExplanationSerializer
    queryset = Explanation.object.get_queryset()
    
class ListUserscore(ListCreateAPIView):
    serializer_class = UserscoreSerializer
    queryset = Userscore.objects.get_queryset()
