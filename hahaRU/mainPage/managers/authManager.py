from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, Http404
from mainPage.moduls.guard import filter
from ..models import User
from ..exeptions import BadRequest
def Register(request):
    if request.method == "POST":
        login = request.POST['Name']
        email = request.POST['email']
        password = request.POST['Password']
        password2 = request.POST['Password2']
        if not login:
            raise BadRequest("Логин не может быть пустым!");
        if not email:
            raise BadRequest("Email не может быть пустым!");
        if not password:
            raise BadRequest("Пароль не может быть пустым!");
        if not password2:
            raise BadRequest("Повтор пароля не может быть пустым!");
        login = login.replace(" ", "")
        email = email.replace(" ", "")
        if not (login == filter(request.POST['Name'].replace(" ", ""))):
            raise BadRequest("Недопустимые символы в логине!");
        if not (password == filter(request.POST['Password'])):
            raise BadRequest("Недопустимые символы в пароле!");
        if not (password2 == filter(request.POST['Password2'])):
            raise BadRequest("Недопустимые символы в повторе пароля!");
        users = User.objects.filter(Login=login)
        if len(users)>0:
            raise BadRequest("пользователь с данным логином уже зарегистрирован!");
        users = User.objects.filter(Email=email)
        if len(users) > 0:
            raise BadRequest("пользователь с данным email уже зарегистрирован!");
        if (password != password2):
            raise BadRequest("Пароли не совпадают!");
        user = User(Login=login,Password=password,Email=email)
        user.save()
        return {"text":"ок","status":"ok"}
        

def Login(request):
    if request.method == "POST":
        login = request.POST['Name']
        password = request.POST['Password']
        if not login:
            raise BadRequest("Логин не может быть пустым!");
        if not password:
            raise BadRequest("Пароль не может быть пустым!");
        login = login.replace(" ", "")
        if not (login == filter(request.POST['Name'].replace(" ", ""))):
            raise BadRequest("Недопустимые символы в логине!");
        if not (password == filter(request.POST['Password'])):
            raise BadRequest("Недопустимые символы в повторе пароля!");
        users = User.objects.filter(Login=login)
        if not len(users):
            raise BadRequest("Нет пользователя с таким логином!")
        user = users[0]
        if not (password == user.Password):
            raise BadRequest("Пароль не верен!")
            
        return {"text":"ок","status":"ok"}
            # if (!Auth.VerifyHashedPassword(user.Password, data.Password)) return "Пароль не верен";
            # httpContext.Session.SetInt32("id", user.Id);