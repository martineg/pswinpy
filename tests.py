import unittest

from pswinpy import *
from datetime import datetime

class ApiTests(unittest.TestCase):
  
  def testInitializer(self):
    API("user", "password")


class RequestTests(unittest.TestCase):  

  def testXmlWithNoMessages(self):
    r = Request("user", "password")
    self.assertEqual(r.xml(), 
        "<?xml version=\"1.0\"?>\r\n" + \
        "<SESSION><CLIENT>user</CLIENT><PW>password</PW><MSGLST></MSGLST></SESSION>")

  def testXmlWithMinimumMessage(self):
    r = Request("tom", "tomspasswd")
    r.addMessage(12345678, "A simple message")
    self.assertEqual(r.xml(), 
        "<?xml version=\"1.0\"?>\r\n" + \
        "<SESSION><CLIENT>tom</CLIENT><PW>tomspasswd</PW><MSGLST>" + \
        "<MSG><ID>1</ID><TEXT>A simple message</TEXT><RCV>12345678</RCV></MSG>" + \
        "</MSGLST></SESSION>")

  def testXmlWithCompleteMessage(self):
    r = Request("tom", "tomspasswd")
    r.addMessage(12345678, "A simple message", sender="Foo", TTL=4, tariff=500, serviceCode=15001, 
        deliveryTime=datetime(2011, 2, 15, 13, 30))
    self.assertEqual(r.xml(), 
        "<?xml version=\"1.0\"?>\r\n" + \
        "<SESSION><CLIENT>tom</CLIENT><PW>tomspasswd</PW><MSGLST>" + \
        "<MSG>" + \
        "<ID>1</ID><TEXT>A simple message</TEXT><RCV>12345678</RCV>" + \
        "<SND>Foo</SND><TTL>4</TTL><TARIFF>500</TARIFF><SERVICECODE>15001</SERVICECODE>" + \
        "<DELIVERYTIME>201102151330</DELIVERYTIME>" + \
        "</MSG>" + \
        "</MSGLST></SESSION>")

  # TODO - XML for multiple messages

class HttpSenderTests(unittest.TestCase):
  pass

if __name__ == '__main__':
  unittest.main()
