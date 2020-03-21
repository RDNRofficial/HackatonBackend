from django.conf.urls import url, include
from django.contrib import admin


from .views import *

urlpatterns = [
    url(r'answer/$', ListAnswer.as_view()),
    url(r'question/$', ListQuestion.as_view()),
    url(r'userlevel/$', ListUserlevel.as_view()),
    url(r'explanation/$', ListExplanations.as_view()),
    url(r'diymanuals/$', ListDIYManuals.as_view()),
    url(r'qa/$', ListQA.as_view()),
    url(r'diy/$', ListDIY.as_view()),
    url(r'answer/item/(?P<pk>[0-9]+)/$', ModifyAnswer.as_view()),
    url(r'question/item/(?P<pk>[0-9]+)/$', ModifyQuestion.as_view()),
    url(r'userlevel/item/(?P<pk>[0-9]+)/$', ModifyUserlevel.as_view()),
    url(r'explanation/item/(?P<pk>[0-9]+)/$', ModifyExplanation.as_view()),
    url(r'diymanuals/item/(?P<pk>[0-9]+)/$', ModifyDIYManuals.as_view())
]