from django.urls import path, include
from .views import *

urlpatterns = [
    path('', Home.as_view(),name="index"),
    path('Generator', Generator.as_view()),
    path('Generator/Jokes', Jokes.as_view()),
    path('Generator/Word', Word.as_view()),
    path('Generator/YT', YT.as_view()),
    path('Auth', Auth.as_view()),
    path('Registration/Registration', RegistartionApi.as_view()),
    path('Auth/Login', LoginApi.as_view()),
    path('Auth', Auth.as_view()),
    path('Registration', Registration.as_view()),
    path('User', User.as_view()),
    path('User/<int:id>', UserId.as_view()),
]
