from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, Http404
from ..moduls.guard import filter
from django.core.validators import validate_email, EmailValidator
from django.contrib.auth import logout
from ..models import User
import re
import bcrypt


def Register(request):
    if request.method == "POST":
        login = request.POST['Name']
        email = request.POST['email']
        password = request.POST['Password']
        password2 = request.POST['Password2']
        if not login:
            return {"text": "Логин не может быть пустым!", "status": "error"}
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
        valid_email = email.split("@")
        if len(valid_email) != 2:
            return {"text": "Неверный формат email!", "status": "error"}
        valid_email = ''.join(valid_email)
        if not (valid_email == filter(valid_email)):
            return {"text": "Недопустимые символы в email!", "status": "error"}
        try:
            EmailValidator(message='Неверный формат email!', whitelist=[])(email)
        except:
            return {"text": "Неверный формат email!", "status": "error"}
        if not (password == filter(request.POST['Password'])):
            return {"text": "Недопустимые символы в пароле!", "status": "error"}
        if not (password2 == filter(request.POST['Password2'])):
            return {"text": "Недопустимые символы в повторе пароля!", "status": "error"}
        users = User.objects.filter(Login=login)
        if len(users) > 0:
            return {"text": "Такой пользователь уже зарегистрирован!", "status": "error"}
        users = User.objects.filter(Email=email)
        if len(users) > 0:
            return {"text": "Такой email уже занят!", "status": "error"}
        if (password != password2):
            return {"text": "Пароли не совпадают!", "status": "error"}
        password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        user = User(Login=login, Password=password, Email=email)
        user.save()
        return {"text": "ок", "status": "ok"}
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
            return {"text": "Логин не может быть пустым!", "status": "error"}
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
        if not bcrypt.checkpw(password.encode('utf-8'), user.Password.encode('utf-8')):
            return {"text": "Пароль не верен!", "status": "error"}
        request.session["id"] = user.id
        return {"text": "ок", "status": "ok"}


def logout_view(request):
    logout(request)