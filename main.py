#!/bin/env python2
from bottle import route, run,debug,request,response
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


    f = open(fileName+".html",'w')
    f.write("""<!DOCTYPE html><html><head><title>Viewing Paste</title><script src="/head.js"></script><body><div class="src highlight-{0}"><code>""".format(lang))
    f.write(cgi.escape(text))
    f.write("""</code></div><script type="text/javascrpt">head.js("http://ajax.googleapis.com/ajax/libs/jquery/1.5.0/jquery.min.js","chili.js","m.js",function(){renderPaste();})</script></body></html>""")
    f.close()
    return name


if not os.path.exists("pastes"):
    os.makedirs("pastes")
    os.chmod("pastes",766)


debug(True)
run(reloader=True)
