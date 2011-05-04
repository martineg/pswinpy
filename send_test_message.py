
from pswinpy import *

Mode.test = True
Mode.debug = True
HttpSender.host = "www.google.com"
api = API('tormar','xjQ4o0DNSY4qXfIF9pty')
api.sendSms(4790696698, "test from python 3")
