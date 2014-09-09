from django.db import models

from robotice_control.const import DEVICE_TYPE_CHOICES

class Plan(models.Model):

    name = models.CharField(u"name", max_length=255)
    description = models.TextField(u"description", max_length=255, blank=True)

    class Meta:
        verbose_name = u"plan"
        verbose_name_plural = u"plans"

class ModelDevice(models.Model):

    name = models.CharField(u"name", max_length=255)
    type = models.CharField(u"type", max_length=255, choices=DEVICE_TYPE_CHOICES, default="sensor")
    plan = models.ForeignKey(Plan, verbose_name=u"plan", related_name="devices")

    class Meta:
        verbose_name = u"model device"
        verbose_name_plural = u"model devices"

class Cycle(models.Model):

    name = models.CharField(u"name", max_length=255)
    description = models.TextField(u"description", max_length=255, blank=True)

    start = models.DateField(u"start", null=True, blank=True)
    end = models.DateField(u"end", null=True, blank=True)

    device = models.ForeignKey(ModelDevice, verbose_name=u"model_device", related_name="model_devices")

    class Meta:
        verbose_name = u"cycle"
        verbose_name_plural = u"cycles"


