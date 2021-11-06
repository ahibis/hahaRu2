from django.views.generic import View
from django.http.response import JsonResponse
from .managers.apiManager import *

class GetUser(View):
    def post(self):
        return JsonResponse(getUser(1))

class GetMy(View):
    def post(self, requests, *args, **kargs):
        return JsonResponse(getMy(id,requests))
