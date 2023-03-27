from django.urls import path
from . import views

urlpatterns = [
    path("",views.home,name="home"),
    path("add",views.add_questions,name="add_questions"),
    path("signup",views.sign_up,name="sign_up"),
    path("signin",views.sign_in,name="sign_in"),
    path("signout",views.sign_out,name="sign_out"),
]
