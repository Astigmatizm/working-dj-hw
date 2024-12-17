from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import IceCreamViewSet, IceCreamKioskViewSet

router = DefaultRouter()
router.register(r'icecream', IceCreamViewSet)
router.register(r'kiosk', IceCreamKioskViewSet)

urlpatterns = [
    path('api/', include(router.urls)),  # Подключаем маршруты, сгенерированные маршрутизатором
]
