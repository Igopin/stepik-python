from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class QuestionManager(models.Manager):
    def new(self):
        return super().get_queryset().exclude(added_at__lt=datetime.date.today())

    def popular(self):
        return super().get_queryset().order_by('rating')

class Question(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    added_at = models.DateTimeField()
    rating = models.IntegerField()
    author = models.CharField(max_length=64)
    like = models.ManyToManyField(User)

    objects = QuestionManager()

class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField()
    author = models.CharField(max_length=64)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

