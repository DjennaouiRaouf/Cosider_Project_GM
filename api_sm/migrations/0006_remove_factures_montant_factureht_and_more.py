# Generated by Django 4.2.7 on 2024-04-23 09:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api_sm', '0005_remove_factures_montant_ava_remb_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='factures',
            name='montant_factureHT',
        ),
        migrations.RemoveField(
            model_name='factures',
            name='montant_factureTTC',
        ),
    ]