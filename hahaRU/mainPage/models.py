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

class User(models.Model):
    Login = models.CharField(max_length=20)
    Password = models.CharField(max_length=100)
    AvatarSrc = models.CharField(max_length=256)
    Date = models.DateField(auto_now=True)
    Email = models.CharField(max_length=50)
    Status = models.CharField(max_length=100)
    FavoriteJoke = models.CharField(max_length=512)
    VkLink = models.CharField(max_length=100)
    Telegram = models.CharField(max_length=100)
    InstaLink = models.CharField(max_length=100)
    def __init__(self,Login,Password,Email):
        self.Login = Login
        self.Password = Password
        self.AvatarSrc = "/img/logo.png"
        self.Date= today()
        self.Email = Email
        self.Status = "привет, я Фиксик"
        self.FavoriteJoke = "",
        self.VkLink = "",
        self.Telegram = "",
        self.InstaLink = ""
    def __str__(self):
        return self.Login