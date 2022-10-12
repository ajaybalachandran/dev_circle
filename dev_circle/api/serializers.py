from rest_framework import serializers
from django.contrib.auth.models import User
from api.models import *


class UserSerializer(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True)
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email', 'username', 'password']

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class QuestionSerializer(serializers.ModelSerializer):
    user = serializers.CharField(read_only=True)
    asked_date = serializers.DateTimeField(read_only=True)
    # tags = serializers.CharField(read_only=True)

    class Meta:
        model = Questions
        fields = '__all__'

    def validate_tags(self, value):
        # print(value)
        count = len(value)
        print(count)
        if count > 5:
            raise serializers.ValidationError('only 5 tags were allowed')
        return value

    def create(self, validated_data):
        user = self.context.get('user')
        # print(validated_data)
        tags = validated_data.pop('tags')
        # print(tags)
        question = Questions.objects.create(**validated_data, user=user)
        # print(question.id)
        question = Questions.objects.get(id=question.id)
        for tag in tags:
            question.tags.add(tag)
            question.save()

        return question


class AnswerSerializer(serializers.ModelSerializer):
    user = serializers.CharField(read_only=True)
    question = serializers.CharField(read_only=True)
    answered_date = serializers.CharField(read_only=True)
    up_vote = serializers.CharField(read_only=True)
    down_vote = serializers.CharField(read_only=True)

    class Meta:
        model = Answers
        fields = '__all__'

    def create(self, validated_data):
        question = self.context.get('question')
        user = self.context.get('user')
        return Answers.objects.create(**validated_data, question=question, user=user)