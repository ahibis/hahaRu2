from ..exeptions import AuthError, BadRequest
from ..models import *
from datetime import date
def getUser(id):
    user = User.objects.get(pk=id);
    if not user:
        raise BadRequest("user with this id doesn't defined")
    user.Password=""
    a=user.__dict__
    del a['_state']
    return user.__dict__

def getMy(id=0):
    return getUser(id)

def updateUser(data,id):
    keys = data.keys()
    if not "id" in data.keys():
        raise BadRequest("id is required")
    if id != int(data["id"]):
        raise BadRequest("нельзя изменять чужой аккаунт")
    user = User.objects.get(pk=id)
    if not user:
        raise BadRequest("пользователь не найден")
    if "AvatarSrc" in keys:
        user.AvatarSrc = data["AvatarSrc"]
    if "Date" in keys:
        user.Date = date(*map(int, data["Date"].split("-")))
    if "Status" in keys:
        user.Status= data["Status"]
    if "FavoriteJoke" in keys:
        user.FavoriteJoke= data["FavoriteJoke"]
    if "VkLink" in keys:
        user.VkLink = data["VkLink"]
    if "Telegram" in keys:
        user.Telegram = data["Telegram"]
    if "InstaLink" in keys:
        user.InstaLink= data["InstaLink"]
    user.save()
    return {"status":"ok","text":"ok"}