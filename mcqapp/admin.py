from django.contrib import admin
from .models import Questions, QuestionsADD, Points

# Register your models here.

admin.site.register([Questions, QuestionsADD, Points])
