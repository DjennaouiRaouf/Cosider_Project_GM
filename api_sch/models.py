from django.db import models




class TabProduction(models.Model):
    id_production = models.AutoField(db_column='ID_Production', primary_key=True,verbose_name='ID')
    code_type_production = models.CharField(max_length=2,null=False, db_column='Code_Type_Production',verbose_name='Type Production')
    code_site = models.CharField(max_length=500,null=False, db_column='Code_site',verbose_name='Code Site')
    code_filiale = models.CharField(db_column='Code_Filiale', max_length=5, blank=True, null=True,verbose_name='Code Filiale')
    nt = models.CharField(max_length=20, db_column='NT',  blank=True, null=True,verbose_name='NT')
    code_groupeactivite = models.CharField(max_length=4, db_column='Code_GroupeActivite',blank=True, null=True,verbose_name="Code groupe d'activité")
    code_activite = models.CharField(max_length=4, db_column='Code_Activite', blank=True, null=True,verbose_name="Code Activité")
    code_tache = models.CharField(max_length=30, db_column='Code_Tache', blank=True, null=True,verbose_name="Code Tache")
    recepteur = models.CharField(db_column='Recepteur', max_length=20, blank=True, null=True,verbose_name="Recepteur")
    code_produit = models.CharField(max_length=4, db_column='Code_Produit', blank=True, null=True,verbose_name="Code Produit")
    code_unite_mesure = models.CharField(max_length=4, db_column='Code_Unite_Mesure', blank=True, null=True,verbose_name='Unite')
    type_prestation = models.SmallIntegerField(db_column='Type_Prestation', blank=True, null=True,verbose_name='Type Prestation')
    mmaa = models.DateField(db_column='Mmaa')
    quantite_1 = models.FloatField(db_column='Quantite_1', blank=True, null=True,verbose_name='Quantite')
    valeur_1 = models.DecimalField(db_column='Valeur_1', max_digits=19, decimal_places=4, blank=True, null=True,verbose_name='Valeur')
    quantite_2 = models.FloatField(db_column='Quantite_2', blank=True, null=True,verbose_name='Quantite')
    valeur_2 = models.DecimalField(db_column='Valeur_2', max_digits=19, decimal_places=4, blank=True, null=True,verbose_name='Valeur')
    quantite_3 = models.FloatField(db_column='Quantite_3', blank=True, null=True,verbose_name='Quantite')
    valeur_3 = models.DecimalField(db_column='Valeur_3', max_digits=19, decimal_places=4, blank=True, null=True,verbose_name='Valeur')
    prevu_realiser = models.CharField(db_column='Prevu_Realiser', max_length=1)
    est_cloturer = models.BooleanField(db_column='Est_Cloturer', blank=True, null=True)
    user_id = models.CharField(db_column='User_ID', max_length=15, blank=True, null=True)
    date_modification = models.DateTimeField(db_column='Date_Modification', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Tab_Production'
        app_label = 'api_sch'




class TabAgence(models.Model):
    id = models.CharField(db_column='Code_Agence', primary_key=True, max_length=15)
    code_banque = models.ForeignKey('TabBanque', models.DO_NOTHING, db_column='Code_banque')  
    libelle= models.CharField(db_column='Libelle_Agence', max_length=50)  
    compte_comptable = models.CharField(db_column='Compte_Comptable', max_length=10, blank=True, null=True)  
    est_bloquer = models.BooleanField(db_column='Est_Bloquer', blank=True, null=True)  
    user_id = models.CharField(db_column='User_ID', max_length=15, blank=True, null=True)  
    date_modification = models.DateTimeField(db_column='Date_Modification', blank=True, null=True)  


    class Meta:
        managed = False
        db_table = 'Tab_agence'
        app_label = 'api_sch'

    def __str__(self):
        return self.id + " - " + self.libelle


class TabBanque(models.Model):
    code_banque = models.CharField(db_column='Code_Banque', primary_key=True, max_length=15)  
    libelle = models.CharField(db_column='Libelle_Banque', max_length=50, blank=True, null=True)  
    acronyme = models.CharField(db_column='Acronyme', max_length=20, blank=True, null=True)  
    est_bloquer = models.BooleanField(db_column='Est_Bloquer', blank=True, null=True)  
    user_id = models.CharField(db_column='User_ID', max_length=15, blank=True, null=True)  
    date_modification = models.DateTimeField(db_column='Date_Modification', blank=True, null=True)  

    class Meta:
        managed = False
        db_table = 'tab_banque'
        app_label = 'api_sch'



class TabFiliale(models.Model):
    id = models.CharField(db_column='Code_Filiale', primary_key=True, max_length=5)
    code_entreprise=models.CharField(max_length=2,null=False, db_column='Code_Entreprise')
    libelle = models.CharField(db_column='Libelle_Filiale', max_length=50, blank=True, null=True)

    def __str__(self):
        return str(self.id)
    class Meta:
        managed = False
        db_table = 'Tab_filiale'
        app_label = 'api_sch'



class TabUniteDeMesure(models.Model):
    id = models.CharField(db_column='Code_Unite_Mesure', primary_key=True, max_length=4)  # Field name made lowercase.
    libelle = models.CharField(db_column='Symbole_Unite', max_length=10, blank=True, null=True)  # Field name made lowercase.
    libelle_unite = models.CharField(db_column='Libelle_Unite', max_length=50, blank=True, null=True)  # Field name made lowercase.
    est_bloquer = models.BooleanField(db_column='Est_Bloquer', blank=True, null=True)  # Field name made lowercase.
    user_id = models.CharField(db_column='User_ID', max_length=15, blank=True, null=True)  # Field name made lowercase.
    date_modification = models.DateTimeField(db_column='Date_Modification', blank=True, null=True)  # Field name made lowercase.


    def __str__(self):
        return str(self.libelle)
    class Meta:
        managed = False
        db_table = 'Tab_Unite_de_mesure'

    def __str__(self):
        return self.libelle



class TabSituationNt(models.Model):
    id = models.CharField(db_column='Code_Situation_NT', primary_key=True, max_length=2)  # Field name made lowercase.
    libelle = models.CharField(db_column='Libelle_Situation_NT', max_length=50, blank=True, null=True)  # Field name made lowercase.
    est_bloquer = models.BooleanField(db_column='Est_Bloquer', blank=True, null=True)  # Field name made lowercase.
    user_id = models.CharField(db_column='User_ID', max_length=15, blank=True, null=True)  # Field name made lowercase.
    date_modification = models.DateTimeField(db_column='Date_Modification', blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return str(self.id)
    class Meta:
        managed = False
        db_table = 'Tab_Situation_NT'





class TabDivision(models.Model):
    id = models.CharField(db_column='Code_Division', primary_key=True, max_length=15)  # Field name made lowercase.
    code_filiale = models.ForeignKey('TabFiliale', models.DO_NOTHING, db_column='Code_Filiale', blank=True, null=True)  # Field name made lowercase.
    libelle = models.CharField(db_column='Libelle_Division', max_length=100, blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return str(self.libelle)
    class Meta:
        managed = False
        db_table = 'Tab_Division'


class TabCommune(models.Model):
    id = models.CharField(db_column='Code_Commune_Ons', primary_key=True, max_length=10)  # Field name made lowercase.
    libelle = models.CharField(db_column='Libelle_Commune', max_length=50, blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return str(self.libelle)
    class Meta:
        managed = False
        db_table = 'Tab_Commune'



