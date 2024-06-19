from datetime import datetime
from cpkmodel import CPkModel
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator

from django.db.models import Q
from django_currentuser.middleware import get_current_user
from api_sch.models import *
from django.db import connection



class GeneralManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(Q(est_bloquer=False) or Q(est_bloquer=None))
    def deleted(self):
        return super().get_queryset().filter(Q(est_bloquer=True))



class DeleteMixin:
    def delete(self, *args, **kwargs):
        self.est_bloquer = True
        self.save()


class ProductionStockee(DeleteMixin,CPkModel):
    code_site=models.CharField(db_column='Code_Site', primary_key=True, max_length=10 , editable=False,
                                 verbose_name='Pole')
    nt=models.CharField(db_column='NT', max_length=20,editable=False,primary_key=True,verbose_name='NT')

    code_tache = models.CharField(db_column='Code_Tache', editable=False, max_length=30
                                  , verbose_name="Code Tache", primary_key=True)

    qte_att=models.FloatField(db_column='Qte_Attachee',  verbose_name='Qte Attachée',editable=False)
    qte_prod=models.FloatField(db_column='Qte_Produite',  verbose_name='Qte Produite',editable=False)

    ecart=models.FloatField(db_column='Ecart_Prod_Att',  verbose_name='Ecart (Production et Attachement)',editable=False)
    ind= models.BooleanField(db_column='Indicateur',verbose_name='Indicateur',editable=False)
    class Meta:
        managed = False
        db_table = 'Vue_Production_Stockee'
        verbose_name = 'Production_Stockee'
        verbose_name_plural = 'Production_Stockee'


class Clients(DeleteMixin,models.Model):
    id =models.CharField(db_column='Code_Client', primary_key=True,
                                   max_length=20,verbose_name="Code Client")
    type_client = models.SmallIntegerField(db_column='Type_Client', blank=True, null=True,verbose_name="Type Client")  
    est_client_cosider = models.BooleanField(db_column='Est_Client_Cosider', blank=True,
                                             null=True,verbose_name="Est Client Cosider ?")  
    libelle = models.CharField(db_column='Libelle_Client', max_length=300, blank=True,
                                      null=True,verbose_name="Libellé")  
    nif = models.CharField(db_column='NIF', unique=True, max_length=50, blank=True,
                           null=True,verbose_name="NIF")  
    raison_social = models.CharField(db_column='Raison_Social', max_length=50, blank=True,
                                     null=True,verbose_name="Raison Sociale")
    num_registre_commerce = models.CharField(db_column='Num_Registre_Commerce', max_length=20, blank=True,
                                             null=True,verbose_name="N° Registre Commerce")


    est_bloquer = models.BooleanField(db_column='Est_Bloquer', default=False,
                                      editable=False)
    user_id = models.CharField(db_column='User_ID', max_length=15, editable=False,default=get_current_user)
    date_modification = models.DateTimeField(db_column='Date_Modification', auto_now=True)
    objects = GeneralManager()

    def __str__(self):
        return  self.id

    class Meta:
        managed=False
        db_table = 'Tab_Client'
        verbose_name = 'Clients'
        verbose_name_plural = 'Clients'



class Sites(DeleteMixin,models.Model):
    RG=(
        ('',''),
        ('N','Nord'),
         ('S','Sud'),
          ('W','West'),
           ('E','Est'),
            ('C','Centre'),
    )
    id = models.CharField(db_column='Code_site', primary_key=True, max_length=10 ,
                                 verbose_name='Code Pole')
    code_filiale = models.ForeignKey(TabFiliale, models.DO_NOTHING,
                                     db_column='Code_Filiale',verbose_name='Filiale')
    code_region = models.CharField(db_column='Code_Region', max_length=1, blank=True,
                                   null=True,verbose_name='Région',choices=RG)
    libelle = models.CharField(db_column='Libelle_Site', max_length=150, blank=True,
                                    null=True,verbose_name='Libellé')
    code_agence = models.ForeignKey(TabAgence, models.DO_NOTHING, db_column='Code_Agence', blank=True,
                                    null=True,verbose_name='Agence')
    type_site = models.SmallIntegerField(db_column='Type_Site', blank=True, null=True,verbose_name='Type du Site')
    code_division = models.ForeignKey(TabDivision, models.DO_NOTHING, db_column='Code_Division', blank=True,
                                      null=True,verbose_name='Division')
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
    objects = GeneralManager()


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



class NT(DeleteMixin,CPkModel):
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
    objects = GeneralManager()
    class Meta:
        managed=False
        db_table = 'Tab_NT'
        verbose_name = 'NT'
        verbose_name_plural = 'NT'
        unique_together = (('code_site', 'nt'),)











class Marche(DeleteMixin,CPkModel):
    id = models.CharField(db_column='Num_Contrat', primary_key=True,verbose_name='Contrat N°',
                                   max_length=500)
    num_avenant = models.IntegerField(db_column='Num_Avenant',editable=False,verbose_name='Avenant N°',default=0)
    code_site = models.CharField(db_column='Code_Site', max_length=10,
                                 verbose_name='Code du Site')
    nt = models.CharField(db_column='NT', max_length=20, null=False, verbose_name='NT')

    libelle = models.TextField(db_column='Libelle',null=False,verbose_name='Libellé')
    ods_depart = models.DateField(db_column='Ods_Depart',null=False
                                  , verbose_name='ODS de démarrage')
    delais = models.IntegerField(db_column='Delais',default=0, null=True
                                         , verbose_name='Délai des travaux')
    revisable = models.BooleanField(db_column='Revisable',default=True, null=False
                                    , verbose_name='Est-il révisable ?')
    actualisable = models.BooleanField(db_column='Actualisable',default=True, null=False
                                    , verbose_name='Est-il révisable ?')
    delai_paiement_f=models.IntegerField(db_column='Delai_Paiement_F',default=0, validators=[MinValueValidator(0), MaxValueValidator(100)],
                                         null=True, verbose_name='Délai de paiement')
    rabais =  models.FloatField(db_column='Rabais',default=0,  verbose_name='Taux de rabais',
                              validators=[MinValueValidator(0), MaxValueValidator(100)], null=False)
    tva = models.FloatField(db_column='Tva',default=0,  verbose_name='TVA',
                              validators=[MinValueValidator(0), MaxValueValidator(100)], null=False)
    rg = models.FloatField(db_column='Rg',default=0,
                             validators=[MinValueValidator(0), MaxValueValidator(100)], null=False
                             , verbose_name='Taux de retenue de garantie')

    date_signature = models.DateField(db_column='Date_Signature',null=False, verbose_name='Date de signature')

    est_bloquer = models.BooleanField(db_column='Est_Bloquer', default=False,
                                      editable=False)
    user_id = models.CharField(db_column='User_ID', max_length=15, editable=False,default=get_current_user)
    date_modification = models.DateTimeField(db_column='Date_Modification', auto_now=True)
    objects = GeneralManager()
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




class MarcheAvenant(DeleteMixin,CPkModel):
    id = models.CharField(db_column='Num_Contrat', primary_key=True,verbose_name='Contrat N°',
                                   max_length=500)
    num_avenant = models.IntegerField(db_column='Num_Avenant',primary_key=True,editable=False,verbose_name='Avenant N°',default=0)
    code_site = models.CharField(db_column='Code_Site', max_length=10,
                                 verbose_name='Pole')
    nt = models.CharField(db_column='NT', max_length=20, null=False, verbose_name='NT')

    libelle = models.TextField(db_column='Libelle',null=False,verbose_name='Libellé')
    ods_depart = models.DateField(db_column='Ods_Depart',null=False
                                  , verbose_name='ODS de démarrage')
    delais = models.IntegerField(db_column='Delais',default=0, null=True
                                         , verbose_name='Délai des travaux')
    revisable = models.BooleanField(db_column='Revisable',default=True, null=False
                                    , verbose_name='Est-il révisable ?')
    actualisable = models.BooleanField(db_column='Actualisable', default=True, null=False
                                       , verbose_name='Est-il révisable ?')

    delai_paiement_f=models.IntegerField(db_column='Delai_Paiement_F',default=0, validators=[MinValueValidator(0), MaxValueValidator(100)],
                                         null=True
                                                 , verbose_name='Délai de paiement')
    rabais =  models.FloatField(db_column='Rabais',default=0,  verbose_name='Taux de rabais',
                              validators=[MinValueValidator(0), MaxValueValidator(100)], null=False)
    tva = models.FloatField(db_column='Tva',default=0,  verbose_name='TVA',
                              validators=[MinValueValidator(0), MaxValueValidator(100)], null=False)
    rg = models.FloatField(db_column='Rg',default=0,
                             validators=[MinValueValidator(0), MaxValueValidator(100)], null=False
                             , verbose_name='Taux de retenue de garantie')
    date_signature = models.DateField(db_column='Date_Signature',null=False, verbose_name='Date de signature')


    est_bloquer = models.BooleanField(db_column='Est_Bloquer', default=False,
                                      editable=False)
    user_id = models.CharField(db_column='User_ID', max_length=15, editable=False,default=get_current_user)

    date_modification = models.DateTimeField(db_column='Date_Modification', auto_now=True)
    objects = GeneralManager()
    class Meta:
        managed = False
        db_table = 'Marche_Avenant'

    @property
    def ht(self):
        try:
            dqes = DQEAvenant.objects.filter(code_site=self.code_site, nt=self.nt,num_avenant=self.num_avenant)
            sum = 0
            for dqe in dqes:
                sum = sum + dqe.prix_q
            return sum
        except DQEAvenant.DoesNotExist:
            return 0

    @property
    def ttc(self):
        return round(self.ht + (self.ht * self.tva / 100), 4)


class DQE(DeleteMixin,CPkModel):
    code_site = models.CharField(db_column='Code_site',primary_key=True, max_length=10,
                                 verbose_name='Code du Site')
    nt = models.CharField(db_column='NT', max_length=20,primary_key=True, null=False, verbose_name='NT')
    code_tache = models.CharField(db_column='Code_Tache',null=False, max_length=30
                                  ,verbose_name="Code Tache",primary_key=True)
    libelle = models.TextField(db_column='Libelle_Tache',verbose_name="Libellé")
    unite =models.ForeignKey('api_sch.TabUniteDeMesure',on_delete=models.DO_NOTHING, null=False,db_column='Code_Unite_Mesure', verbose_name='Unité')
    prix_u = models.FloatField(
        db_column='Prix_Unitaire',
        validators=[MinValueValidator(0)], default=0
        , verbose_name='Prix unitaire'
    )
    est_tache_composite = models.BooleanField(db_column='Est_Tache_Composite', blank=True,
                                              null=False,default=False,verbose_name="Tache composée ?")
    est_tache_complementaire = models.BooleanField(db_column='Est_Tache_Complementaire', blank=True,
                                                   null=False,default=False,verbose_name="Tache complementaire ?")
    quantite = models.FloatField( validators=[MinValueValidator(0)], default=0,verbose_name='Quantité')

    est_bloquer = models.BooleanField(db_column='Est_Bloquer', default=False,
                                      editable=False)
    user_id = models.CharField(db_column='User_ID', max_length=15, editable=False,default=get_current_user)
    date_modification = models.DateTimeField(db_column='Date_Modification', auto_now=True)
    objects = GeneralManager()


    @property
    def prix_q(self):
        try:
            pq= float(self.prix_u)*float(self.quantite)
            return pq
        except:
            return 0

    class Meta:
        managed = False
        db_table = 'Tab_NT_Taches'
        verbose_name = 'DQE'
        verbose_name_plural = 'DQE'
        unique_together=(('code_site','nt','code_tache'))
        app_label = 'api_sm'






class DQEAvenant(DeleteMixin,CPkModel):
    code_site = models.CharField(db_column='Code_Site', primary_key=True, max_length=10,
                                 verbose_name='Code du Site')
    nt = models.CharField(db_column='NT', max_length=20, primary_key=True, null=False, verbose_name='NT')
    code_tache = models.CharField(db_column='Code_Tache', null=False, max_length=30
                                  , verbose_name="Code Tache", primary_key=True)
    num_avenant = models.IntegerField(db_column='Num_Avenant', blank=True, null=True,verbose_name='Avenant N°')  
    est_tache_composite = models.BooleanField(db_column='Est_Tache_Composite', blank=True, null=True,verbose_name='Est Composée ?')  
    est_tache_complementaire = models.BooleanField(db_column='Est_Tache_Complementaire', blank=True, null=True,verbose_name='Est Complémentaire ?')  
    libelle = models.TextField(db_column='Libelle_Tache', blank=True, null=True)  
    unite =models.ForeignKey('api_sch.TabUniteDeMesure',on_delete=models.DO_NOTHING, null=False,db_column='Code_Unite_Mesure', verbose_name='Unité')
    quantite = models.FloatField(db_column='Quantite', blank=True, null=True)  
    prix_u = models.DecimalField(db_column='Prix_Unitaire', max_digits=19, decimal_places=4, blank=True, null=True,verbose_name='Prix Unit')  
    est_bloquer = models.BooleanField(db_column='Est_Bloquer', blank=True, null=True)  
    user_id = models.CharField(db_column='User_ID', max_length=15, editable=False, default=get_current_user)
    date_modification = models.DateTimeField(db_column='Date_Modification', auto_now=True)
    objects = GeneralManager()

    @property
    def prix_q(self):
        try:
            pq= float(self.prix_u)*float(self.quantite)
            return pq
        except:
            return 0


    class Meta:
        managed = False
        db_table = 'Tab_NT_Taches_Avenant'
        unique_together = (('code_site', 'nt', 'code_tache'),)





class TypeAvance(DeleteMixin,models.Model):
    id = models.CharField(db_column='Id_Type_Avance', primary_key=True,
                                      max_length=3)  

    libelle = models.CharField(db_column='Libelle',max_length=500, null=False, unique=True)
    taux_max = models.FloatField(db_column='Taux',default=0,validators=[MinValueValidator(0), MaxValueValidator(100)], null=False)

    est_bloquer = models.BooleanField(db_column='Est_Bloquer', default=False,
                                      editable=False)
    user_id = models.CharField(db_column='User_ID', max_length=15, editable=False,default=get_current_user)
    date_modification = models.DateTimeField(db_column='Date_Modification', auto_now=True)
    objects = GeneralManager()
    def __str__(self):
        return self.libelle

    class Meta:
        managed=False
        verbose_name = 'Type Avance'
        verbose_name_plural = 'Type Avance'
        db_table = 'Type_Avance'
        app_label = 'api_sm'



class Avance(DeleteMixin,models.Model):
    id = models.CharField(db_column='Id_Avance', primary_key=True,max_length=30)
    type = models.ForeignKey(TypeAvance, on_delete=models.DO_NOTHING, null=False,db_column='Type_Avance',
                             verbose_name="Type d'avance")
    num_avance = models.PositiveIntegerField(db_column='Num_Avance',default=0, null=False, blank=True, editable=False,
                                                verbose_name="Numero d'avance")
    marche = models.ForeignKey(Marche, on_delete=models.DO_NOTHING, null=False, related_name="Avance_Marche",to_field='id',db_column='Num_Marche')


    montant = models.FloatField(db_column='Montant' ,validators=[MinValueValidator(0)], default=0,null=False,verbose_name='Montant d\'avance')

    debut = models.FloatField(db_column='Taux_Debut_Remb',default=0,  verbose_name="Debut",
                                      validators=[MinValueValidator(0), MaxValueValidator(100)], null=False)
    fin=models.FloatField(db_column='Taux_Fin_Remb',default=80,  verbose_name="Fin",
                                      validators=[MinValueValidator(0), MaxValueValidator(100)], null=False)

    date = models.DateField(db_column='Date_Avance', null=False, verbose_name="Date d'avance")
    remboursee = models.BooleanField(db_column='Remboursee', default=False, null=False, verbose_name='Est Remboursée')

    est_bloquer = models.BooleanField(db_column='Est_Bloquer', default=False,
                                      editable=False)
    user_id = models.CharField(db_column='User_ID', max_length=15, editable=False,default=get_current_user)
    date_modification = models.DateTimeField(db_column='Date_Modification', auto_now=True)
    objects = GeneralManager()
    @property
    def taux_avance (self):
        m=MarcheAvenant.objects.get(id=self.marche.id,num_avenant=0)
        return (self.montant/m.ht)*100

    @property
    def taux_remb(self):
        tremb = round(
            (float(self.taux_avance) / (float(self.fin) - float(self.debut))) * 100, 4)
        return tremb

    class Meta:
        managed=False
        verbose_name = 'Avance'
        verbose_name_plural = 'Avances'
        db_table='Avances'






class Attachements(DeleteMixin,models.Model):
    id = models.CharField(db_column='Id_Attachement', primary_key=True, max_length=30)  

    marche = models.ForeignKey('Marche', models.DO_NOTHING, db_column='Num_Marche', blank=True,
                                   null=True)
    code_site = models.CharField(db_column='Code_Site', max_length=10,
                                 verbose_name='Code du Site')
    nt = models.CharField(db_column='NT', max_length=20, null=False, verbose_name='NT')
    code_tache = models.CharField(db_column='Code_Tache', null=False, max_length=30
                                  , verbose_name="Code Tache")
    qte = models.FloatField(db_column='Quantite', validators=[MinValueValidator(0)], default=0,verbose_name='Quantité Mois')
    prix_u = models.FloatField( db_column='Prix_Unitaire',validators=[MinValueValidator(0)], default=0,
                                     editable=False,verbose_name='Prix unitaire')
    montant= models.FloatField(db_column='Montant', validators=[MinValueValidator(0)], default=0,verbose_name='Montant du Mois')
    date=models.DateField(null=False,db_column='Mmaa',verbose_name='Date')

    est_bloquer = models.BooleanField(db_column='Est_Bloquer', default=False,
                                      editable=False)
    user_id = models.CharField(db_column='User_ID', max_length=15, editable=False,default=get_current_user)
    date_modification = models.DateTimeField(db_column='Date_Modification', auto_now=True)
    objects = GeneralManager()

    def delete(self, *args, **kwargs):
        username = str(get_current_user())
        id_Att=self.id
        sql_query = f"""
                 IF NOT EXISTS(SELECT * FROM Detail_Facture WHERE Detail = '{id_Att}')
                            BEGIN
                                 DECLARE @Count INT =  (SELECT  COUNT(Est_Bloquer) FROM Attachements WHERE Est_Bloquer = 1);
                                 UPDATE Attachements SET Id_Attachement =CONCAT(Id_Attachement,'-A-',@Count),User_ID='{username}', Date_Modification = GETDATE(),Est_Bloquer = 1 WHERE Id_Attachement = '{id_Att}' ;
                            END
                 ELSE
                            BEGIN
                                RAISERROR ('Annulation Impossible Déja Facturé', 16, 1)
                            END     
               """
        with connection.cursor() as cursor:
            cursor.execute(sql_query)


    @property
    def qte_cumule(self):
        try:
            ct=DQE.objects.get(nt=self.marche.nt,code_site=self.marche.code_site,code_tache=self.code_tache)
            previous_cumule = Attachements.objects.filter(code_tache=ct.code_tache,date__lt=self.date)
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
            previous_cumule = Attachements.objects.filter(code_tache=ct.code_tache, date__lt=self.date)
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
            previous_cumule = Attachements.objects.filter(code_tache=ct.code_tache, date__lt=self.date)
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
            previous_cumule = Attachements.objects.filter(code_tache=ct.code_tache,date__lt=self.date)
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



class Factures(DeleteMixin,models.Model):
    numero_facture=models.CharField(max_length=800,db_column='Num_Facture',primary_key=True,verbose_name='Numero de facture')
    num_situation=models.IntegerField(null=False,db_column='Num_Situation',verbose_name='Numero de situation')
    marche=models.ForeignKey(Marche,db_column='Num_Marche',on_delete=models.DO_NOTHING,null=False,verbose_name='Marche',to_field="id")
    du = models.DateField(db_column='Date_Debut',null=False,verbose_name='Du')
    au = models.DateField(db_column='Date_Fin',null=False,verbose_name='Au')
    paye = models.BooleanField(default=False,db_column='Paye', null=False,editable=False)
    date = models.DateField(db_column='Date_Facture',auto_now=True, editable=False)
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

    objects = GeneralManager()

    def delete(self, *args, **kwargs):
        num_f = self.numero_facture
        username=str(get_current_user())
        sql_query = f"""
                        
                        IF NOT EXISTS (SELECT * FROM Encaissements WHERE Facture = '{num_f}')
                            BEGIN
                                   UPDATE Detail_Facture SET Num_Facture = NULL WHERE  Num_Facture = '{num_f}';
                                   UPDATE Remboursement SET Num_Facture = NULL WHERE  Num_Facture = '{num_f}';
                                   UPDATE Penalite_Retard SET Num_Facture = NULL WHERE  Num_Facture = '{num_f}';
                                   
                                   DECLARE @Count INT =  (SELECT  COUNT(Est_Bloquer) FROM Factures WHERE Est_Bloquer = 1);
                                   UPDATE Factures SET Num_Facture = CONCAT('{num_f}', '-A-',@Count ) , Est_Bloquer = 1,User_ID='{username}',Date_Modification=GETDATE() WHERE Num_Facture = '{num_f}';
                                   UPDATE Detail_Facture SET Num_Facture = CONCAT('{num_f}', '-A-', @Count)  , Est_Bloquer = 1,User_ID='{username}',Date_Modification=GETDATE()  WHERE  Num_Facture IS NULL;
                                   UPDATE Remboursement SET Num_Facture = CONCAT('{num_f}', '-A-', @Count)  , Est_Bloquer = 1,User_ID='{username}',Date_Modification=GETDATE()  WHERE  Num_Facture IS NULL;
                                   UPDATE Penalite_Retard SET Num_Facture = CONCAT('{num_f}', '-A-', @Count)  , Est_Bloquer = 1,User_ID='{username}',Date_Modification=GETDATE()  WHERE  Num_Facture IS NULL;
                                   
                            
                            END
                        
                        ELSE
                            BEGIN
                                RAISERROR ('Annulation Impossible', 16, 1)
                            END     
               
               """
        with connection.cursor() as cursor:
            try:
                cursor.execute(sql_query)
            except Exception as e:
                raise ValidationError(str(e))
    @property
    def montant_ava_remb(self):
        try:
            remb=Remboursement.objects.get(facture=self.numero_facture,avance__type__id='A')
            if(remb):
                return remb.montant
            else:
                return 0
        except Remboursement.DoesNotExist:
            return  0
    @property
    def montant_avf_remb(self):
        try:
            remb=Remboursement.objects.get(facture=self.numero_facture,avance__type__id='F')
            if(remb):
                return remb.montant
            else:
                return 0
        except Remboursement.DoesNotExist:
            return 0

    @property
    def montant_ave_remb(self):
        try:
            remb = Remboursement.objects.get(facture=self.numero_facture, avance__type__id='E')
            if (remb):
                return remb.montant
            else:
                return 0
        except Remboursement.DoesNotExist:
            return 0

    @property
    def penalite(self):
        try:
            p = PenaliteRetard.objects.get(facture__numero_facture=self.numero_facture, facture__num_situation=self.num_situation)
            if (p):
                return p.montant
            else:
                return 0
        except PenaliteRetard.DoesNotExist:
            return 0


    @property
    def montant_factureHT(self):
        return round(self.montant - self.montant_rb - self.montant_rg-self.montant_ava_remb-self.montant_avf_remb-self.montant_ave_remb-self.penalite, 2)
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







class Remboursement(DeleteMixin,models.Model):
    id = models.AutoField(db_column='Id_Remb', primary_key=True)
    facture = models.ForeignKey(Factures,db_column='Num_Facture', on_delete=models.DO_NOTHING, null=True, blank=True, to_field="numero_facture")
    avance=models.ForeignKey(Avance,db_column='Avance', on_delete=models.DO_NOTHING, null=True, blank=True)

    montant =models.FloatField( db_column='Montant',validators=[MinValueValidator(0)], default=0,
                                         verbose_name="Montant Mois"
                                         ,editable=False)


    est_bloquer = models.BooleanField(db_column='Est_Bloquer', default=False,
                                      editable=False)
    user_id = models.CharField(db_column='User_ID', max_length=15, editable=False,default=get_current_user)
    date_modification = models.DateTimeField(db_column='Date_Modification', auto_now=True)
    objects = GeneralManager()
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
        return round(self.avance.montant-self.montant_cumule,2)

    class Meta:
        managed=False
        db_table='Remboursement'
        verbose_name = 'Remboursement'
        verbose_name_plural = 'Remboursements'
        app_label = 'api_sm'
        unique_together=(('facture','avance'),)


class PenaliteRetard(DeleteMixin,models.Model):

    id = models.AutoField(db_column='Id_Penalite', primary_key=True)
    facture = models.ForeignKey(Factures, db_column='Num_Facture', on_delete=models.DO_NOTHING, null=True,
                                    blank=True, to_field="numero_facture")

    montant = models.FloatField(db_column='Montant', validators=[MinValueValidator(0)], default=0,
                                    verbose_name="Montant Mois"
                                    , editable=False)

    est_bloquer = models.BooleanField(db_column='Est_Bloquer', default=False,
                                          editable=False)
    user_id = models.CharField(db_column='User_ID', max_length=15, editable=False, default=get_current_user)
    date_modification = models.DateTimeField(db_column='Date_Modification', auto_now=True)
    objects = GeneralManager()
    @property
    def montant_cumule(self):
        try:
            previous_cumule = PenaliteRetard.objects.filter(facture__marche=self.facture.marche,
                                                               facture__num_situation__lt=self.facture.num_situation)
            sum = self.montant
            if (previous_cumule):
                for pc in previous_cumule:
                    sum += pc.montant
                return sum
            else:
                return self.montant
        except PenaliteRetard.DoesNotExist:
            return self.montant

    class Meta:
        managed=False
        db_table='Penalite_Retard'
        verbose_name = 'Penalite Retard'
        verbose_name_plural = 'Penalite Retard'
        app_label = 'api_sm'



class DetailFacture(DeleteMixin,models.Model):
    id = models.AutoField(db_column='Id_Df', primary_key=True)
    facture=models.ForeignKey(Factures,on_delete=models.DO_NOTHING,null=True,to_field="numero_facture",db_column='Num_Facture')
    detail=models.ForeignKey(Attachements,on_delete=models.DO_NOTHING,db_column='Detail',null=True)

    est_bloquer = models.BooleanField(db_column='Est_Bloquer', default=False,
                                      editable=False)
    user_id = models.CharField(db_column='User_ID', max_length=15, editable=False,default=get_current_user)
    date_modification = models.DateTimeField(db_column='Date_Modification', auto_now=True)
    objects = GeneralManager()

    class Meta:
        managed=False
        db_table='Detail_Facture'
        verbose_name = 'Datails Facture'
        verbose_name_plural = 'Details Facture'
        app_label = 'api_sm'



class ModePaiement(DeleteMixin,models.Model):
    id=models.CharField(db_column='Id_Mode', primary_key=True,max_length=3)
    libelle=models.CharField(max_length=500,null=False,unique=True)

    est_bloquer = models.BooleanField(db_column='Est_Bloquer', default=False,
                                      editable=False)
    user_id = models.CharField(db_column='User_ID', max_length=15, editable=False,default=get_current_user)
    date_modification = models.DateTimeField(db_column='Date_Modification', auto_now=True)
    objects = GeneralManager()
    def __str__(self):
        return  self.libelle
    class Meta:
        managed=False
        db_table='Mode_Paiement'
        verbose_name = 'Mode de Paiement'
        verbose_name_plural = 'Mode de Paiement'
        app_label = 'api_sm'




class Encaissement(DeleteMixin,models.Model):
    id = models.AutoField(db_column='Id_Enc', primary_key=True)
    facture=models.ForeignKey(Factures,on_delete=models.DO_NOTHING,db_column='Facture',null=True,blank=True,verbose_name="N° Facture")
    date_encaissement=models.DateField(null=False,db_column='Date_Encaissement',verbose_name="Date d'encaissement")
    mode_paiement=models.ForeignKey(ModePaiement,on_delete=models.DO_NOTHING,db_column='Mode_Paiement',null=False,verbose_name="Mode de Paiement")
    montant_encaisse=models.FloatField( db_column='Montant_Encaisse',blank=True,verbose_name="Montant Encaissé",
                                     validators=[MinValueValidator(0)], default=0)
    agence = models.ForeignKey('api_sch.TabAgence',on_delete=models.DO_NOTHING,db_column='Agence' , null=True, verbose_name='Agence')

    numero_piece = models.CharField(db_column='Numero_Piece',max_length=300,null=False,verbose_name="Numero de piéce")

    est_bloquer = models.BooleanField(db_column='Est_Bloquer', default=False,
                                      editable=False)
    user_id = models.CharField(db_column='User_ID', max_length=15, editable=False,default=get_current_user)
    date_modification = models.DateTimeField(db_column='Date_Modification', auto_now=True)
    objects = GeneralManager()

    def delete(self, *args, **kwargs):
        username = str(get_current_user())
        id_Enc=self.id
        sql_query = f"""
                UPDATE Encaissements SET Est_Bloquer= 1 , User_ID ='{username}',Date_Modification= GETDATE() WHERE Id_Enc ={id_Enc}
               """
        with connection.cursor() as cursor:
            cursor.execute(sql_query)

    @property
    def montant_creance(self):
        try:
            enc = float(Encaissement.objects.filter(facture=self.facture, date_encaissement__lt=self.date_encaissement).aggregate(
                models.Sum('montant_encaisse'))[
                "montant_encaisse__sum"] or 0.0)

            if (enc == None):
                enc = float(self.montant_encaisse)
            else:
                enc += float(self.montant_encaisse)

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



class TypeCaution(DeleteMixin,models.Model):
    id= models.CharField(db_column='Id_Type_Caution', primary_key=True, max_length=5)  


    libelle = models.CharField(max_length=500,null=True,blank=True)
    type_avance = models.ForeignKey(TypeAvance, on_delete=models.DO_NOTHING, null=True,blank=True, to_field='id',
                             verbose_name="Type d'avance",db_column='Type_Avance',)
    taux_exact= models.FloatField(db_column='Taux_Exact',
                                   validators=[MinValueValidator(0), MaxValueValidator(100)], null=True,blank=True)
    taux_min = models.FloatField(db_column='Taux_Min',
                               validators=[MinValueValidator(0), MaxValueValidator(100)], null=True,blank=True)
    taux_max = models.FloatField(db_column='Taux_Max',
                                   validators=[MinValueValidator(0), MaxValueValidator(100)], null=True,blank=True)


    est_bloquer = models.BooleanField(db_column='Est_Bloquer', default=False,
                                      editable=False)
    user_id = models.CharField(db_column='User_ID', max_length=15, editable=False,default=get_current_user)
    date_modification = models.DateTimeField(db_column='Date_Modification', auto_now=True)
    objects = GeneralManager()
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


class Cautions(DeleteMixin,models.Model):
    id = models.CharField(db_column='Id_Caution', primary_key=True, max_length=30)

    marche = models.ForeignKey(Marche,db_column='Num_Marche', on_delete=models.DO_NOTHING, null=True, related_name="Caution_Marche",to_field='id')
    type = models.ForeignKey(TypeCaution,db_column='Type_Caution', on_delete=models.DO_NOTHING, null=False,verbose_name="Type",to_field='')
    avance = models.ForeignKey(Avance,db_column='Avance', on_delete=models.DO_NOTHING, null=True, blank=True,verbose_name='Avance')
    date_soumission = models.DateField(db_column='Date_Soumission',null=False,verbose_name="Date dépot")
    agence = models.ForeignKey('api_sch.TabAgence',db_column='Agence', on_delete=models.CASCADE,verbose_name="Agence")
    montant = models.FloatField(
        verbose_name="Montant",
        validators=[MinValueValidator(0)], default=0,
    )
    est_recupere = models.BooleanField(db_column='Est_Recupere',default=False, null=False,verbose_name='Est Recuperée')

    est_bloquer = models.BooleanField(db_column='Est_Bloquer', default=False,
                                      editable=False)
    user_id = models.CharField(db_column='User_ID', max_length=15, editable=False,default=get_current_user)
    date_modification = models.DateTimeField(db_column='Date_Modification', auto_now=True)
    objects = GeneralManager()
    class Meta:
        managed=False
        db_table='Cautions'
        verbose_name = 'Caution'
        verbose_name_plural = 'Caution'
        app_label = 'api_sm'



