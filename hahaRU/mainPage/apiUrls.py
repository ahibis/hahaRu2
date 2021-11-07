from django.urls import path
from .apis import *

urlpatterns = [
    path("getUser", GetUser.as_view()),
    path("getMy", GetMy.as_view()),
    path("updateUser",UpdateUser.as_view())
]