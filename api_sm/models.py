from datetime import datetime

from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.dispatch import receiver
from safedelete import SOFT_DELETE_CASCADE, DELETED_VISIBLE_BY_PK, SOFT_DELETE, HARD_DELETE
from safedelete.managers import SafeDeleteManager
from safedelete.models import SafeDeleteModel
from simple_history.models import HistoricalRecords
from simple_history.signals import pre_create_historical_record



class DeletedModelManager(SafeDeleteManager):
    _safedelete_visibility = DELETED_VISIBLE_BY_PK


# Create your models here.
class Images(SafeDeleteModel):
    _safedelete_policy = SOFT_DELETE_CASCADE
    Types = [
        ('H', 'Home'),
        ('L', 'Login'),

    ]
    key = models.BigAutoField(primary_key=True)
    src = models.ImageField(upload_to="Images/Images", null=False, blank=True, default='default.png')
    type=models.CharField(max_length=100,null=False,blank=True,choices=Types)
    objects = DeletedModelManager()
    class Meta:
        verbose_name = 'Images'
        verbose_name_plural = 'Images'
        app_label = 'api_sm'


class TimeLine(SafeDeleteModel):
    _safedelete_policy = SOFT_DELETE_CASCADE

    key = models.BigAutoField(primary_key=True)
    year = models.PositiveIntegerField(default=datetime.now().year,null=False,blank=True)
    title = models.CharField(max_length=100, null=False, blank=True)
    description=models.TextField(max_length=300,null=False, blank=True,)
    objects = DeletedModelManager()

    class Meta:
        verbose_name = 'TimeLine'
        verbose_name_plural = 'TimeLine'
        app_label = 'api_sm'


class OptionImpression(SafeDeleteModel):
    Types = [
        ('H', 'Header'),
        ('F', 'Footer'),
        ('L', 'Logo'),

    ]
    _safedelete_policy = SOFT_DELETE_CASCADE
    key = models.BigAutoField(primary_key=True)
    src = models.ImageField(upload_to="Images/Impression", null=False, blank=True)
    type=models.CharField( max_length=20,
        choices=Types, unique=True,null=False)
    objects = DeletedModelManager()
    class Meta:
        verbose_name = 'Option d\'Impression'
        verbose_name_plural = 'Option d\'Impression'
        app_label = 'api_sm'
        










class Clients(SafeDeleteModel):
    _safedelete_policy = SOFT_DELETE_CASCADE
    id = models.CharField(db_column='Code_Client', primary_key=True, max_length=500, verbose_name='Code du Client')
    type_client = models.PositiveSmallIntegerField(db_column='Type_Client', blank=True, null=True ,verbose_name='Type de Client')
    est_client_cosider = models.BooleanField(db_column='Est_Client_Cosider', blank=True, null=False
                                             ,verbose_name='Est Client Cosider')
    libelle = models.CharField(db_column='Libelle_Client', max_length=300, blank=True, null=True,
                                      verbose_name='Libelle')

    adresse = models.CharField(db_column='adresse', max_length=500, blank=True, null=True,
                                      verbose_name='Adresse')


    nif = models.CharField(db_column='NIF', unique=True, max_length=50, blank=True, null=True,verbose_name='NIF')
    raison_social = models.CharField(db_column='Raison_Social', max_length=50, blank=True, null=True,verbose_name='Raison Social')
    num_registre_commerce = models.CharField(db_column='Num_Registre_Commerce', max_length=20, blank=True, null=True,
                                             verbose_name='Numero du registre de commerce')

    objects = DeletedModelManager()
    def __str__(self):
        return  self.id



    class Meta:
        verbose_name = 'Clients'
        verbose_name_plural = 'Clients'
        app_label = 'api_sm'
        


class Sites(SafeDeleteModel):
    _safedelete_policy = SOFT_DELETE_CASCADE
    id = models.CharField(db_column='Code_site', primary_key=True, max_length=500 ,
                                 verbose_name='Code du Site')
    responsable_site = models.CharField(db_column='Responsable', max_length=500, blank=True, null=True,
                                 verbose_name='Responsable du Site')
    libelle = models.CharField(db_column='Libelle_Site', max_length=500, blank=True, null=True,
                                 verbose_name='Libelle du Site')
    type_site = models.PositiveSmallIntegerField(db_column='Type_Site', blank=True, null=True,
                                 verbose_name='Type du Site')

    code_filiale = models.CharField(db_column='Code_Filiale', max_length=50,blank=True, null=True,
                                 verbose_name='Code Filiale')
    code_division = models.CharField(db_column='Code_Division', max_length=50, blank=True, null=True,
                                 verbose_name='Code division')

    code_region = models.CharField(db_column='Code_Region', max_length=20, blank=True, null=True,
                                 verbose_name='Code région')
    code_commune_site = models.CharField(db_column='Code_Commune_Site', max_length=50, blank=True, null=True,
                                 verbose_name='Code commune')

    date_ouverture_site = models.DateField(db_column='Date_Ouverture_Site', blank=True, null=True,
                                 verbose_name='Ouverture')
    date_cloture_site = models.DateField(db_column='Date_Cloture_Site', blank=True, null=True,
                                 verbose_name='Cloture')


    objects = DeletedModelManager()

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
        verbose_name = 'Sites'
        verbose_name_plural = 'Sites'
        app_label = 'api_sm'
        








class NT(SafeDeleteModel):
    _safedelete_policy = SOFT_DELETE_CASCADE
    id=models.CharField(db_column='id',max_length=500,primary_key=True,verbose_name="id",editable=False)
    nt = models.CharField(db_column='NT', max_length=20, verbose_name='Numero du travail')
    code_situation = models.ForeignKey('api_sch.TabSituationNt',on_delete=models.DO_NOTHING,db_constraint=False , blank=True, null=True
                                       , verbose_name='Situation')
    libelle = models.CharField(max_length=900, db_column='Libelle_NT', blank=True, null=True
                               , verbose_name='Libelle')
    date_ouverture_nt = models.DateField(db_column='Date_Ouverture_NT', blank=True, null=True
                                         , verbose_name='Ouverture')
    date_cloture_nt = models.DateField(db_column='Date_Cloture_NT', blank=True, null=True
                                       , verbose_name='Cloture')

    code_site = models.ForeignKey(Sites, on_delete=models.DO_NOTHING, db_column='Code_site', null=False
                                  , verbose_name='Code du Site')
    code_client = models.ForeignKey(Clients, on_delete=models.DO_NOTHING, db_column='Code_Client',null=True
                                    , verbose_name='Code du client')



    objects = DeletedModelManager()

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = 'Numero du travail'
        verbose_name_plural = 'Numero du travail'
        unique_together = (('code_site', 'nt'),)
        app_label = 'api_sm'
        





class Marche(SafeDeleteModel):
    _safedelete_policy = SOFT_DELETE_CASCADE

    id=models.CharField(max_length=500,primary_key=True,verbose_name='Code du Contrat')
    nt = models.ForeignKey(NT, on_delete=models.DO_NOTHING, db_column='nt', null=False
                           , verbose_name='Numero Travail',to_field="id")

    libelle = models.CharField(null=False, max_length=500
                               , verbose_name='Libelle')
    ods_depart = models.DateField(null=False, blank=True
                                  , verbose_name='ODS de démarrage')
    delais = models.PositiveIntegerField(default=0, null=False
                                         , verbose_name='Délai des travaux')
    revisable = models.BooleanField(default=True, null=False
                                    , verbose_name='Est-il révisable ?')
    delai_paiement_f=models.PositiveIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(100)],
                                         null=True
                                                 , verbose_name='Délai de paiement')
    rabais =  models.DecimalField(default=0, max_digits=38, decimal_places=2, verbose_name='Taux de rabais',
                              validators=[MinValueValidator(0), MaxValueValidator(100)], null=False)
    tva = models.DecimalField(default=0, max_digits=38, decimal_places=2, verbose_name='TVA',
                              validators=[MinValueValidator(0), MaxValueValidator(100)], null=False)
    rg = models.DecimalField(default=0, max_digits=38, decimal_places=2,
                             validators=[MinValueValidator(0), MaxValueValidator(100)], null=False
                             , verbose_name='Taux de retenue de garantie')



    date_signature = models.DateField(null=False, verbose_name='Date de signature')
   
    objects = DeletedModelManager()
    history = HistoricalRecords()

    @property
    def ht(self):
        try:
            dqes = DQE.objects.filter(marche=self.id)
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



class Meta:
        verbose_name = 'Marchés'
        verbose_name_plural = 'Marchés'
        app_label = 'api_sm'
        





class DQE(SafeDeleteModel): # le prix final
    _safedelete_policy = SOFT_DELETE_CASCADE
    id=models.CharField(db_column='id',max_length=500,primary_key=True,verbose_name="id",editable=False)
    marche = models.ForeignKey(Marche,on_delete=models.DO_NOTHING,  null=False,related_name="marche_dqe",
                               to_field="id",verbose_name="Code du marché")
    code_tache = models.CharField(db_column='Code_Tache',null=False, max_length=30
                                  ,verbose_name="Code de la tache")
    libelle = models.TextField(db_column='Libelle_Tache',verbose_name="Libelle")
    unite =models.ForeignKey('api_sch.TabUniteDeMesure',on_delete=models.DO_NOTHING,db_constraint=False , null=False, verbose_name='Unité de mesure')
    prix_u = models.DecimalField(
        max_digits=38, decimal_places=2,
        validators=[MinValueValidator(0)], default=0
        , verbose_name='Prix unitaire'
    )
    est_tache_composite = models.BooleanField(db_column='Est_Tache_Composite', blank=True,
                                              null=False,default=False,verbose_name="Tache composée")
    est_tache_complementaire = models.BooleanField(db_column='Est_Tache_Complementaire', blank=True,
                                                   null=False,default=False,verbose_name="Tache complementaire")
    quantite = models.DecimalField(max_digits=38, decimal_places=2, validators=[MinValueValidator(0)], default=0,verbose_name='Quantité')

    aug_dim= models.DecimalField(max_digits=38, decimal_places=2, default=0,verbose_name='Augmentation/Diminution')
    
    objects = DeletedModelManager()

    @property
    def prix_q(self):
        return round(self.quantite * self.prix_u, 4)


    def __str__(self):
        return (str(self.id))



    class Meta:
        verbose_name = 'DQE'
        verbose_name_plural = 'DQE'
        app_label = 'api_sm'
        permissions = [
            ("upload_dqe", "Can upload DQE"),
            ("download_dqe", "Can download DQE"),

        ]
        





class Ordre_De_Service(SafeDeleteModel):
    _safedelete_policy = SOFT_DELETE_CASCADE
    Types = [
        ('Interruption', 'Interruption'),
        ('Reprise', 'Interruption'),

    ]
    marche = models.ForeignKey(Marche, on_delete=models.DO_NOTHING, null=True, related_name="ods_marche")
    date = models.DateField(null=True,blank=True,verbose_name='Date Interruption')
    rep_int=models.CharField(null=False,default='Interruption',max_length=300,choices=Types,verbose_name='Reprise/Interruption')
    motif = models.TextField(null=True, blank=True,verbose_name='Motif')

    objects = DeletedModelManager()




    class Meta:
        verbose_name = 'Ordre de service'
        verbose_name_plural = 'Ordre de service'
        app_label = 'api_sm'
        











class TypeAvance(SafeDeleteModel):
    _safedelete_policy = SOFT_DELETE_CASCADE
    libelle = models.CharField(max_length=500, null=False, unique=True)
    taux_max = models.DecimalField(default=0, max_digits=38, decimal_places=2,
                                                 validators=[MinValueValidator(0), MaxValueValidator(100)], null=False)



    objects = DeletedModelManager()

    def __str__(self):
        return self.libelle



    class Meta:
        verbose_name = 'Type Avance'
        verbose_name_plural = 'Type Avance'
        app_label = 'api_sm'
        


class Avance(SafeDeleteModel):
    _safedelete_policy = SOFT_DELETE_CASCADE
    type = models.ForeignKey(TypeAvance, on_delete=models.DO_NOTHING, null=False, to_field='id',
                             verbose_name="Type d'avance")
    num_avance = models.PositiveIntegerField(default=0, null=False, blank=True, editable=False,
                                                verbose_name="Numero d'avance")
    marche = models.ForeignKey(Marche, on_delete=models.DO_NOTHING, null=False, related_name="Avance_Marche",to_field='id')

    taux_avance = models.DecimalField(default=0, max_digits=38, decimal_places=2, verbose_name="Taux d'avance", editable=False,
                                      validators=[MinValueValidator(0), MaxValueValidator(100)], null=False)


    montant = models.DecimalField(max_digits=38, decimal_places=2, validators=[MinValueValidator(0)], default=0,null=False,verbose_name='Montant d\'avance')

    fin=models.DecimalField(default=80, max_digits=38, decimal_places=2, verbose_name="% Fin",
                                      validators=[MinValueValidator(0), MaxValueValidator(100)], null=False)









    date=models.DateField(null=False,verbose_name="Date d'avance")
    remboursee = models.BooleanField(default=False, null=False,verbose_name='Est Remboursée')


    objects = DeletedModelManager()

    def __str__(self):
        return str(self.marche)+"-"+self.type.libelle+'-'+str(self.num_avance)
    class Meta:
        verbose_name = 'Avance'
        verbose_name_plural = 'Avances'

        app_label = 'api_sm'
        





class Attachements(SafeDeleteModel):
    _safedelete_policy = SOFT_DELETE_CASCADE
    marche=models.ForeignKey(Marche, on_delete=models.DO_NOTHING,null=False, blank=False)
    dqe = models.ForeignKey(DQE, on_delete=models.DO_NOTHING)# item + quantité marche + prix unitaire
    qte = models.DecimalField(max_digits=38, decimal_places=2, validators=[MinValueValidator(0)], default=0,verbose_name='Quantité Mois')
    prix_u = models.DecimalField(max_digits=38, decimal_places=2, validators=[MinValueValidator(0)], default=0,
                                     editable=False,verbose_name='Prix unitaire')
    montant= models.DecimalField(max_digits=38, decimal_places=2, validators=[MinValueValidator(0)], default=0,verbose_name='Montant du Mois',editable=False)
    date=models.DateField(null=False,verbose_name='Date')
    objects = DeletedModelManager()

    @property
    def qte_cumule(self):
        try:
            previous_cumule = Attachements.objects.filter(dqe=self.dqe,date__lt=self.date)
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
            previous_cumule = Attachements.objects.filter(dqe=self.dqe, date__lt=self.date)
            sum = 0
            if (previous_cumule):
                for pc in previous_cumule:
                    sum += pc.qte
                return sum
            else:
                return 0
        except Attachements.DoesNotExist:
            return 0
    @property
    def montant_precedent(self):
        try:
            previous_cumule = Attachements.objects.filter(dqe=self.dqe, date__lt=self.date)
            sum = 0
            if (previous_cumule):
                for pc in previous_cumule:
                    sum += pc.montant
                return sum
            else:
                return 0
        except Attachements.DoesNotExist:
            return 0

    @property
    def montant_cumule(self):
        try:
            previous_cumule = Attachements.objects.filter(dqe=self.dqe,date__lt=self.date)
            sum = self.montant
            if (previous_cumule):
                for pc in previous_cumule:
                    sum += pc.montant
                return sum
            else:
                return self.montant
        except Attachements.DoesNotExist:
            return self.montant

    def __str__(self):
        return  str(self.id)+"-"+self.dqe.code_tache


    class Meta:
        verbose_name = 'Attachements'
        verbose_name_plural = 'Attachements'
        unique_together=(('dqe','date'),)
        app_label = 'api_sm'
        


class Factures(SafeDeleteModel):
    _safedelete_policy = SOFT_DELETE_CASCADE
    numero_facture=models.CharField(max_length=800,primary_key=True,verbose_name='Numero de facture')
    num_situation=models.IntegerField(null=False,verbose_name='Numero de situation')
    marche=models.ForeignKey(Marche,on_delete=models.DO_NOTHING,null=False,verbose_name='Marche',to_field="id")
    du = models.DateField(null=False,verbose_name='Du')
    au = models.DateField(null=False,verbose_name='Au')
    paye = models.BooleanField(default=False, null=False,editable=False)
    date = models.DateField(auto_now=True, editable=False)
    montant= models.DecimalField(max_digits=38, decimal_places=2, validators=[MinValueValidator(0)], default=0,
                                      verbose_name="Montant du Mois"
                                      ,editable=False)

    montant_rb = models.DecimalField(max_digits=38, decimal_places=2, validators=[MinValueValidator(0)], default=0,
                                       verbose_name="Montant du rabais"
                                       , editable=False) #montant du rabais du mois


    montant_rg=models.DecimalField(max_digits=38, decimal_places=2, validators=[MinValueValidator(0)], default=0,
                                         verbose_name="Montant Retenue de garantie"
                                         ,editable=False) #retenue de garantie le montant du mois

    montant_avf_remb=models.DecimalField(max_digits=38, decimal_places=2, validators=[MinValueValidator(0)], default=0,
                                         verbose_name="Montant d'avance forfaitaire remboursé"
                                         ,editable=False)
    montant_ava_remb = models.DecimalField(max_digits=38, decimal_places=2, validators=[MinValueValidator(0)], default=0,
                                          verbose_name="Montant d'avance appros remboursé"
                                          , editable=False)

    montant_factureHT=models.DecimalField(max_digits=38, decimal_places=2, validators=[MinValueValidator(0)], default=0,
                                         verbose_name="Montant de la facture HT"
                                         ,editable=False)

    montant_factureTTC=models.DecimalField(max_digits=38, decimal_places=2, validators=[MinValueValidator(0)], default=0,
                                         verbose_name="Montant de la facture TTC"
                                         ,editable=False)

    taux_realise=models.DecimalField(max_digits=38,decimal_places=2,validators=[MinValueValidator(0),MinValueValidator(100)], default=0,
                                         verbose_name="Taux Realisé"
                                         ,editable=False)

    is_remb=models.BooleanField(default=False,null=False,editable=False,verbose_name='Remboursement Effectué')

    objects = DeletedModelManager()

    @property
    def montant_precedent(self):
        try:
            previous_cumule = Factures.objects.filter(marche=self.marche, date__lt=self.date)
            sum = 0
            if (previous_cumule):
                for pc in previous_cumule:
                    sum += pc.montant
                return sum
            else:
                return 0
        except Factures.DoesNotExist:
            return 0

    @property
    def montant_cumule(self):
        try:
            previous_cumule = Factures.objects.filter(marche=self.marche, date__lt=self.date)
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
        verbose_name = 'Factures'
        verbose_name_plural = 'Factures'
        app_label = 'api_sm'
        
class Remboursement(SafeDeleteModel):
    _safedelete_policy = SOFT_DELETE_CASCADE
    facture = models.ForeignKey(Factures, on_delete=models.DO_NOTHING, null=True, blank=True, to_field="numero_facture")
    avance=models.ForeignKey(Avance, on_delete=models.DO_NOTHING, null=True, blank=True)

    montant =models.DecimalField(max_digits=38, decimal_places=2, validators=[MinValueValidator(0)], default=0,
                                         verbose_name="Montant Mois"
                                         ,editable=False)

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



    objects = DeletedModelManager()



    class Meta:
        verbose_name = 'Remboursement'
        verbose_name_plural = 'Remboursements'
        app_label = 'api_sm'
        unique_together=(('facture','avance'),)



class DetailFacture(SafeDeleteModel):
    _safedelete_policy = SOFT_DELETE_CASCADE
    facture=models.ForeignKey(Factures,on_delete=models.DO_NOTHING,null=True,blank=True,to_field="numero_facture")
    detail=models.ForeignKey(Attachements,on_delete=models.DO_NOTHING)
    objects = DeletedModelManager()

    class Meta:
        verbose_name = 'Datails Facture'
        verbose_name_plural = 'Details Facture'
        app_label = 'api_sm'
        


class ModePaiement(SafeDeleteModel):
    _safedelete_policy = SOFT_DELETE_CASCADE
    libelle=models.CharField(max_length=500,null=False,unique=True)

    def __str__(self):
        return  self.libelle
    class Meta:
        verbose_name = 'Mode de Paiement'
        verbose_name_plural = 'Mode de Paiement'
        app_label = 'api_sm'
        



class Encaissement(SafeDeleteModel):
    _safedelete_policy = SOFT_DELETE_CASCADE

    facture=models.ForeignKey(Factures,on_delete=models.DO_NOTHING,null=True,blank=True,verbose_name="Facture")
    date_encaissement=models.DateField(null=False,verbose_name="Date d'encaissement")
    mode_paiement=models.ForeignKey(ModePaiement,on_delete=models.DO_NOTHING,null=False,verbose_name="Mode de paiement")
    montant_encaisse=models.DecimalField(max_digits=38, decimal_places=2, blank=True,verbose_name="Montant encaissé",
                                     validators=[MinValueValidator(0)], default=0)
    agence = models.ForeignKey('api_sch.TabAgence',on_delete=models.DO_NOTHING,db_constraint=False , null=True, verbose_name='Agence')

    numero_piece = models.CharField(max_length=300,null=False,verbose_name="Numero de piéce")

    objects = DeletedModelManager()

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
        verbose_name = 'Encaissement'
        verbose_name_plural = 'Encaissement'
        unique_together=(("facture","date_encaissement"),)
        app_label = 'api_sm'



class TypeCaution(SafeDeleteModel):
    _safedelete_policy = SOFT_DELETE_CASCADE
    libelle = models.CharField(max_length=500,null=True,blank=True)
    type_avance = models.ForeignKey(TypeAvance, on_delete=models.DO_NOTHING, null=True,blank=True, to_field='id',
                             verbose_name="Type d'avance")
    taux_exact= models.DecimalField(max_digits=38, decimal_places=2,
                                   validators=[MinValueValidator(0), MaxValueValidator(100)], null=True,blank=True)
    taux_min = models.DecimalField(max_digits=38, decimal_places=2,
                               validators=[MinValueValidator(0), MaxValueValidator(100)], null=True,blank=True)
    taux_max = models.DecimalField( max_digits=38, decimal_places=2,
                                   validators=[MinValueValidator(0), MaxValueValidator(100)], null=True,blank=True)

    objects = DeletedModelManager()

    def __str__(self):
        return self.libelle

    def save(self, *args, **kwargs):
        super(TypeCaution, self).save(*args, **kwargs)



    class Meta:
        verbose_name = 'Type_Caution'
        verbose_name_plural = 'Type_Caution'
        app_label = 'api_sm'


class Cautions(SafeDeleteModel):
    _safedelete_policy = SOFT_DELETE_CASCADE
    marche = models.ForeignKey(Marche, on_delete=models.DO_NOTHING, null=False, related_name="Caution_Marche")
    type = models.ForeignKey(TypeCaution, on_delete=models.DO_NOTHING, null=False)
    avance = models.ForeignKey(Avance, on_delete=models.DO_NOTHING, null=True, blank=True)
    date_soumission = models.DateField(null=False,verbose_name="Date dépot")
    taux = models.DecimalField(default=0,max_digits=38, decimal_places=2,
                                     validators=[MinValueValidator(0), MaxValueValidator(100)], null=False)
    agence = models.ForeignKey('api_sch.TabAgence', on_delete=models.CASCADE, db_constraint=False)
    montant = models.DecimalField(
        max_digits=38, decimal_places=2,
        validators=[MinValueValidator(0)], default=0,
        editable=False
    )
    est_recupere = models.BooleanField(default=False, null=False,verbose_name='Est Recuperée')

    objects = DeletedModelManager()


    class Meta:
        verbose_name = 'Caution'
        verbose_name_plural = 'Caution'
        app_label = 'api_sm'




'''
CREATE VIEW Tab_Banque AS
SELECT * FROM CA_CH.dbo.Tab_Banque;

CREATE VIEW Tab_Agence AS
SELECT * FROM CA_CH.dbo.Tab_Agence;

CREATE VIEW Tab_Unite_de_Mesure AS
SELECT * FROM CA_CH.dbo.Tab_Unite_de_Mesure
;

CREATE VIEW Tab_Situation_NT AS
SELECT * FROM CA_CH.dbo.Tab_Situation_NT
;



'''