from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, Http404

from django.core.exceptions import ValidationError
from ..models import User
from ..exeptions import BadRequest, check
import bcrypt
def Register(request):
    if request.method == "POST":
        login = request.POST['Name']
        email = request.POST['email']
        password = request.POST['Password']
        password2 = request.POST['Password2']
        if not password2:
            raise BadRequest("Повтор пароля не может быть пустым!");
        users = User.objects.filter(Login=login)
        if len(users)>0:
            raise BadRequest("пользователь с данным логином уже зарегистрирован!");
        users = User.objects.filter(Email=email)
        if len(users) > 0:
            raise BadRequest("пользователь с данным email уже зарегистрирован!");
        if (password != password2):
            raise BadRequest("Пароли не совпадают!")
        password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        user = User(Login=login,Password=password,Email=email)
        check(user)
        user.save()
        request.session["id"]= user.id
        return {"text":"ок","status":"ok"}
        


def Login(request):
    if request.method == "POST":
        login = request.POST['Name']
        password = request.POST['Password']
        users = User.objects.filter(Login=login)
        if not len(users):
            raise BadRequest("Нет пользователя с таким логином!")
        user = users[0]
        if not bcrypt.checkpw(password.encode('utf-8'), user["Password"].encode('utf-8')):
            raise BadRequest("Пароль не верен!")
        check(user)
        request.session["id"]= user.id
        return {"text":"ок","status":"ok"}

def logout_view(request):
    pass

