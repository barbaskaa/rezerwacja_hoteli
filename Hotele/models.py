from django.db import models
from django.contrib.auth.models import User

class Standard(models.Model):
    nazwa = models.CharField(max_length=12)
    def __str__(self):
        return self.nazwa

    class Meta:
        verbose_name = "Standard hotelu"
        verbose_name_plural = "Standardy hoteli"

class Uslugi(models.Model):
    nazwa = models.CharField(max_length=100)
    class Meta:
        verbose_name = "Usługa hotelowa"
        verbose_name_plural = "Usługi hotelowe"

    def __str__(self):
        return self.nazwa

class Hotele(models.Model):
    nazwa = models.CharField(max_length=100)
    opis = models.TextField(blank=True)
    cena = models.DecimalField(max_digits=12, decimal_places=2)
    standard = models.ForeignKey(Standard, on_delete=models.CASCADE, null = True)
    usluga = models.ManyToManyField(Uslugi)

    def __str__(self):
        return self.nazwa

    class Meta:
        verbose_name="Hotel"
        verbose_name_plural="Hotele"

class RezerwacjaHotelu(models.Model):
    hotel = models.ForeignKey(Hotele, on_delete=models.CASCADE)
    uzytkownik = models.ForeignKey(User, on_delete=models.CASCADE)
    zameldowanie = models.DateField()
    wymeldowanie = models.DateField()
    rodzaj_platnosci = models.CharField(max_length=100,choices=(("karta","karta"),("gotówka","gotówka"),("przelew","przelew"),("BLIK","BLIK")))



    class Meta:
        verbose_name="Rezerwacja"
        verbose_name_plural="Rezerwacje"

    def __str__(self):

        return "Rezerwacja hotelu {} na użytkownika: {}".format(self.hotel, self.uzytkownik)

