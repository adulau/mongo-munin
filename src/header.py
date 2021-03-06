
import urllib.request, urllib.error, urllib.parse
import sys
import os

try:
    import json
except ImportError:
    import simplejson as json


def getServerStatus():
    host = os.environ.get("host", "127.0.0.1")
    port = 28017
    url = "http://%s:%d/_status" % (host, port)
    req = urllib.request.Request(url)
    user = os.environ.get("user")
    password = os.environ.get("password")
    if user and password:
        passwdmngr = urllib.request.HTTPPasswordMgrWithDefaultRealm()
        passwdmngr.add_password(None, 'http://%s:%d' % (host, port), user, password)
        authhandler = urllib.request.HTTPDigestAuthHandler(passwdmngr)
        opener = urllib.request.build_opener(authhandler)
        urllib.request.install_opener(opener)
    raw = urllib.request.urlopen(req).read()
    return json.loads( raw.decode('utf-8') )["serverStatus"]
