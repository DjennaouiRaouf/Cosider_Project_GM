# signals.py
import sys
from datetime import datetime

from _decimal import Decimal
from django.db import IntegrityError
from django.db.models import Q, Count, F
from django.db.models.signals import post_save, pre_save, post_delete, pre_delete
from django.dispatch import *
from num2words import num2words
from .models import *


# NT
@receiver(pre_save, sender=NT)
def pre_save_nt(sender, instance, **kwargs):
    if (instance.date_cloture_nt and instance.date_ouverture_nt):
        if (instance.date_cloture_nt <= instance.date_ouverture_nt):
            raise ValidationError("Date de cloture doit etre supérieur ou égale à la date d\'ouverture")



@receiver(post_save, sender=NT)
def post_save_nt(sender, instance, created, **kwargs):
    if created:
        if (instance.date_cloture_nt and instance.date_ouverture_nt):
            if (instance.date_cloture_nt <= instance.date_ouverture_nt):
                raise ValidationError("Date de cloture doit etre supérieur ou égale à la date d\'ouverture")

    if not created:
        if (instance.date_cloture_nt and instance.date_ouverture_nt):
            if (instance.date_cloture_nt <= instance.date_ouverture_nt):
                raise ValidationError("Date de cloture doit etre supérieur ou égale à la date d\'ouverture")


@receiver(pre_save, sender=Attachements)
def pre_save_attachement(sender, instance, **kwargs):

    instance.id=Attachements.objects.filter(marche=instance.marche).count()
    dqe=DQE.objects.get(nt=instance.nt,code_site=instance.code_site,code_tache=instance.code_tache)
    instance.prix_u=dqe.prix_u




@receiver(pre_save, sender=Factures)
def pre_save_factures(sender, instance, **kwargs):
    if (instance.du > instance.au):
        raise ValidationError('Date de debut doit etre inferieur à la date de fin')
    else:
        debut = instance.du
        fin = instance.au
        if( not Attachements.objects.filter(marche=instance.marche, date__lte=fin, date__gte=debut,est_bloquer=False)):
            raise ValidationError('Facturation impossible les attachements ne sont pas disponible ')
        m=0
        attachements=Attachements.objects.filter(marche=instance.marche, date__lte=fin, date__gte=debut,est_bloquer=False)
        for attachement in attachements:
            m += attachement.montant




        instance.montant = m
        instance.montant_rb = m * (instance.marche.rabais / 100)
        instance.montant_rg = round((m - instance.montant_rb) * (instance.marche.rg / 100), 2)




@receiver(pre_save,  sender=Encaissement)
def pre_save_encaissement(sender, instance, **kwargs):
    if not instance.pk:
        try:

            sum = Encaissement.objects.filter(facture=instance.facture, date_encaissement__lt=instance.date_encaissement,est_bloquer=False).aggregate(models.Sum('montant_encaisse'))[
                        "montant_encaisse__sum"]

        except Encaissement.DoesNotExist:
                pass

        if(not sum):
            sum=0
        sum=sum+instance.montant_encaisse
        if(instance.montant_creance == 0):
            instance.facture.paye=True
            instance.facture.save()
        if(instance.montant_creance < 0):
            raise ValidationError('Le paiement de la facture est terminer')


@receiver(pre_save, sender=Remboursement)
def pre_save_remboursement(sender, instance, **kwargs):
    tr=round(instance.facture.montant_cumule/instance.facture.marche.ht,2)
    print(tr)
    print(instance.avance.debut)
    if (instance.avance.remboursee):
            raise ValidationError('Cette avance est remboursée')
    elif (instance.avance.debut>=tr):
        print(tr)
        print(instance.avance.debut)
    else:
        montant = (instance.facture.montant - instance.facture.montant_rb - instance.facture.montant_rg - instance.facture.montant_ava_remb - instance.facture.montant_avf_remb - instance.facture.montant_ave_remb) * (
                                       instance.avance.taux_remb / 100)

        previous_cumule =0
        previous_restant =0
        try:
            previous_remboursement=Remboursement.objects.filter(facture__marche=instance.facture.marche,avance=instance.avance, facture__num_situation__lt=instance.facture.num_situation).last()
            previous_cumule=previous_remboursement.montant_cumule
            previous_restant=previous_remboursement.rst_remb
        except Remboursement.DoesNotExist:
            previous_restant =0
            previous_cumule = 0

        previous_cumule += montant
        previous_restant = instance.avance.montant-previous_cumule
        if(previous_restant< 0):
            instance.montant=previous_remboursement.rst_remb

        if (instance.rst_remb == 0):
            instance.avance.remboursee = True
            instance.avance.save()




@receiver(pre_save, sender=ModePaiement)
def pre_save_mp(sender, instance, **kwargs):
    instance.libelle = instance.libelle.lower()


@receiver(post_save, sender=Factures)
def post_save_facture(sender, instance, created, **kwargs):
    if created:
        debut = instance.du
        fin = instance.au
        details = Attachements.objects.filter(marche=instance.marche, date__lte=fin, date__gte=debut)
        for d in details:
            if(d.est_bloquer == False):
                DetailFacture(
                    facture=instance,
                    detail=d
                ).save()







@receiver(pre_save, sender=Avance)
def pre_save_avance(sender, instance, **kwargs):

    if not instance.pk:
        instance.id = (instance.type.id) + str(Avance.objects.filter(marche=instance.marche).count())
        instance.num_avance = Avance.objects.filter(marche=instance.marche).count()









@receiver(pre_save, sender=TypeCaution)
def pre_save_type_caution(sender, instance, **kwargs):
    if (instance.type_avance):
        instance.libelle = instance.type_avance.libelle





