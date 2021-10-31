from django.contrib import admin

# Register your models here.
from .models import Comment,Articale

admin.site.register(Articale)
admin.site.register(Comment)