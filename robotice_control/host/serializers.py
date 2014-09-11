
from rest_framework import serializers

from robotice_control.host.models import RealDevice

class RealDeviceSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = RealDevice