# Generated by Django 4.1.6 on 2023-02-03 01:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Hotele', '0004_remove_hotele_usluga_delete_uslugi'),
    ]

    operations = [
        migrations.CreateModel(
            name='Standard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa', models.CharField(max_length=12)),
            ],
            options={
                'verbose_name': 'Standard hotelu',
                'verbose_name_plural': 'Standardy hoteli',
            },
        ),
        migrations.AddField(
            model_name='hotele',
            name='standard',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Hotele.standard'),
        ),
    ]