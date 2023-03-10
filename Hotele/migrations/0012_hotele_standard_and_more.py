# Generated by Django 4.1.6 on 2023-02-04 14:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Hotele', '0011_rename_platnosc_rezerwacjahotelu_rodzaj_platnosci'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotele',
            name='standard',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Hotele.standard'),
        ),
        migrations.AlterField(
            model_name='rezerwacjahotelu',
            name='rodzaj_platnosci',
            field=models.CharField(choices=[('karta', 'karta'), ('gotówka', 'gotówka'), ('przelew', 'przelew'), ('BLIK', 'BLIK')], max_length=100),
        ),
    ]
