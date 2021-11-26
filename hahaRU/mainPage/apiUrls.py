from django.urls import path
from .apis import *

urlpatterns = [
    path("getUser", GetUser.as_view()),
    path("getMy", GetMy.as_view()),
    path("updateUser", UpdateUser.as_view()),
    path("getContents", GetContents.as_view()),
    path("getPosts", GetPosts.as_view()),
    path("getRandomMemImg", GetRundomMemImg.as_view()),
    path("getRandomMemText", GetRundomMemText.as_view()),
    path("getRandomVideo", GetRundomVideo.as_view()),
    path("sendPost", SendPost.as_view()),
]