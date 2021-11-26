from django.views.generic import View
from django.http.response import JsonResponse
from .managers.apiManager import *
from .exeptions import safe, isAuth
class GetUser(View):
    @safe
    def post(self, requests):
        return JsonResponse(getUser(1))

class GetMy(View):
    @safe
    @isAuth
    def post(self, requests, id):
        data = getMy(id)
        return JsonResponse(data)

class UpdateUser(View):
    @safe
    @isAuth
    def post(self, requests, id):
        return JsonResponse(updateUser(requests.POST,id))

class GetContents(View):
    @safe
    def post(self, requests):
        return JsonResponse(getContents(requests.POST))

class GetPosts(View):
    @safe
    def post(self, requests):
        return JsonResponse(getPosts(requests.POST))

class GetRundomMemImg(View):
    @safe
    def post(self, requests):
        return JsonResponse(getRandomMemImg())

class GetRundomMemText(View):
    @safe
    def post(self, requests):
        return JsonResponse(getRandomMemText())

class GetRundomVideo(View):
    @safe
    def post(self, requests):
        return JsonResponse(getRandomVideo())

class SendPost(View):
    @safe
    @isAuth
    def post(self, requests, id):
        return JsonResponse(sendPost(requests.POST,id))