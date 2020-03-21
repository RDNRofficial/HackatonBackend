from rest_framework import serializers
from drf_queryfields import QueryFieldsMixin
from .models import *

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ("__all__")