import unittest

from pswinpy import *

class ApiTests(unittest.TestCase):
  
  def testInitializer(self):
    API("user", "password")


class RequestTests(unittest.TestCase):  

  def testXmlWithNoMessages(self):
    r = Request("user", "password")
    self.assertEqual(r.xml(), 
        "<?xml version=\"1.0\"?>\r\n" + \
        "<SESSION><CLIENT>user</CLIENT><PW>password</PW><MSGLST></MSGLST></SESSION>")

  # TODO - Test single, minimum message
  #
  # "<?xml version=\"1.0\"?>\r\n" + \
  #      "<SESSION><CLIENT>Bob</CLIENT><PW>123</PW><MSGLST>" + \
  #      "<MSG><ID>1</ID><TEXT>A message</TEXT><RCV>12345678</RCV></MSG>" + \
  #      "</MSGLST></SESSION>"
  
  # TODO - Test single, complete message
  #
  # "<?xml version=\"1.0\"?>\r\n" + \
  #      "<SESSION><CLIENT>Bob</CLIENT><PW>123</PW><MSGLST>" + \
  #      "<MSG>" + \
  #      "<ID>1</ID><TEXT>A delayed message</TEXT><RCV>88888888</RCV>" + \
  #      "<SND>FooBar</SND><TTL>4</TTL><TARIFF>500</TARIFF><SERVICECODE>15001</SERVICECODE>" + \
  #      "<DELIVERYTIME>201102151330</DELIVERYTIME>" + \
  #      "</MSG>" + \
  #      "</MSGLST></SESSION>"
  
  # TODO - XML for multiple messages

class HttpSenderTests(unittest.TestCase):
  pass

if __name__ == '__main__':
  unittest.main()
