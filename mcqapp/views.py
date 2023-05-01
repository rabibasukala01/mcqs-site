from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import JsonResponse,HttpResponse

from .models import Questions
from random import shuffle

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
        wrong_question_id=[]

        for question in questionset:
            if question.correct_answer!=requests.POST[str(question.qid)]: #if answer is incorrect
                wrong_question_id.append(question.qid)

            else:  #if answer is correct
                score+=1
            
        return JsonResponse({'score':score,
                            'wrong_question_id':wrong_question_id})


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
        password=requests.POST['password']
        email=requests.POST['email']
        try:
            users = User.objects.create_user(username, email, password1)
            users.first_name = first_name
            users.last_name = last_name
            users.save() 
            return HttpResponse('user created')
        except:
            return HttpResponse('user created')
           

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

def sign_out(requests):
    logout(requests)
    return HttpResponse('logged out')