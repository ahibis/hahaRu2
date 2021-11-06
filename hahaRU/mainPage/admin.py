from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(Articale)
admin.site.register(Comment)
admin.site.register(User)
admin.site.register(Anecdot)
admin.site.register(AnecdotEnd)
admin.site.register(AnecdotText)
admin.site.register(Post)
admin.site.register(Video)
admin.site.register(videoSrc)
admin.site.register(Mem)
admin.site.register(MemPicture)
admin.site.register(FunnyWord)