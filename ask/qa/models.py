import datetime

from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class QuestionManager(models.Manager):
    def new(self):
        return self.order_by('-added_at')

    def popular(self):
        return self.order_by('-rating')

class Question(models.Model):
    title = models.CharField(max_length=255, null=True)
    text = models.TextField(null=True)
    added_at = models.DateTimeField(null=True)
    rating = models.IntegerField(null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='question_name', null=True)
    likes = models.ManyToManyField(User)

    objects = QuestionManager()

    def get_url(self):
        return reverse('qa-question', kwargs={'question_id': self.id})

    def __str__(self):
        return self.title

class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField(null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='answer_author', null=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, null=True)

