
class Request(object):
  
  def __init__(self, username, password):
    self.user = username
    self.password = password

  def xml(self):
    return "<?xml version=\"1.0\"?>\r\n" + \
           "<SESSION><CLIENT>%s</CLIENT><PW>%s</PW><MSGLST></MSGLST></SESSION>" \
           % (self.user, self.password)

  
