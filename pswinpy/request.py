
class Request(object):
  
  def __init__(self, username, password):
    self.user = username
    self.password = password
    self.messages = []

  def addMessage(self, to, text):
    self.messages.append({'receiver': to, 'text': text})

  def xml(self):
    return "<?xml version=\"1.0\"?>\r\n" + \
           "<SESSION><CLIENT>%s</CLIENT><PW>%s</PW><MSGLST>%s</MSGLST></SESSION>" \
           % (self.user, self.password, self.messageListXml())

  def messageListXml(self):
    return reduce(lambda x, y: x + y, 
                  map(self.messageXml, self.messages), 
                  "")

  def messageXml(self, message):
    return "<MSG><ID>1</ID><TEXT>%s</TEXT><RCV>%s</RCV></MSG>" \
        % (message['text'], str(message['receiver']))
  
