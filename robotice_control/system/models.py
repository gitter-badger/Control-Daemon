# -*- coding: utf-8 -*-

from django.db import models
from django.conf import settings
from django.forms.models import model_to_dict

from django.db import models

import yaml

from robotice_control.utils.models import RoboticeModelMixin

from robotice_control.plan.models import Plan, ModelDevice
from robotice_control.host.models import RealDevice

class Location(models.Model, RoboticeModelMixin):

    name = models.CharField(u"name", max_length=255)
    description = models.TextField(u"description", max_length=255, blank=True)


    def __unicode__(self):
        return self.name or ("Location - %s" % self.pk)

    class Meta:
        verbose_name = u"location"
        verbose_name_plural = u"locations"

class System(models.Model, RoboticeModelMixin):

    name = models.CharField(u"name", max_length=255)
    plan = models.ForeignKey(Plan, verbose_name=u"plan", related_name="plans")
    location = models.ForeignKey(Location, verbose_name=u"location", related_name="systems")

    @property
    def yaml(self):
        """return dictionary serialized into yaml
        """
        system = {}

        system["name"] = self.name

        system["plan"] = self.plan.to_yaml

        devices = []

        for device in self.devices.all():

            devices.append(serialized(device))

        system["devices"] = devices

        return system

    def __unicode__(self):
        return self.name or ("System - %s" % self.pk)

    class Meta:
        verbose_name = u"system"
        verbose_name_plural = u"systems"

class SystemDevice(models.Model, RoboticeModelMixin):

    name = models.CharField(u"name", max_length=255, blank=True, null=True)
    model_device = models.ForeignKey(ModelDevice, verbose_name=u"model_device", related_name="system_devices")
    real_device = models.ForeignKey(RealDevice, verbose_name=u"real_device", related_name="system_devices")
    system = models.ForeignKey(System, verbose_name=u"system", related_name="devices")

    @property
    def model_device_yaml(self):
        return self.model_device.to_yaml

    @property
    def real_device_yaml(self):
        return self.real_device.to_yaml

    @property
    def to_yaml(self):
        result = {}
        result["name"] = self.real_device.name
        try:
            result["devices"] = real_device.to_yaml
        except Exception, e:
            pass

        return yaml.safe_dump(result)

    def __unicode__(self):
        return self.name or ("System device - %s" % self.pk)

    class Meta:
        verbose_name = u"system device"
        verbose_name_plural = u"system devices"