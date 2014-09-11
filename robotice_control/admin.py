# -*- coding: UTF-8 -*-

from django.contrib import admin, messages
from django.http import HttpResponseRedirect
from django.utils.html import mark_safe

from robotice_control.host.models import Host, RealDevice
from robotice_control.plan.models import Plan, ModelDevice, Cycle
from robotice_control.system.models import System, SystemDevice, Location

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

class CycleInline(admin.TabularInline):
    model = SystemDevice
    extra = 1
    suit_classes = 'suit-tab suit-tab-system-cycle'

class SystemInline(admin.TabularInline):
    model = System
    extra = 1
    suit_classes = 'suit-tab suit-tab-system-inline'

class SystemAdmin(admin.ModelAdmin):

    list_display = ('name', )
    inlines = [SystemDeviceInline]

admin.site.register(System, SystemAdmin)

class CycleAdmin(admin.ModelAdmin):

    list_display = ('name', 'start', 'end', 'description' )

admin.site.register(Cycle, CycleAdmin)


class HostAdmin(admin.ModelAdmin):

    list_display = ('hostname', )
    inlines = [RealDeviceInline]

admin.site.register(Host, HostAdmin)

class LocationAdmin(admin.ModelAdmin):

    list_display = ('name', )
    inlines = [SystemInline]

admin.site.register(Location, LocationAdmin)


class PlanAdmin(admin.ModelAdmin):

    list_display = ('name', )
    inlines = [ModelDeviceInline]

admin.site.register(Plan, PlanAdmin)
