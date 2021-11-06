from django.shortcuts import render
from django.views.generic import TemplateView, View
from django.http.response import JsonResponse
from .models import Articale, Comment
from .managers.authManager import Register,Login
'''
def index(request):
    articles = Articale.objects.order_by("-date")
    return render(request, "mainPage/list.html",{"articles":articles})
'''
class Home(TemplateView):
    template_name = "Home/index.html"

class Auth(TemplateView):
    template_name = "Auth/index.html"

class Generator(TemplateView):
    template_name = "Generator/index.html"

class Jokes(TemplateView):
    template_name = "Generator/Jokes.html"

class Word(TemplateView):
    template_name = "Generator/Word.html"

class YT(TemplateView):
    template_name = "Generator/YT.html"

class Registration(TemplateView):
    template_name = "Registration/index.html"

class User(TemplateView):
    template_name = "User/index.html"
# Create your views here.
class RegistartionApi(View):
    def post(self,requests):
        try:
            return JsonResponse(Register(requests))
        except Exception as e:
            return JsonResponse({"text":"что-то не так","status":"error","what":str(e)})

class LoginApi(View):
    def post(self,requests):
        try:
            return JsonResponse(Login(requests))
        except Exception as e:
            return JsonResponse({"text":"что-то не так","status":"error","what":str(e)})