from pswinpy import *

Mode.test = True
Mode.debug = True
HttpSender.host = "www.google.com"
api = API('****','****')
api.sendSms(4700000000, "test from python 3")
