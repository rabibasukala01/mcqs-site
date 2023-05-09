from django.contrib import admin
from .models import Questions, QuestionsADD, Points, Category

# Register your models here.

admin.site.register([Questions, QuestionsADD, Points, Category])
