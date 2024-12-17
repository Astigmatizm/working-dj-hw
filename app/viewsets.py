from rest_framework import viewsets
from .models import IceCreamKiosk, IceCream
from .serializers import IceCreamKioskSerializer, IceCreamSerializer

class IceCreamKioskViewSet(viewsets.ModelViewSet):
    queryset = IceCreamKiosk.objects.all()
    serializer_class = IceCreamKioskSerializer

class IceCreamViewSet(viewsets.ModelViewSet):
    queryset = IceCream.objects.all()
    serializer_class = IceCreamSerializer
