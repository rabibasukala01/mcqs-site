from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.decorators import login_required

from .models import Questions, QuestionsADD, Points
from random import shuffle
from datetime import datetime

"""
Homepage   
"""


def home(requests):
    return render(requests, "home.html")


"""
api to choosing answer to the question area()
"""


def questionArea(requests):
    questionset = list(Questions.objects.all())
    shuffle(questionset)  # shuffle the question in list
    if requests.method == "POST":
        score = 0
        ur_answer = []  # to store user's wrong answer
        wrong_questions = []  # to store wrong question
        for question in questionset:
            if (
                question.correct_answer != requests.POST[str(question.qid)]
            ):  # if answer is incorrect
                ur_answer.append(requests.POST[str(question.qid)])

                # to get the each wrong question object from the id of the question
                wrong_questions.append(
                    Questions.objects.get(qid=question.qid)
                )  # filter returns the queryset all the object with the given id (so need to do [0]),get returns only the object with the given id

            else:  # if answer is correct
                score += 1

        wrongs = zip(
            wrong_questions, ur_answer
        )  # ziping the wrong question object and user's wrong answer
        context = {
            "score": score,
            "wrongs": wrongs,
        }

        return render(requests, "result.html", context)

    return render(requests, "questions.html", {"questionset": questionset})


"""
ADD question manually 
"""


@login_required
def add_questions(requests):
    if requests.method == "POST":
        question_text = requests.POST["question_text"]
        option1 = requests.POST["option1"]
        option2 = requests.POST["option2"]
        option3 = requests.POST["option3"]
        option4 = requests.POST["option4"]
        correct_answer = requests.POST["correct_answer"]
        QuestionsADD(
            question_text=question_text,
            option1=option1,
            option2=option2,
            option3=option3,
            option4=option4,
            correct_answer=correct_answer,
            who_added=requests.user,
        ).save()
        # print(requests.user)

        return HttpResponse(
            "Question added! thank you for your contribution.We will shortly view your question"
        )
    return render(requests, "add_questions.html")


"""
show added questions
"""


def show_added_questions(requests):
    questions = QuestionsADD.objects.all()
    return render(requests, "show_added_questions.html", {"questions": questions})


"""
accept the question and add points to that contributor
"""


def accept_added_questions(request, qid):
    thatquestion = QuestionsADD.objects.get(qid=qid)
    question_text = thatquestion.question_text
    option1 = thatquestion.option1
    option2 = thatquestion.option2
    option3 = thatquestion.option3
    option4 = thatquestion.option4
    correct_answer = thatquestion.correct_answer
    Questions(
        question_text=question_text,
        option1=option1,
        option2=option2,
        option3=option3,
        option4=option4,
        correct_answer=correct_answer,
    ).save()

    user = User.objects.get(username=thatquestion.who_added)
    pointsOBJ = Points.objects.get(user=user.id)
    pointsOBJ.points = pointsOBJ.points + 1
    pointsOBJ.save()  # update the points of the user in the Points db |

    # delete from secondary db(QuestionADD) after adding to primary db(Questions)
    thatquestion.delete()

    print(f"Question of id {qid} is added to the Question db(primary)")
    return redirect("show_added_questions")


"""
reject the question
(delete the question from holding/secondary(QuestionADD) db)
"""


def reject_added_questions(request, qid):
    # TODO - some alert before deleting
    QuestionsADD.objects.get(qid=qid).delete()
    return HttpResponse(f"Question of id {qid} rejected")


"""
AUthentications
"""


def sign_up(requests):
    if requests.method == "POST":
        first_name = requests.POST["first_name"]
        last_name = requests.POST["last_name"]
        username = requests.POST["username"]
        email = requests.POST["email"]
        password1 = requests.POST["password1"]
        password2 = requests.POST["password2"]

        # TODO -basic auth handle:
        if password1 != password2:
            return HttpResponse("cant create")

        try:
            users = User.objects.create_user(username, email, password1)
            users.first_name = first_name
            users.last_name = last_name
            users.last_login = datetime.now()
            users.save()
            extended_user = Points(user=users, points=0)
            extended_user.save()
            return HttpResponse("user created")
        except:
            pass

    return render(requests, "sign_up.html")


def sign_in(requests):
    if requests.method == "POST":
        username = requests.POST["username"]
        password = requests.POST["password"]
        user = authenticate(username=username, password=password)
        if user is not None:
            login(requests, user)
            return HttpResponse("logged in")

    return render(requests, "sign_in.html")


@login_required
def sign_out(requests):
    logout(requests)
    return HttpResponse("logged out")
