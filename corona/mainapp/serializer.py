from rest_framework import serializers
from drf_queryfields import QueryFieldsMixin
from .models import *

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ("__all__")

        
class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ("__all__")

        
class UserscoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Userscore
        fields = ("__all__")

class ExplanationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Explanation
        fields = ("__all__")

class DIYManualSerializer(serializers.ModelSerializer):
    class Meta:
        model = DIYManual
        fields = ("__all__")