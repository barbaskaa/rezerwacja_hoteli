from .models import Hotele, RezerwacjaHotelu, Standard, Uslugi
from rest_framework import serializers

class HoteleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotele
        fields = ['nazwa','opis','cena','standard','usluga']

class StandardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Standard
        fields = ['nazwa']

class UslugiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Uslugi
        fields = ['nazwa']

class RezerwacjaHoteluSerializer(serializers.ModelSerializer):
    class Meta:
        model = RezerwacjaHotelu
        fields = ['hotel', 'uzytkownik', 'zameldowanie', 'wymeldowanie', 'rodzaj_platnosci']