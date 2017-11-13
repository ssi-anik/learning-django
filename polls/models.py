from django.db import models
from django.utils.timezone import now


class Question(models.Model):
    db_table = 'questions'
    question_text = models.CharField(max_length=200, verbose_name='Question')
    publication_date = models.DateTimeField('Publish at: ', name='published_at')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    class Meta:
        db_table = 'choices'

    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200, verbose_name='choice')
    votes = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.choice_text
