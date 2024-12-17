from rest_framework import serializers
from .models import IceCream, IceCreamKiosk

class IceCreamSerializer(serializers.ModelSerializer):
    class Meta:
        model = IceCream
        fields = '__all__'

class IceCreamKioskSerializer(serializers.ModelSerializer):
    class Meta:
        model = IceCreamKiosk
        fields = '__all__'
