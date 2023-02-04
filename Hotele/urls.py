from .views import *
from django.contrib import admin
from rest_framework import routers
from .views import HoteleViewSet, UslugiViewSet, StandardViewSet, RezerwacjaHoteluViewSet
from django.urls import include, path

router = routers.DefaultRouter()
router.register(r'hotele',HoteleViewSet)
router.register(r'uslugi', UslugiViewSet)
router.register(r'standard',StandardViewSet)
router.register(r'rezerwacja', RezerwacjaHoteluViewSet)

urlpatterns = [
   # path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    path('', home , name='home'),


]
