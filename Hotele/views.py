from django.shortcuts import render
from .models import Hotele, Uslugi, Standard, RezerwacjaHotelu
from django.db.models import Q

from rest_framework import viewsets
from .serializer import HoteleSerializer, StandardSerializer, UslugiSerializer, RezerwacjaHoteluSerializer

class HoteleViewSet(viewsets.ModelViewSet):
    queryset = Hotele.objects.all()
    serializer_class =  HoteleSerializer

class StandardViewSet(viewsets.ModelViewSet):
    queryset = Standard.objects.all()
    serializer_class = StandardSerializer

class UslugiViewSet(viewsets.ModelViewSet):
    queryset = Uslugi.objects.all()
    serializer_class = UslugiSerializer

class RezerwacjaHoteluViewSet(viewsets.ModelViewSet):
    queryset = RezerwacjaHotelu.objects.all()
    serializer_class = RezerwacjaHoteluSerializer

def home(request):
    uslugi_obiekty = Uslugi.objects.all()
    hotele_obiekty = Hotele.objects.all()
    sortuj = request.GET.get('sortuj')
    szukaj = request.GET.get('szukaj')
    uslugi = request.GET.getlist('uslugi')

    if sortuj:
        if sortuj == 'ASC':
            hotele_obiekty = hotele_obiekty.order_by('cena')
        elif sortuj == 'DSC':
            hotele_obiekty = hotele_obiekty.order_by('-cena')

    if szukaj:
        hotele_obiekty = hotele_obiekty.filter(
            Q(nazwa__icontains=szukaj) |
            Q(opis__icontains=szukaj ))

    # if len(uslugi):
    #     hotele_obiekty = hotele_obiekty.filter(uslugi__nazwa__in=uslugi)

    context = {'uslugi_obiekty':uslugi_obiekty,'hotele_obiekty':hotele_obiekty,
               'sortuj': sortuj, 'szukaj':szukaj, 'uslugi':uslugi}

    return render(request,'strona_glowna.html',context)
