from django.shortcuts import render
from rest_framework import viewsets
from .models import IceCream, IceCreamKiosk
from .serializers import IceCreamSerializer, IceCreamKioskSerializer
from django.http import HttpResponse


def get_string(request):
    html_content = """
        <html>
            <head>
                <title>String Response</title>
            </head>
            <body>
                <h1>эта строка была возвращена из фронтенда</h1>
            </body>
        </html>
        """
    return HttpResponse(html_content)


class IceCreamViewSet(viewsets.ModelViewSet):
    queryset = IceCream.objects.all()
    serializer_class = IceCreamSerializer


class IceCreamKioskViewSet(viewsets.ModelViewSet):
    queryset = IceCreamKiosk.objects.all()
    serializer_class = IceCreamKioskSerializer