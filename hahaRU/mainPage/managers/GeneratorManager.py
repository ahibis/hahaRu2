from typing import Text
from ..models import *
import random
def anecdotGen():
    count1 = AnecdotText.objects.count()
    count2 = AnecdotEnd.objects.count()
    if not count1 or not count2:
        return ""
    i1 = random.randint(1,count1)
    i2 = random.randint(1, count2)
    start=""
    end=""
    try:
        start = AnecdotText.objects.get(pk=i1)
        end = AnecdotEnd.objects.get(pk=i2)
        text = start.text +" "+ end.text
        anecdot = Anecdot(text = text)
        anecdot.save()
        return text
    except:
        return ""
        

def RandomString(length):
    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    return "".join([*map(lambda a:random.choice(chars),range(10))])

def GetURL1():
    count = 1
    API_KEY = "AIzaSyBVJ5iH6EhlQ7g_3XQlO4US_ytkbam1kOU";
    q = RandomString(4);
    url = "https://www.googleapis.com/youtube/v3/search?key=" + API_KEY + "&maxResults=" + count + "&part=snippet&type=video&q=" + q;
    url = "dQw4w9WgXcQ";
    return url;
def wordGen():
    i = random.randint(0, 399);
    bonus = [ "Похороны", "Абоба"];
    if (i == 0):
        return bonus[random.randint(0, 1)]
    s1 = [ "Д", "Б", "П" ]                              # s1 = [ "Д", "Б", "Х", "П" ]
    s = s1[random.randint(0, 2)];                            # s = s1[random.randint(0, 3)];
    s2 = [ "аб", "об", "уб", "ыб", "еб", "иб" ];
    s += s2[random.randint(0, 5)];
    A = [ s, "Пип", "Зелеб", "Еб", "Ебол", "Хеб", "Поп" ];
    s3 = A[random.randint(0, 5)];
    B = [ "y", "ы", "e", "o" ];
    s3 += B[random.randint(0, 3)];
    C = [ "лда", "га", "бa", "нгa", "ус" ];
    s3 += C[random.randint(0, 4)];
    return s3;  
              
def funnyWordGen():
    word = FunnyWord(text = wordGen())
    word.save()
    return word

