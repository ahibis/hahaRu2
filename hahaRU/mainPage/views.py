from django.shortcuts import render
from django.views.generic import TemplateView, View
from django.http.response import JsonResponse
from .models import Articale, Comment, FunnyWord
from .managers.authManager import Register, Login
from .exeptions import safe
from .managers.GeneratorManager import anecdotGen, funnyWordGen
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
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['anecdot'] = anecdotGen()
        return context

class Word(TemplateView):
    template_name = "Generator/Word.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['word'] = funnyWordGen()
        return context

class YT(TemplateView):
    template_name = "Generator/YT.html"

class Registration(TemplateView):
    template_name = "Registration/index.html"

class User(TemplateView):
    template_name = "User/index.html"
# Create your views here.
class RegistartionApi(View):
    @safe
    def post(self,requests):
        return JsonResponse(Register(requests))

class LoginApi(View):
    @safe
    def post(self,requests):
        return JsonResponse(Login(requests))
        