from django.urls import path, include
from api.views import *
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('question', QuestionsView, basename='questions')
router.register('answer', AnswersView, basename='answers')
urlpatterns = [

]+router.urls
