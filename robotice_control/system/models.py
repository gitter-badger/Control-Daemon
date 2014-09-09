# -*- coding: utf-8 -*-

from django.db import models
from django.conf import settings

from django.db import models

from robotice_control.plan.models import Plan, ModelDevice
from robotice_control.host.models import RealDevice


class System(models.Model):

    name = models.CharField(u"name", max_length=255)
    plan = models.ForeignKey(Plan, verbose_name=u"plan", related_name="plans")

    class Meta:
        verbose_name = u"system"
        verbose_name_plural = u"systems"

class SystemDevice(models.Model):

    name = models.CharField(u"name", max_length=255, blank=True, null=True)
    model_device = models.ForeignKey(ModelDevice, verbose_name=u"model_device", related_name="system_devices")
    real_device = models.ForeignKey(RealDevice, verbose_name=u"real_device", related_name="system_devices")
    system = models.ForeignKey(System, verbose_name=u"system", related_name="devices")

    def __unicode__(self):
        return self.name or ("System device - %s" % self.pk)

    class Meta:
        verbose_name = u"system device"
        verbose_name_plural = u"system devices"