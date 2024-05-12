# signals.py
import sys
from datetime import datetime

from _decimal import Decimal
from django.db import IntegrityError
from django.db.models import Q, Count, F
from django.db.models.signals import post_save, pre_save, post_delete, pre_delete
from django.dispatch import *
from num2words import num2words
from safedelete.signals import post_softdelete, pre_softdelete
from simple_history import register
from simple_history.signals import pre_create_historical_record
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


# DQE

@receiver(pre_save, sender=DQE)
def pre_save_dqe(sender, instance, **kwargs):
    if not instance.pk:
        instance.id = str(instance.code_tache) + "_" + str(instance.marche.id)

    instance.libelle = instance.libelle.lower()



"""
@receiver(pre_create_historical_record,sender=Marche)
def pre_create_historical_record_callback(sender, **kwargs):
    instance = kwargs['instance']
    sender_model_name = sender.__name__
    if(sender_model_name == "HistoricalMarche"):
        try:
            latest_history_record = instance.history.latest()
            print(latest_history_record.date_signature,instance.date_signature)
            if latest_history_record.date_signature == instance.date_signature:
                raise IntegrityError("Data is already present in the historical records.")
            else:
                print(instance.history.num_avenant)
        except Marche.history.model.DoesNotExist:
            pass
    else:
        pass
"""


@receiver(pre_save, sender=Attachements)
def pre_save_attachement(sender, instance, **kwargs):
    dqe=DQE.objects.get(nt=instance.nt,code_site=instance.code_site,code_tache=instance.code_tache)
    instance.prix_u=dqe.prix_u
    instance.montant=float(instance.qte)*float(instance.prix_u)





@receiver(pre_save, sender=Factures)
def pre_save_factures(sender, instance, **kwargs):
    if (instance.du > instance.au):
        raise ValidationError('Date de debut doit etre inferieur à la date de fin')
    else:
        debut = instance.du
        fin = instance.au
        if( not Attachements.objects.filter(dqe__marche=instance.marche, date__lte=fin, date__gte=debut)):
            raise ValidationError('Facturation impossible les attachements ne sont pas disponible ')
        m=0
        attachements=Attachements.objects.filter(dqe__marche=instance.marche, date__lte=fin, date__gte=debut)
        for attachement in attachements:
            m+=attachement.montant

        instance.montant = m
        instance.montant_rb = m * (instance.marche.rabais / 100)
        instance.montant_rg = round((m - instance.montant_rb) * (instance.marche.rg / 100), 2)

        qte_real = Attachements.objects.filter(Q(marche=instance.marche) & Q(date__lte=fin)).aggregate(
                models.Sum('qte'))["qte__sum"]
        qte_dqe = DQE.objects.filter(Q(marche=instance.marche)).aggregate(
                models.Sum('quantite'))["quantite__sum"]
        instance.taux_realise = round((qte_real / qte_dqe) * 100, 2)





@receiver(pre_save,  sender=Encaissement)
def pre_save_encaissement(sender, instance, **kwargs):
    if not instance.pk:
        try:

            sum = Encaissement.objects.filter(facture=instance.facture, date_encaissement__lt=instance.date_encaissement).aggregate(models.Sum('montant_encaisse'))[
                        "montant_encaisse__sum"]

        except Encaissement.DoesNotExist:
                pass

        if(not sum):
            sum=0
        sum=sum+instance.montant_encaisse
        montant_creance=instance.facture.montant_factureTTC-sum
        if(instance.montant_creance == 0):
            instance.facture.paye=True
            instance.facture.save()
        if(instance.montant_creance < 0):
            raise ValidationError('Le paiement de la facture est terminer')

@receiver(post_softdelete, sender=Encaissement)
def update_on_softdelete(sender, instance, **kwargs):
    try:
        encaissements=Encaissement.objects.filter(Q(id__gt=instance.id))
        if(encaissements):
            encaissements.update(montant_creance=F('montant_creance') + instance.montant_encaisse)

    except Encaissement.DoesNotExist:
        pass


@receiver(pre_save, sender=Remboursement)
def pre_save_remboursement(sender, instance, **kwargs):
    if (instance.avance.remboursee):
            raise ValidationError('Cette avance est remboursée')
    else:
        tremb = round(
                (instance.avance.taux_avance / (instance.avance.fin - instance.facture.taux_realise)) * 100, 2)
        instance.montant = instance.facture.montant_factureHT * (tremb / 100)

        if (instance.rst_remb < 0):
            instance.montant = instance.avance.montant
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
            DetailFacture(
                facture=instance,
                detail=d
            ).save()





@receiver(pre_save, sender=DetailFacture)
def pre_save_detail_facture(sender, instance, **kwargs):
    if (instance.detail.dqe.marche != instance.facture.marche):
        raise ValidationError("Cette attachement ne fais pas partie du marche")


@receiver(pre_save, sender=Avance)
def pre_save_avance(sender, instance, **kwargs):
    if not instance.pk:
        try:
            instance.taux_avance = round((float(instance.montant) / float(instance.marche.ttc))*100)
        except Exception as e :
            instance.taux_avance = 0
        instance.num_avance = Avance.objects.filter(marche=instance.marche).count()









@receiver(pre_save, sender=TypeCaution)
def pre_save_type_caution(sender, instance, **kwargs):
    if (instance.type_avance):
        instance.libelle = instance.type_avance.libelle


@receiver(pre_save, sender=Cautions)
def pre_save_caution(sender, instance, **kwargs):
    if (instance.avance):
        if (instance.avance.marche != instance.marche):
            raise ValidationError(
                f'Le Marché {instance.marche} ne posséde pas cette avance  de type {instance.avance.type}')
        else:
            if (instance.avance.type != instance.type.type_avance):
                raise ValidationError(
                    f'Cette avance est de type {instance.avance.type} n\'est pas compatible avec la caution de type {instance.type.type_avance} ')

    exact = instance.type.taux_exact
    max = instance.type.taux_max
    min = instance.type.taux_min
    if (exact != None):
        if (instance.taux != exact):
            raise ValidationError(
                f'le taux de la caution du marché  {instance.taux} doit etre égale à {exact}')

        if (min != None and max != None):
            if (not min <= instance.taux <= max):
                raise ValidationError(
                    f'le taux de la caution du marché  {instance.taux}  doit etre comprise entre [{min},{max}]')

    montant = 0
    if (instance.avance):
        montant = instance.avance.montant
    else:
        montant = instance.marche.ttc

    instance.montant = round(montant * instance.taux / 100, 2)




