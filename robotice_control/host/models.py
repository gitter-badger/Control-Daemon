from django.db import models

from django_extensions.db.fields.json import JSONField

from robotice_control.const import DEVICE_TYPE_CHOICES, CPU_ARCH_CHOICES, METRIC_TYPE_CHOICES


class Host(models.Model):

    hostname = models.CharField(u"hostname", max_length=255)
    cpu_arch = models.CharField(u"cpu arch", max_length=16, choices=CPU_ARCH_CHOICES, default="i386")

    class Meta:
        verbose_name = u"host"
        verbose_name_plural = u"hosts"

class RealDevice(models.Model):

    name = models.CharField(u"name", max_length=255)
    type = models.CharField(u"type", max_length=255, choices=DEVICE_TYPE_CHOICES, default="sensor")
    extra = JSONField(u"type", max_length=255, null=True, blank=True)
    host = models.ForeignKey(Host, verbose_name=u"host", related_name="devices")
    metric = models.CharField(u"metric", max_length=255, choices=METRIC_TYPE_CHOICES, default="dummy")


    class Meta:
        verbose_name = u"real device"
        verbose_name_plural = u"real devices"