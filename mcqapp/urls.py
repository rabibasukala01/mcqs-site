from django.urls import path
from . import views

urlpatterns = [
    path("home",views.home,name="home"),
    path("",views.questionArea,name="questionArea"),
    path("add",views.add_questions,name="add_questions"),
    path("signup",views.sign_up,name="sign_up"),
    path("signin",views.sign_in,name="sign_in"),
    path("signout",views.sign_out,name="sign_out"),
]
