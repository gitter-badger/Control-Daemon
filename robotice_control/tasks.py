import datetime

from django.conf import settings

from celery import task

from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)

@task()
def sync_all():

	return "PING"