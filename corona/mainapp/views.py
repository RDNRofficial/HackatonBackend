from django.shortcuts import render
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView, ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import *
from .models import *

class ListAnswer(ListCreateAPIView):
    serializer_class = AnswerSerializer
    queryset = Answer.objects.get_queryset()