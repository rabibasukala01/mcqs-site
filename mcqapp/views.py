from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from django.contrib.auth.decorators import login_required

from .models import Questions
from random import shuffle
from datetime import datetime

"""
Homepage
"""
def home(requests):
    return render(requests,'home.html')

"""
api to choosing answer to the question area()
"""
def questionArea(requests):
    questionset=list(Questions.objects.all())
    shuffle(questionset)  #shuffle the question in list
    if requests.method=='POST':
        score=0
        ur_answer=[] #to store user's wrong answer
        wrong_questions=[] #to store wrong question 
        for question in questionset:
            if question.correct_answer!=requests.POST[str(question.qid)]: #if answer is incorrect
                ur_answer.append(requests.POST[str(question.qid)])
                
                 # to get the each wrong question object from the id of the question
                wrong_questions.append(Questions.objects.get(qid=question.qid)) #filter returns the queryset all the object with the given id (so need to do [0]),get returns only the object with the given id

            else:  #if answer is correct
                score+=1
       
        
        wrongs=zip(wrong_questions,ur_answer) #ziping the wrong question object and user's wrong answer
        context={
            'score':score,
           'wrongs':wrongs,
        }
        
        return render(requests,'result.html',context)

    return render(requests,'questions.html',{'questionset':questionset})


"""
ADD question manually 
"""
def add_questions(requests):
    if requests.method=='POST':
        question_text=requests.POST['question_text']
        option1=requests.POST['option1']
        option2=requests.POST['option2']
        option3=requests.POST['option3']
        option4=requests.POST['option4']
        correct_answer=requests.POST['correct_answer']
        Questions(question_text=question_text,option1=option1,option2=option2,option3=option3,option4=option4,correct_answer=correct_answer).save()
        return HttpResponse('question added')
    return render(requests,'add_questions.html')

"""
AUthentications
"""
def sign_up(requests):
    if requests.method=='POST':
        first_name=requests.POST['first_name']
        last_name=requests.POST['last_name']
        username=requests.POST['username']
        email=requests.POST['email']
        password1=requests.POST['password1']
        password2=requests.POST['password2']

        #Todo -basic auth handle:
        if password1 != password2:
            return HttpResponse('cant create')
        
        try:
            users = User.objects.create_user(username, email, password1)
            users.first_name = first_name
            users.last_name = last_name
            users.last_login=datetime.now()
            users.save() 
            return HttpResponse('user created')
        except:
            pass

    return render(requests,'sign_up.html')

def sign_in(requests):
    if requests.method=='POST':
        username=requests.POST['username']
        password=requests.POST['password']
        user=authenticate(username=username,password=password)
        if user is not None:
            login(requests,user)
            return HttpResponse('logged in')

    return render(requests,'sign_in.html')

@login_required
def sign_out(requests):
    logout(requests)
    return HttpResponse('logged out')