
from rest_framework import serializers

from robotice_control.plan.models import ModelDevice

class ModelDeviceSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ModelDevice