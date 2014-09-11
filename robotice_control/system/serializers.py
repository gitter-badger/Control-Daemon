
from rest_framework import serializers

from robotice_control.host.serializers import RealDeviceSerializer
from robotice_control.plan.serializers import ModelDeviceSerializer

from robotice_control.system.models import SystemDevice

class SystemDeviceSerializer(serializers.ModelSerializer):
    
    model_device = ModelDeviceSerializer
    real_device = RealDeviceSerializer

    class Meta:
        model = SystemDevice


def serialized(device):
    data = SystemDeviceSerializer(device).data
    return device.data_to_yaml(data)