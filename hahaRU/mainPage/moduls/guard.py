import html
import urllib.parse

def filter(str):
    return urllib.parse.quote_plus(html.escape(str))