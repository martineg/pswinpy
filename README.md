PSWinCom Python Package
=======================

A Python interface to the [PSWinCom SMS Gateway](http://pswin.com/english/products/gateway).

Project Status
--------------

This project is in its infancy! Fork it if you want to help out.

Installation
------------

The pswinpy package is distributed through PyPI as both egg, Windows and source. (TODO: add more info)

Basic Usage
-----------
To use this package, you will need sign up for a Gateway account with PSWinCom. Demo account are available.

This piece of code demonstrates how to send a simple SMS message:

    TODO

You can also send multiple messages in a single request, like this:

    TODO

Properties
----------
Receiver and message text are the two mandatory properties when sending a message. You may specify additional properties by .....

For instance this is how you would specify a sender:

    TODO

Properties currently supported are:

* TODO

Specifying Host
---------------
The package is set to use a particular PSWinCom SMS Gateway by default. The host can be changed globaly by setting api_host:

    TODO

License
-------
This code is free to use under the terms of the MIT license.

