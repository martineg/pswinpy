from pswinpy.request import Request

class API(object):
  
  def __init__(self, username, password):
    self.request = Request(username, password)

  def sendSms(self, to=None, text=None, args=None):
    pass

  def addSMS(self, to, text, args=None):
    pass
