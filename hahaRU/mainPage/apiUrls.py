from django.urls import path
from . import apis 
from django.views.generic import View

patterns = []

for el in apis.__dict__.items():
    key = el[0]
    value = el[1]
    if key == "View":
        continue
    if not "as_view" in dir(value):
        continue
    patterns.append(path(key[0].lower() + key[1:], value.as_view()))

urlpatterns = patterns
