from django.shortcuts import render
from rest_framework import viewsets
from .models import IceCream, IceCreamKiosk
from .serializers import IceCreamSerializer, IceCreamKioskSerializer

class IceCreamViewSet(viewsets.ModelViewSet):
    queryset = IceCream.objects.all()
    serializer_class = IceCreamSerializer

class IceCreamKioskViewSet(viewsets.ModelViewSet):
    queryset = IceCreamKiosk.objects.all()
    serializer_class = IceCreamKioskSerializer