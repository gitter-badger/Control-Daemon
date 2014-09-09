# -*- coding: UTF-8 -*-

from django.contrib import admin, messages
from django.http import HttpResponseRedirect
from django.utils.html import mark_safe

from robotice_control.host.models import Host, RealDevice
from robotice_control.plan.models import Plan, ModelDevice
from robotice_control.system.models import System, SystemDevice

class RealDeviceInline(admin.TabularInline):
    model = RealDevice
    extra = 1
    suit_classes = 'suit-tab suit-tab-real-device'

class ModelDeviceInline(admin.TabularInline):
    model = ModelDevice
    extra = 1
    suit_classes = 'suit-tab suit-tab-model-device'

class SystemDeviceInline(admin.TabularInline):
    model = SystemDevice
    extra = 1
    suit_classes = 'suit-tab suit-tab-system-device'

class SystemAdmin(admin.ModelAdmin):

    list_display = ('name', )
    inlines = [SystemDeviceInline]

admin.site.register(System, SystemAdmin)

class HostAdmin(admin.ModelAdmin):

    list_display = ('hostname', )
    inlines = [RealDeviceInline]

admin.site.register(Host, HostAdmin)

class PlanAdmin(admin.ModelAdmin):

    list_display = ('name', )
    inlines = [ModelDeviceInline]

admin.site.register(Plan, PlanAdmin)
