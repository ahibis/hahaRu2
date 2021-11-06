from django.db import models
from django.db.models.deletion import CASCADE

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
class AnecdotTexts(models.Model):
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
class MemPictures(models.Model):
    imgSrc = models.CharField(max_length=100, default="")
    def __str__(self):
        return self.imgSrc
class Post(models.Model):
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
    Login = models.CharField(max_length=20, default="")
    Password = models.CharField(max_length=100, default="")
    AvatarSrc = models.CharField(max_length=256, default="")
    Date = models.DateField(auto_now=True)
    Email = models.CharField(max_length=50, default="")
    Status = models.CharField(max_length=100, default="")
    FavoriteJoke = models.CharField(max_length=512, default="")
    VkLink = models.CharField(max_length=100, default="")
    Telegram = models.CharField(max_length=100, default="")
    InstaLink = models.CharField(max_length=100, default="")
    def __str__(self):
        return self.Login
