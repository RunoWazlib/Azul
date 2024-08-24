from django.db import models

# Create your models here.
# straight from Django how to make a poll
class Question(models.Model):
    # database fields
    # column name = value
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

class Choice(models.Model):
    #Foreign Key defines a relationship (each choice is related to a single question)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)