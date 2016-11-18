from django.core.urlresolvers import reverse
from django.db import models
from django.contrib.auth.models import User


class QuestionManager(models.Manager):

    def new(self):
        qs = super(QuestionManager, self).get_queryset()
        return qs.order_by('-id')

    def popular(self):
        qs = super(QuestionManager, self).get_queryset()
        return qs.order_by('-rating')


# Create your models here.
class Question(models.Model):
    objects = QuestionManager()
    title = models.CharField(max_length=255)
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name='question_author')
    likes = models.ManyToManyField(User, related_name='question_like')

    def get_absolute_url(self):
        return reverse('question', kwargs={"id": self.id})

    def __unicode__(self):
        return self.title


class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    author = models.ForeignKey(User, default=1, null=True, on_delete=models.SET_NULL)

    def __unicode__(self):
        return self.text




