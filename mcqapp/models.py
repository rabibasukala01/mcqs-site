from django.db import models
import uuid
# Create your models here.
class Questions(models.Model):
    question_text = models.CharField(max_length=500)
    qid=models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    option1 = models.CharField(max_length=300)
    option2 = models.CharField(max_length=300)
    option3 = models.CharField(max_length=300)
    option4 = models.CharField(max_length=300)
    correct_answer = models.CharField(max_length=300)
    

    def __str__(self):
        return self.question_text
