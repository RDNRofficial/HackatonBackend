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


class UserlevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Userlevel
        fields = ("__all__")


class ExplanationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Explanation
        fields = ("__all__")


class DIYManualSerializer(serializers.ModelSerializer):
    class Meta:
        model = DIYManual
        fields = ("__all__")


class QuestionAnswerSerializer(serializers.ModelSerializer):
    """Combined Serializer for a Question and all its possible answers"""
    answers = serializers.SerializerMethodField()

    class Meta:
        model = Question
        fields = ("__all__")

    def get_answers(self, obj):
        """Gets all answers with a reference to the serialized question"""
        answer_list = Answer.objects.filter(question=obj.pk)
        serializer = AnswerSerializer(instance=answer_list, many=True)
        return serializer.data


class DIYSerializer(serializers.ModelSerializer):
    """Combined Serializer for a DIYManual and all its explanations"""
    steps = serializers.SerializerMethodField()

    class Meta:
        model = DIYManual
        fields = ("__all__")

    def get_steps(self, obj):
        """Gets all explanations wich have a reference to the serialized DIYManual"""
        explanation_list = Explanation.objects.filter(manual=obj.pk)
        serializer = ExplanationSerializer(instance=explanation_list, many=True)
        return serializer.data
