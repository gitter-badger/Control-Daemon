from django.db import models

from robotice_control.const import DEVICE_TYPE_CHOICES

from robotice_control.utils.models import RoboticeModelMixin

class Plan(models.Model, RoboticeModelMixin):

    name = models.CharField(u"name", max_length=255)
    description = models.TextField(u"description", max_length=255, blank=True)

    def __unicode__(self):
        return self.name or ("Plan - %s" % self.pk)

    class Meta:
        verbose_name = u"plan"
        verbose_name_plural = u"plans"

class ModelDevice(models.Model, RoboticeModelMixin):

    name = models.CharField(u"name", max_length=255)
    type = models.CharField(u"type", max_length=255, choices=DEVICE_TYPE_CHOICES, default="sensor")
    plan = models.ForeignKey(Plan, verbose_name=u"plan", related_name="devices")
    plan = models.ForeignKey(Plan, verbose_name=u"plan", related_name="devices")

    def __unicode__(self):
        return self.name or ("Model device - %s" % self.pk)

    class Meta:
        verbose_name = u"model device"
        verbose_name_plural = u"model devices"

class Cycle(models.Model, RoboticeModelMixin):

    name = models.CharField(u"name", max_length=255)
    description = models.TextField(u"description", max_length=255, blank=True)

    start = models.DateField(u"start", null=True, blank=True)
    end = models.DateField(u"end", null=True, blank=True)

    device = models.ForeignKey(ModelDevice, verbose_name=u"model_device", related_name="cycles")

    def __unicode__(self):
        return self.name or ("Cycle - %s" % self.pk)

    class Meta:
        verbose_name = u"cycle"
        verbose_name_plural = u"cycles"


