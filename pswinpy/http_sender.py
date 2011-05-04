
import httplib

class HttpSender(object):

  def __init__(self, host='http://gw2-fro.pswin.com:81/'):
    self.host = host

  def send(self, request):
    xml = request.xml()
    webservice = httplib.HTTP("gw2-fro.pswin.com:81")
    webservice.putrequest("POST", "/")
    webservice.putheader("Content-type", "text/xml; charset=\"UTF-8\"")
    webservice.putheader("Content-length", "%d" % len(xml))
    webservice.endheaders()
    webservice.send(xml)

    statuscode, statusmessage, header = webservice.getreply()
    print "Response: ", statuscode, statusmessage
    print "headers: ", header
    res = webservice.getfile().read()
    print res
    
    
