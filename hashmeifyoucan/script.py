import requests
import hashlib
import webbrowser
def open_link(url):
    r = requests.get(url)
    return r.text

def isolate_message(html):
    begin_str = '----- BEGIN MESSAGE -----'
    end_str = '----- END MESSAGE -----'
    return html[ html.index(begin_str) + len(begin_str) + 6 : html.index(end_str) - 6].strip()[:-6]

def hash_string(str):
    hashed = hashlib.sha512(str.encode('utf-8'))
    return hashed.hexdigest()

def open_url(url, param):
    webbrowser.open("{}{}".format(url, param))

open_url('http://challenges.ringzer0team.com:10013/?r=', hash_string(isolate_message(open_link('http://challenges.ringzer0team.com:10013/'))))