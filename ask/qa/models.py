import uuid

from django.db import models


# class QuestionManager(models.Manager):
#
#     def new(self):
#         qs = super(QuestionManager, self).get_queryset()
#         return qs.order_by('-id')
#
#     def popular(self):
#         qs = super(QuestionManager, self).get_queryset()
#         return qs.order_by('-rating')
#
#
# # Create your models here.
# class Question(models.Model):
#     objects = QuestionManager()
#     title = models.CharField(max_length=255)
#     text = models.TextField()
#     added_at = models.DateTimeField(auto_now_add=True)
#     rating = models.IntegerField(default=0)
#     author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='question_author')
#     likes = models.ManyToManyField(User, related_name='question_like')
#
#     def get_url(self):
#         return "/question/{}/".format(self.id)
#
#     def __unicode__(self):
#         return self.title
#
#
# class Answer(models.Model):
#     text = models.TextField()
#     added_at = models.DateTimeField(auto_now_add=True)
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     author = models.ForeignKey(User, on_delete=models.CASCADE)
#
#     def __unicode__(self):
#         return self.text

class Host(models.Model):
    table_name = models.TextField()
    host_name = models.TextField()
    eea_sqm = models.TextField()
    iSecure = models.TextField()
    dev_pt = models.TextField()
    hardware_model = models.TextField()
    hardware_cpuram = models.TextField()
    os = models.TextField()
    oracle = models.TextField()
    iSecure_link = models.TextField()
    sqm_link = models.TextField()
    svc_mgmt_link = models.TextField()
    eea_sqm_gui_link = models.TextField()
    database = models.TextField()
    utf8 = models.TextField()
    last_update = models.DateTimeField(auto_now_add=True)
    owner = models.TextField()
    comments = models.TextField()

    def __unicode__(self):
        return self.text









