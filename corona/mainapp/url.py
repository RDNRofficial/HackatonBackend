from django.conf.urls import url, include
from django.contrib import admin


from .views import *

urlpatterns = [
    url(r'answer/$', ListAnswer.as_view()),
    url(r'question/$', ListQuestion.as_view()),
]