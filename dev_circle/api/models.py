from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Tags(models.Model):
    tag = models.CharField(max_length=50)
    tag_description = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.tag


class Questions(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=250)
    link = models.URLField(max_length=200, null=True)
    code = models.CharField(max_length=500, null=True)
    image = models.ImageField(upload_to='images', null=True)
    asked_date = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tags)

    def __str__(self):
        return self.title


class Answers(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Questions, on_delete=models.CASCADE)
    description = models.CharField(max_length=250)
    link = models.URLField(max_length=200, null=True)
    code = models.CharField(max_length=500, null=True)
    image = models.ImageField(upload_to='ans_images', null=True)
    answered_date = models.DateTimeField(auto_now_add=True)
    up_vote = models.ManyToManyField(User, related_name='ans_up', null=True)
    down_vote = models.ManyToManyField(User, related_name='ans_down', null=True)

    def __str__(self):
        return self.description

    class Meta:
        unique_together = ('user', 'question')