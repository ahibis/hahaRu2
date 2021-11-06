from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, Http404
from mainPage.moduls.guard import filter
from ..models import User
import re
def Register(request):
    if request.method == "POST":
        login = request.POST['Name']
        email = request.POST['email']
        password = request.POST['Password']
        password2 = request.POST['Password2']
        if not login:
            return {"text": "Логин не может быть пустым!","status": "error"}
        if not email:
            return {"text": "Email не может быть пустым!", "status": "error"}
        if not password:
            return {"text": "Пароль не может быть пустым!", "status": "error"}
        if not password2:
            return {"text": "Повтор пароля не может быть пустым!", "status": "error"}
        login = login.replace(" ", "")
        email = email.replace(" ", "")
        if not (login == filter(request.POST['Name'].replace(" ", ""))):
            return {"text": "Недопустимые символы в логине!", "status": "error"}
        if not (email == filter(request.POST['email'].replace(" ", ""))):
            return {"text": "Недопустимые символы в email!", "status": "error"}
        if not (password == filter(request.POST['Password'])):
            return {"text": "Недопустимые символы в пароле!", "status": "error"}
        if not (password2 == filter(request.POST['Password2'])):
            return {"text": "Недопустимые символы в повторе пароля!", "status": "error"}
        users = User.objects.filter(Login=login)
        if len(users)>0:
            return {"text": "Такой пользователь уже зарегистрирован!", "status": "error"}
        users = User.objects.filter(Email=email)
        if len(users) > 0:
            return {"text": "Такой email уже занят!", "status": "error"}
        if (password != password2):
            return {"text": "Пароли не совпадают!", "status": "error"}
        user = User(Login=login,Password=password,Email=email)
        user.save()
        return {"text":"ок","status":"ok"}
        '''
        newUser = User.objects.get(1);
        newUser["Login"] = "fdfdf";
        newUser.save()
        '''
        


def Login(request):
    if request.method == "POST":
        login = request.POST['Name']
        password = request.POST['Password']
        if not login:
            return {"text": "Логин не может быть пустым!","status": "error"}
        if not password:
            return {"text": "Пароль не может быть пустым!", "status": "error"}
        login = login.replace(" ", "")
        if not (login == filter(request.POST['Name'].replace(" ", ""))):
            return {"text": "Недопустимые символы в логине!", "status": "error"}
        if not (password == filter(request.POST['Password'])):
            return {"text": "Недопустимые символы в пароле!", "status": "error"}
        users = User.objects.filter(Login=login)
        if not len(users):
            return {"text": "Нет пользователя с таким логином!", "status": "error"}
        user = users[0]
        if not (password == user.Password):
            return {"text": "Пароль не верен!", "status": "error"}
        
        return {"text":"ок","status":"ok"}
            # if (!Auth.VerifyHashedPassword(user.Password, data.Password)) return "Пароль не верен";
            # httpContext.Session.SetInt32("id", user.Id);