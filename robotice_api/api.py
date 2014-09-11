# -*- coding: utf-8 -*-

from collections import Counter
import errno
from functools import wraps
import logging
import os
import signal
import tempfile

from django.core.files import File
from django.db import transaction
from django.contrib.auth.models import User

from robotice_control.system.models import System

################################################################################
################################################################################


class RoboticeAPI(object):
    """
        API for comunication with Robotice
    """

    def __init__(self):
        self.logger = logging.getLogger("api")
        self.files = {}

    ###################################

    def ping(self):
        return "pong"

    def systems(self):

        return System.objects.all()