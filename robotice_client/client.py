#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import Pyro4

from uuid import uuid4

try:
    from django.conf import settings
    HMAC_KEY = getattr(settings, "HMAC_KEY")
    URI_ID = getattr(settings, "URI_ID")
    SERVER_IP = getattr(settings, "SERVER_IP")
    URI_PORT = getattr(settings, "URI_PORT")
except ImportError:
    raise e
    # SERVER_IP = '192.168.23.68'
    # NS_BCHOST = "localhost"


################################################################################


#

Pyro4.config.HMAC_KEY = HMAC_KEY
Pyro4.config.HOST = SERVER_IP

################################################################################


class RoboticeClient(object):
    """
        DocumentAPI client
    """

    def __init__(self):
        """
        connect to remote document-parser server
        """
        self.uri = "PYRO:%s@%s:%s" % (URI_ID, SERVER_IP, URI_PORT)

        try:
            self.api = Pyro4.Proxy(self.uri)
        except Exception, e:
            raise e

robotice_client = RoboticeClient()