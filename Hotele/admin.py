from django.contrib import admin
from .models import Hotele, Standard, Uslugi, RezerwacjaHotelu
# Register your models here.
admin.site.register(Hotele)
admin.site.register(Standard)
admin.site.register(Uslugi)
admin.site.register(RezerwacjaHotelu)
