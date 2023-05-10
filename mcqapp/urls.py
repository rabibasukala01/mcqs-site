from django.urls import path
from . import views

urlpatterns = [
    path("home", views.home, name="home"),
    path("", views.questionArea, name="questionArea"),
    path("add", views.add_questions, name="add_questions"),
    path(
        "dashboard/",
        views.admindashboard,
        name="admindashboard",
    ),
    path(
        "dashboard/show_added_questions/<str:id>",
        views.show_added_questions,
        name="show_added_questions",
    ),
    path(
        "show_added_questions/accept/<str:qid>",
        views.accept_added_questions,
        name="accept_added_questions",
    ),
    path(
        "show_added_questions/reject/<str:qid>",
        views.reject_added_questions,
        name="reject_added_questions",
    ),
    path("signup", views.sign_up, name="sign_up"),
    path("signin", views.sign_in, name="sign_in"),
    path("signout", views.sign_out, name="sign_out"),
]
