import datetime
import socket
from django.conf import settings

from celery import task

from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)

@task(name='control.sync_config')
def sync_confi():

    return "PING"

@task(name='control.keep_alive')
def keep_alive():

    return "ALIVE from %s" % socket.getfqdn()