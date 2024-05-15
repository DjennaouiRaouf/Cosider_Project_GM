from datetime import datetime
from cpkmodel import CPkModel
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models import Q
from django_currentuser.middleware import get_current_user
from api_sch.models import *


class Clients(models.Model):
    id =models.CharField(db_column='Code_Client', primary_key=True,
                                   max_length=20,verbose_name="Code Client")
    type_client = models.SmallIntegerField(db_column='Type_Client', blank=True, null=True,verbose_name="Type Client")  
    est_client_cosider = models.BooleanField(db_column='Est_Client_Cosider', blank=True,
                                             null=True,verbose_name="Est Client Cosider ?")  
    libelle = models.CharField(db_column='Libelle_Client', max_length=300, blank=True,
                                      null=True,verbose_name="Libelle")  
    nif = models.CharField(db_column='NIF', unique=True, max_length=50, blank=True,
                           null=True,verbose_name="NIF")  
    raison_social = models.CharField(db_column='Raison_Social', max_length=50, blank=True,
                                     null=True,verbose_name="Raison social")  
    num_registre_commerce = models.CharField(db_column='Num_Registre_Commerce', max_length=20, blank=True,
                                             null=True,verbose_name="N° Registre Commerce")


    est_bloquer = models.BooleanField(db_column='Est_Bloquer', default=False,
                                      editable=False)
    user_id = models.CharField(db_column='User_ID', max_length=15, editable=False,default=get_current_user)
    date_modification = models.DateTimeField(db_column='Date_Modification', auto_now=True)


    def __str__(self):
        return  self.id

    class Meta:
        managed=False
        db_table = 'Tab_Client'
        verbose_name = 'Clients'
        verbose_name_plural = 'Clients'



class Sites(models.Model):
    RG=(
        ('',''),
        ('N','Nord'),
         ('S','Sud'),
          ('W','West'),
           ('E','Est'),
            ('C','Centre'),
    )
    id = models.CharField(db_column='Code_site', primary_key=True, max_length=10 ,
                                 verbose_name='Code du Site')
    code_filiale = models.ForeignKey(TabFiliale, models.DO_NOTHING,
                                     db_column='Code_Filiale',verbose_name='Code Filiale')
    code_region = models.CharField(db_column='Code_Region', max_length=1, blank=True,
                                   null=True,verbose_name='Région',choices=RG)
    libelle = models.CharField(db_column='Libelle_Site', max_length=150, blank=True,
                                    null=True,verbose_name='Libellé')
    code_agence = models.ForeignKey(TabAgence, models.DO_NOTHING, db_column='Code_Agence', blank=True,
                                    null=True,verbose_name='Code Agence')
    type_site = models.SmallIntegerField(db_column='Type_Site', blank=True, null=True,verbose_name='Type du Site')
    code_division = models.ForeignKey(TabDivision, models.DO_NOTHING, db_column='Code_Division', blank=True,
                                      null=True,verbose_name='Code Division')
    code_commune_site = models.CharField(db_column='Code_Commune_Site', max_length=10, blank=True,
                                         null=True,verbose_name='Code Commune')
    jour_cloture_mouv_rh_paie = models.CharField(db_column='Jour_Cloture_Mouv_RH_Paie', max_length=2, blank=True,
                                                 null=True)  
    date_ouverture_site = models.DateField(db_column='Date_Ouverture_Site', blank=True,
                                           null=True,verbose_name='Date Ouverture')
    date_cloture_site = models.DateField(db_column='Date_Cloture_Site', blank=True,
                                         null=True,verbose_name='Date Cloture')


    est_bloquer = models.BooleanField(db_column='Est_Bloquer', default=False,
                                      editable=False)
    user_id = models.CharField(db_column='User_ID', max_length=15, editable=False,default=get_current_user)
    date_modification = models.DateTimeField(db_column='Date_Modification', auto_now=True)



    def __str__(self):
        return self.id


    def save(self, *args, **kwargs):
        if self.date_cloture_site and self.date_ouverture_site:
            if (self.date_cloture_site >= self.date_ouverture_site):
                super(Sites, self).save(*args, **kwargs)
            else:
                raise ValidationError("Date de cloture doit etre supérieur ou égale à la date d\'ouverture")
        if self.date_ouverture_site == None and self.date_cloture_site == None:
            super(Sites, self).save(*args, **kwargs)
        if( self.date_ouverture_site and self.date_cloture_site == None ):
            super(Sites, self).save(*args, **kwargs)

    class Meta:
        managed = False
        db_table = 'Tab_Site'
        verbose_name = 'Sites'
        verbose_name_plural = 'Sites'



class NT(CPkModel):
    code_site = models.CharField(db_column='Code_site', primary_key=True, max_length=10 ,
                                 verbose_name='Code du Site')
    nt = models.CharField(db_column='NT', max_length=20,null=False,primary_key=True,verbose_name='NT')
    code_client = models.CharField(db_column='Code_Client',verbose_name='Client',max_length=20)
    code_situation_nt = models.ForeignKey('api_sch.TabSituationNt', models.DO_NOTHING, db_column='Code_Situation_NT', blank=True, null=True,verbose_name='Situation',to_field='id')
    libelle = models.TextField(db_column='Libelle_NT', blank=True, null=True,verbose_name='libellé')
    date_ouverture_nt = models.DateField(db_column='Date_Ouverture_NT', blank=True, null=True,verbose_name='Ouverture')
    date_cloture_nt = models.DateField(db_column='Date_Cloture_NT', blank=True, null=True,verbose_name='Cloture')

    est_bloquer = models.BooleanField(db_column='Est_Bloquer', default=False,
                                      editable=False)
    user_id = models.CharField(db_column='User_ID', max_length=15, editable=False,default=get_current_user)
    date_modification = models.DateTimeField(db_column='Date_Modification', auto_now=True)
    class Meta:
        managed=False
        db_table = 'Tab_NT'
        verbose_name = 'NT'
        verbose_name_plural = 'NT'
        unique_together = (('code_site', 'nt'),)











class Marche(CPkModel):

    id=models.CharField(max_length=500,primary_key=True,verbose_name='Contrat N°')
    code_site = models.CharField(db_column='Code_site', max_length=10,
                                 verbose_name='Code du Site')
    nt = models.CharField(db_column='NT', max_length=20, null=False, verbose_name='NT')

    libelle = models.TextField(null=False,verbose_name='Libellé')
    ods_depart = models.DateField(null=False, blank=True
                                  , verbose_name='ODS de démarrage')
    delais = models.IntegerField(default=0, null=True
                                         , verbose_name='Délai des travaux')
    revisable = models.BooleanField(default=True, null=False
                                    , verbose_name='Est-il révisable ?')
    delai_paiement_f=models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(100)],
                                         null=True
                                                 , verbose_name='Délai de paiement')
    rabais =  models.FloatField(default=0,  verbose_name='Taux de rabais',
                              validators=[MinValueValidator(0), MaxValueValidator(100)], null=False)
    tva = models.FloatField(default=0,  verbose_name='TVA',
                              validators=[MinValueValidator(0), MaxValueValidator(100)], null=False)
    rg = models.FloatField(default=0, 
                             validators=[MinValueValidator(0), MaxValueValidator(100)], null=False
                             , verbose_name='Taux de retenue de garantie')

    date_signature = models.DateField(null=False, verbose_name='Date de signature')

    est_bloquer = models.BooleanField(db_column='Est_Bloquer', default=False,
                                      editable=False)
    user_id = models.CharField(db_column='User_ID', max_length=15, editable=False,default=get_current_user)
    date_modification = models.DateTimeField(db_column='Date_Modification', auto_now=True)

    @property
    def ht(self):
        try:
            dqes = DQE.objects.filter(code_site=self.code_site,nt=self.nt)
            sum = 0
            for dqe in dqes:
                sum = sum + dqe.prix_q
            return sum
        except DQE.DoesNotExist:
            return 0

    @property
    def ttc(self):
        return round(self.ht + (self.ht * self.tva / 100), 4)

    def __str__(self):
        return self.id


    @property
    def montant_global_f(self):
        factures = Factures.objects.filter(Q(marche=self))
        sum=0
        for f in factures:
            sum+=f.montant_factureTTC
        return sum

    @property
    def montant_global_p(self):

        enc = Encaissement.objects.filter(Q(facture__marche=self)).aggregate(
                models.Sum('montant_encaisse'))[
                "montant_encaisse__sum"] or 0

        return enc

    @property
    def montant_global_c(self):
        return self.montant_global_f-self.montant_global_p

    class Meta:
        managed = False
        db_table = 'Marche'
        verbose_name = 'Marchés'
        verbose_name_plural = 'Marchés'



class DQE(CPkModel):
    code_site = models.CharField(db_column='Code_site',primary_key=True, max_length=10,
                                 verbose_name='Code du Site')
    nt = models.CharField(db_column='NT', max_length=20,primary_key=True, null=False, verbose_name='NT')
    code_tache = models.CharField(db_column='Code_Tache',null=False, max_length=30
                                  ,verbose_name="Code Tache",primary_key=True)
    libelle = models.TextField(db_column='Libelle_Tache',verbose_name="Libelle")
    unite =models.ForeignKey('api_sch.TabUniteDeMesure',on_delete=models.DO_NOTHING, null=False,db_column='Code_Unite_Mesure', verbose_name='Unité')
    prix_u = models.FloatField(
        db_column='Prix_Unitaire',
        validators=[MinValueValidator(0)], default=0
        , verbose_name='Prix unitaire'
    )
    est_tache_composite = models.BooleanField(db_column='Est_Tache_Composite', blank=True,
                                              null=False,default=False,verbose_name="Tache composée")
    est_tache_complementaire = models.BooleanField(db_column='Est_Tache_Complementaire', blank=True,
                                                   null=False,default=False,verbose_name="Tache complementaire")
    quantite = models.FloatField( validators=[MinValueValidator(0)], default=0,verbose_name='Quantité')

    est_bloquer = models.BooleanField(db_column='Est_Bloquer', default=False,
                                      editable=False)
    user_id = models.CharField(db_column='User_ID', max_length=15, editable=False,default=get_current_user)
    date_modification = models.DateTimeField(db_column='Date_Modification', auto_now=True)


    def delete(self, *args, **kwargs):
        self.est_bloquer=True
        super().save(force_update=True,*args, **kwargs)


    @property
    def prix_q(self):
        pq= self.prix_u*self.quantite
        return pq


    class Meta:
        managed = False
        db_table = 'Tab_NT_Taches'
        verbose_name = 'DQE'
        verbose_name_plural = 'DQE'
        unique_together=(('code_site','nt','code_tache'))
        app_label = 'api_sm'



class TypeAvance(models.Model):
    libelle = models.CharField(max_length=500, null=False, unique=True)
    taux_max = models.FloatField(default=0,validators=[MinValueValidator(0), MaxValueValidator(100)], null=False)
    est_bloquer = models.BooleanField(db_column='Est_Bloquer', default=False,
                                      editable=False)
    user_id = models.CharField(db_column='User_ID', max_length=15, editable=False,default=get_current_user)
    date_modification = models.DateTimeField(db_column='Date_Modification', auto_now=True)

    def __str__(self):
        return self.libelle

    class Meta:
        managed=False
        verbose_name = 'Type Avance'
        verbose_name_plural = 'Type Avance'
        db_table = 'TypeAvance'
        app_label = 'api_sm'
        


class Avance(models.Model):
    type = models.ForeignKey(TypeAvance, on_delete=models.DO_NOTHING, null=False, to_field='id',
                             verbose_name="Type d'avance")
    num_avance = models.PositiveIntegerField(default=0, null=False, blank=True, editable=False,
                                                verbose_name="Numero d'avance")
    marche = models.ForeignKey(Marche, on_delete=models.DO_NOTHING, null=False, related_name="Avance_Marche",to_field='id')

    taux_avance = models.FloatField(default=0,  verbose_name="Taux d'avance", editable=False,
                                      validators=[MinValueValidator(0), MaxValueValidator(100)], null=False)

    montant = models.FloatField( validators=[MinValueValidator(0)], default=0,null=False,verbose_name='Montant d\'avance')

    debut = models.FloatField(default=0,  verbose_name="Debut",
                                      validators=[MinValueValidator(0), MaxValueValidator(100)], null=False)
    fin=models.FloatField(default=80,  verbose_name="Fin",
                                      validators=[MinValueValidator(0), MaxValueValidator(100)], null=False)
    est_bloquer = models.BooleanField(db_column='Est_Bloquer', default=False,
                                      editable=False)
    user_id = models.CharField(db_column='User_ID', max_length=15, editable=False,default=get_current_user)
    date_modification = models.DateTimeField(db_column='Date_Modification', auto_now=True)
    date=models.DateField(null=False,verbose_name="Date d'avance")
    remboursee = models.BooleanField(default=False, null=False,verbose_name='Est Remboursée')


    class Meta:
        managed=False
        verbose_name = 'Avance'
        verbose_name_plural = 'Avances'
        db_table='Avances'
        





class Attachements(models.Model):
    marche=models.ForeignKey(Marche,db_column='Num_Marche', on_delete=models.DO_NOTHING,null=False, blank=False,to_field='id')
    code_site = models.CharField(db_column='Code_site', max_length=10,
                                 verbose_name='Code du Site')
    nt = models.CharField(db_column='NT', max_length=20, null=False, verbose_name='NT')
    code_tache = models.CharField(db_column='Code_Tache', null=False, max_length=30
                                  , verbose_name="Code Tache")
    qte = models.FloatField( validators=[MinValueValidator(0)], default=0,verbose_name='Quantité Mois')
    prix_u = models.FloatField( validators=[MinValueValidator(0)], default=0,
                                     editable=False,verbose_name='Prix unitaire')
    montant= models.FloatField( validators=[MinValueValidator(0)], default=0,verbose_name='Montant du Mois',editable=False)
    date=models.DateField(null=False,verbose_name='Date')

    est_bloquer = models.BooleanField(db_column='Est_Bloquer', default=False,
                                      editable=False)
    user_id = models.CharField(db_column='User_ID', max_length=15, editable=False,default=get_current_user)
    date_modification = models.DateTimeField(db_column='Date_Modification', auto_now=True)

    def delete(self, *args, **kwargs):
        self.est_bloquer=True
        super().save(force_update=True,*args, **kwargs)

    @property
    def qte_cumule(self):
        try:
            ct=DQE.objects.get(nt=self.marche.nt,code_site=self.marche.code_site,code_tache=self.code_tache)
            previous_cumule = Attachements.objects.filter(code_tache=ct.code_tache,date__lt=self.date,est_bloquer=False)
            sum = self.qte
            if (previous_cumule):
                for pc in previous_cumule:
                    sum += pc.qte
                return sum
            else:
                return self.qte
        except Attachements.DoesNotExist:
            return self.qte
    @property
    def qte_precedente(self):
        try:
            ct = DQE.objects.get(nt=self.marche.nt, code_site=self.marche.code_site,code_tache=self.code_tache)
            previous_cumule = Attachements.objects.filter(code_tache=ct.code_tache, date__lt=self.date,est_bloquer=False)
            sum = 0
            if (previous_cumule):
                for pc in previous_cumule:
                    sum += pc.qte
            return sum
        except Attachements.DoesNotExist:
            return 0
    @property
    def montant_precedent(self):
        try:
            ct = DQE.objects.get(nt=self.marche.nt, code_site=self.marche.code_site,code_tache=self.code_tache)
            previous_cumule = Attachements.objects.filter(code_tache=ct.code_tache, date__lt=self.date,est_bloquer=False)
            sum = 0

            if (previous_cumule):
                for pc in previous_cumule:
                    sum += pc.montant
            return sum

        except Attachements.DoesNotExist:
            return 0

    @property
    def montant_cumule(self):
        try:
            ct = DQE.objects.get(nt=self.marche.nt, code_site=self.marche.code_site,code_tache=self.code_tache)
            previous_cumule = Attachements.objects.filter(code_tache=ct.code_tache,date__lt=self.date,est_bloquer=False)
            sum = self.montant
            if (previous_cumule):
                for pc in previous_cumule:
                    sum += pc.montant
                return sum
            else:
                return self.montant
        except Attachements.DoesNotExist:
            return self.montant



    class Meta:
        managed=False
        db_table = 'Attachements'
        verbose_name = 'Attachements'
        verbose_name_plural = 'Attachements'
        unique_together=(('marche','code_tache','date'),)
        app_label = 'api_sm'
        


class Factures(models.Model):
    numero_facture=models.CharField(max_length=800,db_column='Num_facture',primary_key=True,verbose_name='Numero de facture')
    num_situation=models.IntegerField(null=False,db_column='Num_Situation',verbose_name='Numero de situation')
    marche=models.ForeignKey(Marche,db_column='Num_Marche',on_delete=models.DO_NOTHING,null=False,verbose_name='Marche',to_field="id")
    du = models.DateField(null=False,verbose_name='Du')
    au = models.DateField(null=False,verbose_name='Au')
    paye = models.BooleanField(default=False,db_column='Paye', null=False,editable=False)
    date = models.DateField(auto_now=True, editable=False)
    montant= models.FloatField( db_column='Montant_Mois',validators=[MinValueValidator(0)], default=0,
                                      verbose_name="Montant du Mois"
                                      ,editable=False)

    montant_rb = models.FloatField( db_column='Montant_RB',validators=[MinValueValidator(0)], default=0,
                                       verbose_name="Montant du rabais"
                                       , editable=False) #montant du rabais du mois


    montant_rg=models.FloatField( db_column='Montant_RG',validators=[MinValueValidator(0)], default=0,
                                         verbose_name="Montant Retenue de garantie"
                                         ,editable=False) #retenue de garantie le montant du mois



    est_bloquer = models.BooleanField(db_column='Est_Bloquer', default=False,
                                      editable=False)
    user_id = models.CharField(db_column='User_ID', max_length=15, editable=False,default=get_current_user)
    date_modification = models.DateTimeField(db_column='Date_Modification', auto_now=True)





    @property
    def montant_ava_remb(self):
        try:
            remb=Remboursement.objects.get(facture=self.numero_facture,avance__type=2)
            if(remb):
                return remb.montant
            else:
                return 0
        except Remboursement.DoesNotExist:
            return  0
    @property
    def montant_avf_remb(self):
        try:
            remb=Remboursement.objects.get(facture=self.numero_facture,avance__type=1)
            if(remb):
                return remb.montant
            else:
                return 0
        except Remboursement.DoesNotExist:
            return 0

    @property
    def montant_factureHT(self):
        return round(self.montant - self.montant_rb - self.montant_rg-self.montant_ava_remb-self.montant_avf_remb, 2)
    @property
    def montant_factureTTC(self):
        return round(self.montant_factureHT+(self.montant_factureHT*(self.marche.tva / 100)),2)




    @property
    def montant_precedent(self):
        try:
            previous_cumule = Factures.objects.filter(marche=self.marche, num_situation__lt=self.num_situation)
            sum = 0
            if (previous_cumule):
                for pc in previous_cumule:
                    sum += pc.montant
            return sum
        except Factures.DoesNotExist:
            return 0

    @property
    def montant_cumule(self):
        try:
            previous_cumule = Factures.objects.filter(marche=self.marche, num_situation__lt=self.num_situation)
            sum = self.montant
            if (previous_cumule):
                for pc in previous_cumule:
                    sum += pc.montant
                return sum
            else:
                return self.montant
        except Factures.DoesNotExist:
            return self.montant



    class Meta:
        managed=False
        db_table='Factures'
        verbose_name = 'Factures'
        verbose_name_plural = 'Factures'
        app_label = 'api_sm'
        
class Remboursement(models.Model):
    facture = models.ForeignKey(Factures,db_column='Num_Facture', on_delete=models.DO_NOTHING, null=True, blank=True, to_field="numero_facture")
    avance=models.ForeignKey(Avance,db_column='Avance', on_delete=models.DO_NOTHING, null=True, blank=True)

    montant =models.FloatField( db_column='Montant',validators=[MinValueValidator(0)], default=0,
                                         verbose_name="Montant Mois"
                                         ,editable=False)


    est_bloquer = models.BooleanField(db_column='Est_Bloquer', default=False,
                                      editable=False)
    user_id = models.CharField(db_column='User_ID', max_length=15, editable=False,default=get_current_user)
    date_modification = models.DateTimeField(db_column='Date_Modification', auto_now=True)

    @property
    def montant_cumule(self):
        try:
            previous_cumule = Remboursement.objects.filter(facture__marche=self.facture.marche,avance=self.avance, facture__num_situation__lt=self.facture.num_situation)
            sum = self.montant
            if (previous_cumule):
                for pc in previous_cumule:
                    sum += pc.montant
                return sum
            else:
                return self.montant
        except Remboursement.DoesNotExist:
            return self.montant

    @property
    def rst_remb(self):
        return self.avance.montant-self.montant_cumule







    class Meta:
        managed=False
        db_table='Rembourcement'
        verbose_name = 'Remboursement'
        verbose_name_plural = 'Remboursements'
        app_label = 'api_sm'
        unique_together=(('facture','avance'),)



class DetailFacture(models.Model):
    facture=models.ForeignKey(Factures,on_delete=models.DO_NOTHING,null=True,blank=True,to_field="numero_facture")
    detail=models.ForeignKey(Attachements,on_delete=models.DO_NOTHING)
    est_bloquer = models.BooleanField(db_column='Est_Bloquer', default=False,
                                      editable=False)
    user_id = models.CharField(db_column='User_ID', max_length=15, editable=False,default=get_current_user)
    date_modification = models.DateTimeField(db_column='Date_Modification', auto_now=True)


    class Meta:
        managed=False
        db_table='Detail_Facture'
        verbose_name = 'Datails Facture'
        verbose_name_plural = 'Details Facture'
        app_label = 'api_sm'
        


class ModePaiement(models.Model):
    libelle=models.CharField(max_length=500,null=False,unique=True)
    est_bloquer = models.BooleanField(db_column='Est_Bloquer', default=False,
                                      editable=False)
    user_id = models.CharField(db_column='User_ID', max_length=15, editable=False,default=get_current_user)
    date_modification = models.DateTimeField(db_column='Date_Modification', auto_now=True)

    def __str__(self):
        return  self.libelle
    class Meta:
        managed=False
        db_table='Mode_Paiement'
        verbose_name = 'Mode de Paiement'
        verbose_name_plural = 'Mode de Paiement'
        app_label = 'api_sm'
        



class Encaissement(models.Model):


    facture=models.ForeignKey(Factures,on_delete=models.DO_NOTHING,null=True,blank=True,verbose_name="Facture")
    date_encaissement=models.DateField(null=False,verbose_name="Date d'encaissement")
    mode_paiement=models.ForeignKey(ModePaiement,on_delete=models.DO_NOTHING,null=False,verbose_name="Mode de paiement")
    montant_encaisse=models.FloatField( blank=True,verbose_name="Montant encaissé",
                                     validators=[MinValueValidator(0)], default=0)
    agence = models.ForeignKey('api_sch.TabAgence',on_delete=models.DO_NOTHING,db_constraint=False , null=True, verbose_name='Agence')

    numero_piece = models.CharField(max_length=300,null=False,verbose_name="Numero de piéce")

    est_bloquer = models.BooleanField(db_column='Est_Bloquer', default=False,
                                      editable=False)
    user_id = models.CharField(db_column='User_ID', max_length=15, editable=False,default=get_current_user)
    date_modification = models.DateTimeField(db_column='Date_Modification', auto_now=True)

    @property
    def montant_creance(self):
        try:
            enc = Encaissement.objects.filter(facture=self.facture, date_encaissement__lt=self.date_encaissement).aggregate(
                models.Sum('montant_encaisse'))[
                "montant_encaisse__sum"]

            if (enc == None):
                enc = self.montant_encaisse
            else:
                enc += self.montant_encaisse

            return (self.facture.montant_factureTTC - enc)
        except Encaissement.DoesNotExist:
            return 0




    class Meta:
        managed=False
        db_table="Encaissements"
        verbose_name = 'Encaissement'
        verbose_name_plural = 'Encaissement'
        unique_together=(("facture","date_encaissement"),)
        app_label = 'api_sm'



class TypeCaution(models.Model):

    libelle = models.CharField(max_length=500,null=True,blank=True)
    type_avance = models.ForeignKey(TypeAvance, on_delete=models.DO_NOTHING, null=True,blank=True, to_field='id',
                             verbose_name="Type d'avance")
    taux_exact= models.FloatField(
                                   validators=[MinValueValidator(0), MaxValueValidator(100)], null=True,blank=True)
    taux_min = models.FloatField(
                               validators=[MinValueValidator(0), MaxValueValidator(100)], null=True,blank=True)
    taux_max = models.FloatField( 
                                   validators=[MinValueValidator(0), MaxValueValidator(100)], null=True,blank=True)

    est_bloquer = models.BooleanField(db_column='Est_Bloquer', default=False,
                                      editable=False)
    user_id = models.CharField(db_column='User_ID', max_length=15, editable=False,default=get_current_user)
    date_modification = models.DateTimeField(db_column='Date_Modification', auto_now=True)

    def __str__(self):
        return self.libelle

    def save(self, *args, **kwargs):
        super(TypeCaution, self).save(*args, **kwargs)



    class Meta:
        managed=False
        db_table='Type_Caution'
        verbose_name = 'Type_Caution'
        verbose_name_plural = 'Type_Caution'
        app_label = 'api_sm'


class Cautions(models.Model):

    marche = models.ForeignKey(Marche,db_column='Num_Marche', on_delete=models.DO_NOTHING, null=True, related_name="Caution_Marche",to_field='id')
    type = models.ForeignKey(TypeCaution,db_column='Type_Caution', on_delete=models.DO_NOTHING, null=False,verbose_name="Libelle",to_field='')
    avance = models.ForeignKey(Avance,db_column='Avance', on_delete=models.DO_NOTHING, null=True, blank=True,verbose_name='Avance')
    date_soumission = models.DateField(null=False,verbose_name="Date dépot")
    agence = models.ForeignKey('api_sch.TabAgence',db_column='Agence', on_delete=models.CASCADE,verbose_name="Agence")
    montant = models.FloatField(
        verbose_name="Montant",
        validators=[MinValueValidator(0)], default=0,
    )
    est_recupere = models.BooleanField(default=False,db_column='Est_Recupere', null=False,verbose_name='Est Recuperée')
    est_bloquer = models.BooleanField(db_column='Est_Bloquer', default=False,
                                      editable=False)
    user_id = models.CharField(db_column='User_ID', max_length=15, editable=False,default=get_current_user)
    date_modification = models.DateTimeField(db_column='Date_Modification', auto_now=True)

    class Meta:
        managed=False
        db_table='Cautions'
        verbose_name = 'Caution'
        verbose_name_plural = 'Caution'
        app_label = 'api_sm'




class RevisionPrix(CPkModel):
    marche = models.CharField(db_column='marche_id',primary_key=True, max_length=500)
    code_site = models.CharField(db_column='Code_site', primary_key=True, max_length=10,
                                 verbose_name='Code du Site')
    nt = models.CharField(db_column='NT', max_length=20, primary_key=True, null=False, verbose_name='NT')
    code_tache = models.CharField(db_column='Code_Tache', null=False, max_length=30
                                  , verbose_name="Code Tache", primary_key=True)
    date_rev = models.DateField(db_column='Date_Rev', primary_key=True,verbose_name='Date Révision')
    coef = models.FloatField(db_column='Coef',verbose_name='Coefficient Révision')
    est_bloquer = models.BooleanField(db_column='Est_Bloquer', default=False,
                                      editable=False)
    user_id = models.CharField(db_column='User_ID', max_length=15, editable=False,default=get_current_user)
    date_modification = models.DateTimeField(db_column='Date_Modification', auto_now=True)

    class Meta:
        managed = False
        db_table = 'Revision_Prix'
        unique_together = (('date_rev', 'code_site', 'marche', 'nt', 'code_tache'),)
