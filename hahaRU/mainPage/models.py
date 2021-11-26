from django.db import models
from django.db.models.deletion import CASCADE
from django.core.validators import EmailValidator, validate_slug

# Create your models here.
class Articale(models.Model):
    title = models.CharField("name of title", max_length=200);
    text = models.TextField("text of title")
    date = models.DateTimeField();
    
    def __str__(self):
        return self.title

class Comment(models.Model):
    articale = models.ForeignKey(Articale, on_delete=models.CASCADE)
    autor = models.CharField(max_length=50)
    text = models.TextField()
    
    def __str__(self):
        return self.text

class Anecdot(models.Model):
    date = models.DateField(auto_now = True)
    text = models.TextField(max_length=1000, default="")
    videoSrc = models.CharField(max_length=100, default="")
    imgSrc = models.CharField(max_length=100, default="")
    likes = models.TextField(default='')
    disLikes = models.TextField(default='')
    likesCount = models.IntegerField(default=0)
    disLikesCount = models.IntegerField(default=0)
    def __str__(self):
        return self.text
class AnecdotEnd(models.Model):
    text = models.TextField(max_length=1000, default="")
    def __str__(self):
        return self.text
class AnecdotText(models.Model):
    text = models.TextField(max_length=1000, default="")
    def __str__(self):
        return self.text
class Config(models.Model):
    key = models.CharField(max_length=100, default="")
    value = models.CharField(max_length=100, default="")
    def __str__(self):
        return self.key
class FunnyWord(models.Model):
    date = models.DateField(auto_now = True)
    text = models.TextField(max_length=1000, default="")
    videoSrc = models.CharField(max_length=100, default="")
    imgSrc = models.CharField(max_length=100, default="")
    likes = models.TextField(default='')
    disLikes = models.TextField(default='')
    likesCount = models.IntegerField(default=0)
    disLikesCount = models.IntegerField(default=0)
    def __str__(self):
        return self.text
class Mem(models.Model):
    date = models.DateField(auto_now = True)
    text = models.TextField(max_length=1000, default="")
    videoSrc = models.CharField(max_length=100, default="")
    imgSrc = models.CharField(max_length=100, default="")
    likes = models.TextField(default='')
    disLikes = models.TextField(default='')
    likesCount = models.IntegerField(default=0)
    disLikesCount = models.IntegerField(default=0)
    def __str__(self):
        return self.text
class MemPicture(models.Model):
    imgSrc = models.CharField(max_length=100, default="")
    def __str__(self):
        return self.imgSrc
class MemText(models.Model):
    text = models.CharField(max_length=100, default="")
    def __str__(self):
        return self.text
class Post(models.Model):
    date = models.DateField(auto_now = True)
    text = models.TextField(max_length=1000, default="")
    videoSrc = models.CharField(max_length=100, default="")
    imgSrc = models.CharField(max_length=100, default="")
    likes = models.TextField(default='')
    disLikes = models.TextField(default='')
    likesCount = models.IntegerField(default=0)
    disLikesCount = models.IntegerField(default=0)
    userId = models.IntegerField(default=0)
    def __str__(self):
        return self.text
class Video(models.Model):
    date = models.DateField(auto_now = True)
    text = models.TextField(max_length=1000, default="")
    videoSrc = models.CharField(max_length=100, default="")
    imgSrc = models.CharField(max_length=100, default="")
    likes = models.TextField(default='')
    disLikes = models.TextField(default='')
    likesCount = models.IntegerField(default=0)
    disLikesCount = models.IntegerField(default=0)
    def __str__(self):
        return self.videoSrc
class videoSrc(models.Model):
    src = models.CharField(max_length=100, default="")
    def __str__(self):
        return self.src
class User(models.Model):
    Login = models.SlugField(max_length=20, error_messages={
        "blank":"логин не может быть пустым",
        "invalid":"логин должен состоять только из латинских букв, цифр, знаков подчеркивания или дефиса."
    })
    Password = models.CharField(max_length=100,error_messages={
        "blank":"пароль не может быть пустым"
    })
    Email = models.CharField(max_length=50, validators=[
        EmailValidator(message="не корректный email")
    ],error_messages={
        "blank":"пароль не может быть пустым"
    })
    Date = models.DateField(auto_now=True)
    AvatarSrc = models.CharField(max_length=256, default="/static/img/logo.png", blank=True)
    Status = models.CharField(max_length=100, default="", blank=True)
    FavoriteJoke = models.CharField(max_length=512, default="", blank=True)
    VkLink = models.CharField(max_length=100, default="", blank=True)
    Telegram = models.CharField(max_length=100, default="", blank=True)
    InstaLink = models.CharField(max_length=100, default="", blank=True)
    def __str__(self):
        return self.Login
