from django.core.cache import cache
from django.http import HttpResponse
from django.views import generic
from django.views.decorators.csrf import csrf_exempt

from rest_framework.decorators import api_view
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

from robotice_control.system.serializers import serialized

from robotice_control.system.models import System, Location


class JSONResponse(HttpResponse):

    """
    An HttpResponse that renders its content into JSON.
    """

    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


class BaseApiView(generic.View):

    """
    base view for plain API
    """

    def yaml(self, location):
        """return dictionary serialized into yaml
        """

        result = []

        for system in location.systems.all():
            _system = {}

            _system["name"] = system.name

            _system["plan"] = system.plan.to_yaml

            devices = []
            for device in system.devices.all():

                devices.append(device.to_yaml)

            _system["devices"] = devices

            result.append(_system)
        return result

    def get(self, request, *args, **kwargs):
        """
        result_list = []


        for location in Location.objects.all():
            result_list.append(self.yaml(location))
        """

        from robotice_client.client import robotice_client

        try:
            sensors = robotice_client.api.sensors()
        except Exception, e:
            pass

        uuid = robotice_client.api.uuid()

        return JSONResponse(uuid)
