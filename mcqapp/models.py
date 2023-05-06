from django.db import models
import uuid


# Create your models here.

"""
models to add question by  admins
"""


class Questions(models.Model):
    question_text = models.CharField(max_length=500)
    qid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    option1 = models.CharField(max_length=300)
    option2 = models.CharField(max_length=300)
    option3 = models.CharField(max_length=300)
    option4 = models.CharField(max_length=300)
    correct_answer = models.CharField(max_length=300)

    def __str__(self):
        return self.question_text


"""
model to add/hold contributer's questions in unstaging area.wait for reject or accept
"""


class QuestionsADD(models.Model):
    question_text = models.CharField(max_length=500)
    qid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    option1 = models.CharField(max_length=300)
    option2 = models.CharField(max_length=300)
    option3 = models.CharField(max_length=300)
    option4 = models.CharField(max_length=300)
    correct_answer = models.CharField(max_length=300)

    def __str__(self):
        return self.question_text + "-" + str(self.qid)
