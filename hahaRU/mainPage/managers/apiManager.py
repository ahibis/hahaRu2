from typing import Match
from ..exeptions import AuthError, BadRequest
from ..models import *
from datetime import date
from random import randint
from django.core.files.storage import FileSystemStorage
import uuid

def objToJSON(data):
    json=data.__dict__
    del json['_state']
    return json

def objsToJSON(data):
    return list(map(objToJSON,data))

def getUser(id):
    user = User.objects.get(pk=id);
    if not user:
        raise BadRequest("user with this id doesn't defined")
    user.Password=""
    a=user.__dict__
    del a['_state']
    return a

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


def getContents(data):
    count = 20
    offset = 0
    keys = data.keys()
    if not "type" in keys:
        raise BadRequest("не указан type получаемых данных")
    if "count" in keys:
        count = int(data["count"])
    if "offset" in keys:
        offset = int(data["offset"])
    objs = []
    if data["type"]=="mem":
        objs = objsToJSON(Mem.objects.order_by("-likesCount").all()[offset:offset+count]) 
    elif data["type"]=="funnyWord":
        objs = objsToJSON(FunnyWord.objects.order_by("-likesCount").all()[offset:offset+count])
    elif data["type"]=="video":
        objs = objsToJSON(Video.objects.order_by("-likesCount").all()[offset:offset+count])
    else:
        objs = objsToJSON(Anecdot.objects.order_by("-likesCount").all()[offset:offset+count])
    return {"status":"ok","data":objs}

def getPosts(data):
    count = 20
    offset = 0
    keys = data.keys()
    if "count" in keys:
        count = int(data["count"])
    if "offset" in keys:
        offset = int(data["offset"])
    objs = []
    if not "userId" in keys:
        objs = objsToJSON(Post.objects.order_by("-likesCount").all()[offset:offset+count])
    else:
        objs = objsToJSON(Post.objects.filter(userId=data["userId"]).order_by("-id").all()[offset:offset+count])
    return {"status":"ok","data":objs}

def getRandomMemImg():
    count = MemPicture.objects.count();
    if not count:
        raise BadRequest("нет изображения")
    id = randint(1,count)
    obj = objToJSON(MemPicture.objects.get(pk=id))
    return {"status":"ok","value":obj}

def getRandomMemText():
    count = MemText.objects.count();
    if not count:
        raise BadRequest("нет Текстов")
    id = randint(1,count)
    obj = objToJSON(MemText.objects.get(pk=id))
    return {"status":"ok","value":obj}

def getRandomVideo():
    count = videoSrc.objects.count();
    if not count:
        raise BadRequest("нет видео")
    id = randint(1,count)
    obj = objToJSON(videoSrc.objects.get(pk=id))
    return {"status":"ok","value":obj}

def sendPost(data,id):
    keys = data.keys()
    if not "text" in keys:
        raise BadRequest("text не указан")
    if not data["text"]:
        raise BadRequest("text не может быть пустым")
    post = Post(text=data["text"],userId=id)
    post.save()
    return {"status":"ok","text":"ok"}

def sendAva(files,id):
    if not len(files):
        raise BadRequest("картинка не найдена")
    availableTypes = {"image/jpeg","image/jpg","image/png"}
    path = ""
    for i in files:
        file = files[i]
        if not file.content_type in availableTypes:
            raise BadRequest("поддерживаются аватарки только в jpg, jpeg, png формате")
        fs = FileSystemStorage()
        names = file.name.split(".");
        type = names[-1];
        name = str(uuid.uuid1())+"."+type;
        filename = fs.save("hahaRU/static/img/avaImgs/"+ name, file)
        user = User.objects.get(pk = id);
        path = "/static/img/avaImgs/"+name
        user.AvatarSrc = path;
        user.save()
    return {"status":"ok","value": path}

