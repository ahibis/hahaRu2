from django.views.generic import View
from django.http.response import JsonResponse
from .managers.apiManager import *
from .exeptions import safe, isAuth
from django.core.files.storage import FileSystemStorage
class GetUser(View):
    @safe
    def post(self, requests):
        id = 1
        if "id" in requests.POST:
            id = requests.POST["id"]
        return JsonResponse(getUser(id))

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

class GetRandomMemImg(View):
    @safe
    def post(self, requests):
        return JsonResponse(getRandomMemImg())

class GetRandomMemText(View):
    @safe
    def post(self, requests):
        return JsonResponse(getRandomMemText())

class GetRandomVideo(View):
    @safe
    def post(self, requests):
        return JsonResponse(getRandomVideo())

class SendPost(View):
    @safe
    @isAuth
    def post(self, requests, id):
        return JsonResponse(sendPost(requests.POST,id))


class SaveAva(View):
    @safe
    @isAuth
    def post(self, requests, id):
        return JsonResponse(sendAva(requests.FILES, id))

class ChangeContentDisLiked(View):
    @safe
    @isAuth
    def post(self, requests, id):
        return JsonResponse(changeContentDisLiked(requests.POST,id))

class ChangeContentLiked(View):
    @safe
    @isAuth
    def post(self, requests, id):
        return JsonResponse(changeContentLiked(requests.POST,id))

class ChangeDisLiked(View):
    @safe
    @isAuth
    def post(self, requests, id):
        return JsonResponse(changeDisLiked(requests.POST,id))
class ChangeLiked(View):
    @safe
    @isAuth
    def post(self, requests, id):
        return JsonResponse(changeLiked(requests.POST,id))

class SaveMemPic(View):
    @safe
    def post(self, requests):
        return JsonResponse(saveMemPic(requests.FILES))

class SaveMem(View):
    def post(self, requests):
        return JsonResponse(saveMem(requests.POST))
