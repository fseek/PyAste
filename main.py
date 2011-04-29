#!/bin/env python2
from bottle import route, run,debug,request,response,static_file
from mako.template import Template
from mako.lookup import TemplateLookup
import os

import base64
import datetime
import cgi
import re,string
from hashlib import sha256

alphaNum = re.compile('[\W_]+')
def onlyAlphaNum(string):
    return alphaNum.sub('',string)


salt = """F(/ZvY#KVVb8sYkT1F+M}(K!)-QcgIv.9]d9GH\b._AAaVn<rk(mHH^xkCi"|ET"""

baseHash = sha256()
baseHash.update(salt)

    
@route('/new',method="POST")

if text == '' or text == 'Pasting time!':
	return

def newPaste():
    text = request.POST.get('text')
    lang = onlyAlphaNum(request.POST.get('lang','raw'))
    ip = request.header.get('X-Real-IP',request.get("REMOTE_ADDR"))

    #Hash
    h = baseHash.copy()
    h.update(ip)
    h.update(datetime.datetime.utcnow().isoformat())
    
    name = base64.urlsafe_b64encode(h.digest())[:-1]

    for i in range(0,42):
        if not os.path.exists("pastes/"+name[0:i]+".txt"):
            name = name[0:i]
            break
    

    #lets start with the raw file
    fileName = "pastes/"+name
    f = open(fileName+".txt",'w')
    f.write(text)
    f.close()

    out = templates.get_template("view-paste.tpl").render(code=text,lang=lang)
    f = open(fileName+".html",'w')
    f.write(out)
    f.close()
    return name


@route('/')
def serveIndex():
    return static_file("index.html",root="web/")

@route('/:path#.+#')
def serveStaticWeb(path):
    return static_file(path,root="web/")



if not os.path.exists("mako-cache"):
    os.makedirs("mako-cache")

if not os.path.exists("pastes"):
    os.makedirs("pastes")
    os.chmod("pastes",766)


templates = TemplateLookup(directories=['templates'],module_directory='mako-cache')


debug(True)
run(reloader=True)
