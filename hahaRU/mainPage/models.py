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
    date = models.DateField(default="")