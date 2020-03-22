from django.shortcuts import render
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView, ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import *
from .models import *

#Answer
class ListAnswer(ListCreateAPIView):
    serializer_class = AnswerSerializer
    queryset = Answer.objects.get_queryset()

class ModifyAnswer(RetrieveUpdateDestroyAPIView):
    serializer_class = AnswerSerializer
    queryset = Answer.objects.get_queryset()
    lookup_field = 'pk'

#Question 
class ListQuestion(ListCreateAPIView):
    serializer_class = QuestionSerializer
    queryset = Question.objects.get_queryset()

class ModifyQuestion(RetrieveUpdateDestroyAPIView):
    serializer_class = QuestionSerializer
    queryset = Question.objects.get_queryset()
    lookup_field = 'pk'

#Explanation
class ListExplanations(ListCreateAPIView):
    serializer_class = ExplanationSerializer
    queryset = Explanation.objects.get_queryset()

class ModifyExplanation(RetrieveUpdateDestroyAPIView):
    serializer_class = ExplanationSerializer
    queryset = Question.objects.get_queryset()
    lookup_field = 'pk'

#Userlevel
class ListUserlevel(ListCreateAPIView):
    serializer_class = UserlevelSerializer
    queryset = Userlevel.objects.get_queryset()

class ModifyUserlevel(RetrieveUpdateDestroyAPIView):
    serializer_class = UserlevelSerializer
    queryset = Question.objects.get_queryset()
    lookup_field = 'username'

#DIYList
class ListDIYList(ListCreateAPIView):
    serializer_class = DIYListSerializer
    queryset = DIYList.objects.get_queryset()

class ModifyDIYList(RetrieveUpdateDestroyAPIView):
    serializer_class = DIYListSerializer
    queryset = DIYList.objects.get_queryset()
    lookup_field = 'pk'    

#DIYManuals
class ListDIYManuals(ListCreateAPIView):
    serializer_class = DIYManualSerializer
    queryset = DIYManual.objects.get_queryset()

class ModifyDIYManuals(RetrieveUpdateDestroyAPIView):
    serializer_class = DIYManualSerializer
    queryset = DIYManual.objects.get_queryset()
    lookup_field = 'pk'

#QA
class ListQA(ListAPIView):
    serializer_class = QuestionAnswerSerializer
    queryset = Question.objects.get_queryset()

#DIY
class ListDIY(ListAPIView):
    serializer_class = DIYSerializer
    queryset = DIYManual.objects.get_queryset()