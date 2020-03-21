from django.conf.urls import url, include
from django.contrib import admin


from .views import *

urlpatterns = [
    url(r'answer/$', ListAnswer.as_view()),
    url(r'question/$', ListQuestion.as_view()),
    url(r'userscore/$', ListUserscore.as_view()),
    url(r'explanation/$', ListExplanations.as_view()),
    url(r'diymanuals/$', ListDIYManuals.as_view()),
    url(r'qa/$', ListQA.as_view()),
    url(r'diy/$', ListDIY.as_view())
]