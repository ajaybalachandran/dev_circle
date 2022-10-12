from django.shortcuts import render
from rest_framework.viewsets import ViewSet, ModelViewSet
from rest_framework.response import Response
from api.models import *
from api.serializers import *
from rest_framework import authentication, permissions
from rest_framework.decorators import action
# Create your views here.


# =============================== Users View =================================
class UsersView(ViewSet):
    def create(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)


# ============================= Questions View ===============================
class QuestionsView(ViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    authentication_classes = [authentication.TokenAuthentication]

    def list(self, request, *args, **kwargs):
        all_questions = Questions.objects.all()
        serializer = QuestionSerializer(all_questions, many=True)
        return Response(data=serializer.data)

    def create(self, request, *args, **kwargs):
        # tags = request.data.pop('tags')
        serializer = QuestionSerializer(data=request.data, context={'user': request.user})
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)

    def retrieve(self, request, *args, **kwargs):
        id = kwargs.get('pk')
        question = Questions.objects.get(id=id)
        serializer = QuestionSerializer(question)
        return Response(data=serializer.data)

    def update(self, request, *args, **kwargs):
        id = kwargs.get('pk')
        question = Questions.objects.get(id=id)
        if question.user == request.user:
            serializer = QuestionSerializer(instance=question, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(data=serializer.data)
            else:
                return Response(data=serializer.errors)
        else:
            return Response(data={'msg': 'Access Denied'})

    def destroy(self, request, *args, **kwargs):
        id = kwargs.get('pk')
        question = Questions.objects.get(id=id)
        if question.user == request.user:
            question.delete()
            return Response(data={'msg': 'Deleted'})
        else:
            return Response(data={'msg': 'Access Denied'})

    @action(methods=['POST'], detail=True)
    def add_answer(self, request, *args, **kwargs):
        id = kwargs.get('pk')
        question = Questions.objects.get(id=id)
        if question.user != request.user:
            serializer = AnswerSerializer(data=request.data, context={'question': question, 'user': request.user})  # doubt look in answers view
            if serializer.is_valid():
                serializer.save()
                return Response(data=serializer.data)
            else:
                return Response(data=serializer.errors)
        else:
            return Response(data={'msg': 'Access Denied'})

    @action(methods=['GET'], detail=True)
    def get_answers(self, request, *args, **kwargs):
        id = kwargs.get('pk')
        question = Questions.objects.get(id=id)
        answers = question.answers_set.all()
        serializer = AnswerSerializer(answers, many=True)
        return Response(data=serializer.data)


# =============================== Answers View =================================
class AnswersView(ViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    authentication_classes = [authentication.TokenAuthentication]

    def retrieve(self, request, *args, **kwargs):
        id = kwargs.get('pk')
        answer = Answers.objects.get(id=id)
        serializer = AnswerSerializer(answer)
        return Response(data=serializer.data)

    def update(self, request, *args, **kwargs):
        id = kwargs.get('pk')
        answer = Answers.objects.get(id=id)
        if answer.user == request.user:
            serializer = AnswerSerializer(instance=answer, data=request.data)  # doubt
            if serializer.is_valid():
                serializer.save()
                return Response(data=serializer.data)
            else:
                return Response(data=serializer.errors)
        else:
            return Response(data={'msg': 'Access Denied'})