import os
import re
from datetime import datetime, date, timedelta
import calendar
from logging import getLogger
import decimal
from django.db import models
from django.core import urlresolvers
from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

from django_extensions.db.fields.json import JSONField

from celery.execute import send_task
