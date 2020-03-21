import django
import os
import sys
import random
from mainapp.models import *


tables = [Question, Answer, Userlevel, DIYManual,Explanation]
QUESTIONS = []
ANSWERS = []
USER_LEVEL = []
DIY_MANUALS = []
EXPLANATIONS = []



def delete_tables():
    print("Delete all")
    for table in tables:
        for o in table.objects.all():
            o.delete()


def save(model, modelName, list):
    if len(model.objects.all()) == 0:
        print("Add "+modelName+" Object")
        for m in list:
            m.save()


def create_question():
    save(Question, "Question", QUESTIONS)


def create_answer():
    save(Answer, "Answer", ANSWERS)


def create_userlevel():
    save(Userlevel, "Userlevel", USER_LEVEL)


def create_diymanual():
    save(DIYManual, "DIYManual", DIY_MANUALS)


def create_explanation():
    save(Explanation, "Explanation", EXPLANATIONS)


if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "corona.settings")
    django.setup()
    generate()


def generate():
    print("make migrations\n")
    os.system("python manage.py makemigrations")
    print("migrate\n")
    os.system("python manage.py migrate")
    delete_tables()
    create_question()
    create_answer()
    create_userlevel()
    create_diymanual()
    create_explanation()
    print("DONE\n")
