# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Activite(models.Model):
    code_activite = models.CharField(db_column='Code_Activite', max_length=5)  # Field name made lowercase.
    code_ac = models.CharField(db_column='CODE_AC', max_length=4, blank=True, null=True)  # Field name made lowercase.
    lib_lg_ac = models.CharField(db_column='LIB_LG_AC', max_length=255, blank=True, null=True)  # Field name made lowercase.
    lib_cr_ac = models.CharField(db_column='LIB_CR_AC', max_length=255, blank=True, null=True)  # Field name made lowercase.
    unite_ac = models.CharField(db_column='UNITE_AC', max_length=4, blank=True, null=True)  # Field name made lowercase.
    existe = models.BooleanField(db_column='Existe', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ACTIVITE'


class Attachements(models.Model):
    id_attachement = models.AutoField(db_column='Id_Attachement', primary_key=True)  # Field name made lowercase.
    num_marche = models.ForeignKey('Marche', models.DO_NOTHING, db_column='Num_Marche', blank=True, null=True)  # Field name made lowercase.
    code_site = models.ForeignKey('TabNtTaches', models.DO_NOTHING, db_column='Code_Site', to_field='NT')  # Field name made lowercase.
    nt = models.ForeignKey('TabNtTaches', models.DO_NOTHING, db_column='NT', to_field='NT', related_name='attachements_nt_set')  # Field name made lowercase.
    code_tache = models.ForeignKey('TabNtTaches', models.DO_NOTHING, db_column='Code_Tache', to_field='NT', related_name='attachements_code_tache_set')  # Field name made lowercase.
    quantite = models.FloatField(db_column='Quantite', blank=True, null=True)  # Field name made lowercase.
    prix_unitaire = models.FloatField(db_column='Prix_Unitaire', blank=True, null=True)  # Field name made lowercase.
    montant = models.FloatField(db_column='Montant', blank=True, null=True)  # Field name made lowercase.
    mmaa = models.DateField(db_column='Mmaa')  # Field name made lowercase.
    est_bloquer = models.BooleanField(db_column='Est_Bloquer')  # Field name made lowercase.
    user_id = models.CharField(db_column='User_ID', max_length=15, blank=True, null=True)  # Field name made lowercase.
    date_modification = models.DateTimeField(db_column='Date_Modification', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Attachements'


class AuthToken(models.Model):
    key = models.CharField(primary_key=True, max_length=40)
    created = models.DateTimeField()
    user = models.OneToOneField('User', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'Auth_Token'


class Avances(models.Model):
    id_avance = models.AutoField(db_column='Id_Avance', primary_key=True)  # Field name made lowercase.
    num_avance = models.IntegerField(db_column='Num_Avance')  # Field name made lowercase.
    taux_avance = models.FloatField(db_column='Taux_Avance')  # Field name made lowercase.
    montant = models.FloatField(db_column='Montant')  # Field name made lowercase.
    debut = models.FloatField(db_column='Debut')  # Field name made lowercase.
    fin = models.FloatField(db_column='Fin')  # Field name made lowercase.
    date_avance = models.DateField(db_column='Date_Avance')  # Field name made lowercase.
    remboursee = models.BooleanField(db_column='Remboursee')  # Field name made lowercase.
    num_marche_field = models.ForeignKey('Marche', models.DO_NOTHING, db_column='Num_Marche ')  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    type_avance = models.ForeignKey('TypeAvance', models.DO_NOTHING, db_column='Type_Avance')  # Field name made lowercase.
    est_bloquer = models.BooleanField(db_column='Est_Bloquer')  # Field name made lowercase.
    user_id = models.CharField(db_column='User_ID', max_length=15, blank=True, null=True)  # Field name made lowercase.
    date_modification = models.DateTimeField(db_column='Date_Modification', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Avances'


class Cautions(models.Model):
    id_caution = models.AutoField(db_column='Id_Caution', primary_key=True)  # Field name made lowercase.
    date_soumission = models.DateField(db_column='Date_Soumission')  # Field name made lowercase.
    montant = models.FloatField(db_column='Montant')  # Field name made lowercase.
    est_recupere = models.BooleanField(db_column='Est_Recupere')  # Field name made lowercase.
    agence = models.ForeignKey('TabAgence', models.DO_NOTHING, db_column='Agence')  # Field name made lowercase.
    avance = models.ForeignKey(Avances, models.DO_NOTHING, db_column='Avance', blank=True, null=True)  # Field name made lowercase.
    num_marche = models.ForeignKey('Marche', models.DO_NOTHING, db_column='Num_Marche', blank=True, null=True)  # Field name made lowercase.
    type_caution = models.ForeignKey('TypeCaution', models.DO_NOTHING, db_column='Type_Caution')  # Field name made lowercase.
    est_bloquer = models.BooleanField(db_column='Est_Bloquer')  # Field name made lowercase.
    user_id = models.CharField(db_column='User_ID', max_length=15, blank=True, null=True)  # Field name made lowercase.
    date_modification = models.DateTimeField(db_column='Date_Modification', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Cautions'


class Client(models.Model):
    code_pole = models.CharField(db_column='Code_Pole', max_length=255, blank=True, null=True)  # Field name made lowercase.
    nt = models.FloatField(db_column='NT', blank=True, null=True)  # Field name made lowercase.
    libelle_nt = models.TextField(db_column='Libelle_NT', blank=True, null=True)  # Field name made lowercase.
    libelle_client = models.CharField(db_column='Libelle_Client', max_length=255, blank=True, null=True)  # Field name made lowercase.
    code_client = models.CharField(db_column='Code_Client', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Client'


class ContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'Content_Type'
        unique_together = (('app_label', 'model'),)


class DetailFacture(models.Model):
    id_df = models.AutoField(db_column='Id_Df', primary_key=True)  # Field name made lowercase.
    num_facture = models.ForeignKey('Factures', models.DO_NOTHING, db_column='Num_Facture', blank=True, null=True)  # Field name made lowercase.
    detail = models.ForeignKey(Attachements, models.DO_NOTHING, db_column='Detail')  # Field name made lowercase.
    est_bloquer = models.BooleanField(db_column='Est_Bloquer')  # Field name made lowercase.
    user_id = models.CharField(db_column='User_ID', max_length=15, blank=True, null=True)  # Field name made lowercase.
    date_modification = models.DateTimeField(db_column='Date_Modification', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Detail_Facture'


class Encaissements(models.Model):
    id_enc = models.BigAutoField(db_column='Id_Enc', primary_key=True)  # Field name made lowercase.
    date_encaissement = models.DateField(db_column='Date_Encaissement')  # Field name made lowercase.
    montant_encaisse = models.FloatField(db_column='Montant_Encaisse')  # Field name made lowercase.
    numero_piece = models.CharField(db_column='Numero_Piece', max_length=300)  # Field name made lowercase.
    agence = models.ForeignKey('TabAgence', models.DO_NOTHING, db_column='Agence', blank=True, null=True)  # Field name made lowercase.
    facture = models.ForeignKey('Factures', models.DO_NOTHING, db_column='Facture', blank=True, null=True)  # Field name made lowercase.
    mode_paiement = models.ForeignKey('ModePaiement', models.DO_NOTHING, db_column='Mode_Paiement')  # Field name made lowercase.
    est_bloquer = models.BooleanField(db_column='Est_Bloquer')  # Field name made lowercase.
    user_id = models.CharField(db_column='User_ID', max_length=15)  # Field name made lowercase.
    date_modification = models.DateTimeField(db_column='Date_Modification')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Encaissements'


class Flashp(models.Model):
    code_po = models.CharField(db_column='CODE_PO', max_length=4, blank=True, null=True)  # Field name made lowercase.
    code_nt = models.CharField(db_column='CODE_NT', max_length=4, blank=True, null=True)  # Field name made lowercase.
    code_ac = models.CharField(db_column='CODE_AC', max_length=4, blank=True, null=True)  # Field name made lowercase.
    annee = models.CharField(db_column='ANNEE', max_length=4, blank=True, null=True)  # Field name made lowercase.
    vp_st_1 = models.FloatField(db_column='VP_ST_1', blank=True, null=True)  # Field name made lowercase.
    vp_st_2 = models.FloatField(db_column='VP_ST_2', blank=True, null=True)  # Field name made lowercase.
    vp_st_3 = models.FloatField(db_column='VP_ST_3', blank=True, null=True)  # Field name made lowercase.
    vp_st_4 = models.FloatField(db_column='VP_ST_4', blank=True, null=True)  # Field name made lowercase.
    vp_st_5 = models.FloatField(db_column='VP_ST_5', blank=True, null=True)  # Field name made lowercase.
    vp_st_6 = models.FloatField(db_column='VP_ST_6', blank=True, null=True)  # Field name made lowercase.
    vp_st_7 = models.FloatField(db_column='VP_ST_7', blank=True, null=True)  # Field name made lowercase.
    vp_st_8 = models.FloatField(db_column='VP_ST_8', blank=True, null=True)  # Field name made lowercase.
    vp_st_9 = models.FloatField(db_column='VP_ST_9', blank=True, null=True)  # Field name made lowercase.
    vp_st_10 = models.FloatField(db_column='VP_ST_10', blank=True, null=True)  # Field name made lowercase.
    vp_st_11 = models.FloatField(db_column='VP_ST_11', blank=True, null=True)  # Field name made lowercase.
    vp_st_12 = models.FloatField(db_column='VP_ST_12', blank=True, null=True)  # Field name made lowercase.
    v_co2_1 = models.FloatField(db_column='V_CO2_1', blank=True, null=True)  # Field name made lowercase.
    v_co2_2 = models.FloatField(db_column='V_CO2_2', blank=True, null=True)  # Field name made lowercase.
    v_co2_3 = models.FloatField(db_column='V_CO2_3', blank=True, null=True)  # Field name made lowercase.
    v_co2_4 = models.FloatField(db_column='V_CO2_4', blank=True, null=True)  # Field name made lowercase.
    v_co2_5 = models.FloatField(db_column='V_CO2_5', blank=True, null=True)  # Field name made lowercase.
    v_co2_6 = models.FloatField(db_column='V_CO2_6', blank=True, null=True)  # Field name made lowercase.
    v_co2_7 = models.FloatField(db_column='V_CO2_7', blank=True, null=True)  # Field name made lowercase.
    v_co2_8 = models.FloatField(db_column='V_CO2_8', blank=True, null=True)  # Field name made lowercase.
    v_co2_9 = models.FloatField(db_column='V_CO2_9', blank=True, null=True)  # Field name made lowercase.
    v_co2_10 = models.FloatField(db_column='V_CO2_10', blank=True, null=True)  # Field name made lowercase.
    v_co2_11 = models.FloatField(db_column='V_CO2_11', blank=True, null=True)  # Field name made lowercase.
    v_co2_12 = models.FloatField(db_column='V_CO2_12', blank=True, null=True)  # Field name made lowercase.
    v_co1_1 = models.FloatField(db_column='V_CO1_1', blank=True, null=True)  # Field name made lowercase.
    v_co1_2 = models.FloatField(db_column='V_CO1_2', blank=True, null=True)  # Field name made lowercase.
    v_co1_3 = models.FloatField(db_column='V_CO1_3', blank=True, null=True)  # Field name made lowercase.
    v_co1_4 = models.FloatField(db_column='V_CO1_4', blank=True, null=True)  # Field name made lowercase.
    v_co1_5 = models.FloatField(db_column='V_CO1_5', blank=True, null=True)  # Field name made lowercase.
    v_co1_6 = models.FloatField(db_column='V_CO1_6', blank=True, null=True)  # Field name made lowercase.
    v_co1_7 = models.FloatField(db_column='V_CO1_7', blank=True, null=True)  # Field name made lowercase.
    v_co1_8 = models.FloatField(db_column='V_CO1_8', blank=True, null=True)  # Field name made lowercase.
    v_co1_9 = models.FloatField(db_column='V_CO1_9', blank=True, null=True)  # Field name made lowercase.
    v_co1_10 = models.FloatField(db_column='V_CO1_10', blank=True, null=True)  # Field name made lowercase.
    v_co1_11 = models.FloatField(db_column='V_CO1_11', blank=True, null=True)  # Field name made lowercase.
    v_co1_12 = models.FloatField(db_column='V_CO1_12', blank=True, null=True)  # Field name made lowercase.
    q_co2_1 = models.FloatField(db_column='Q_CO2_1', blank=True, null=True)  # Field name made lowercase.
    q_co2_2 = models.FloatField(db_column='Q_CO2_2', blank=True, null=True)  # Field name made lowercase.
    q_co2_3 = models.FloatField(db_column='Q_CO2_3', blank=True, null=True)  # Field name made lowercase.
    q_co2_4 = models.FloatField(db_column='Q_CO2_4', blank=True, null=True)  # Field name made lowercase.
    q_co2_5 = models.FloatField(db_column='Q_CO2_5', blank=True, null=True)  # Field name made lowercase.
    q_co2_6 = models.FloatField(db_column='Q_CO2_6', blank=True, null=True)  # Field name made lowercase.
    q_co2_7 = models.FloatField(db_column='Q_CO2_7', blank=True, null=True)  # Field name made lowercase.
    q_co2_8 = models.FloatField(db_column='Q_CO2_8', blank=True, null=True)  # Field name made lowercase.
    q_co2_9 = models.FloatField(db_column='Q_CO2_9', blank=True, null=True)  # Field name made lowercase.
    q_co2_10 = models.FloatField(db_column='Q_CO2_10', blank=True, null=True)  # Field name made lowercase.
    q_co2_11 = models.FloatField(db_column='Q_CO2_11', blank=True, null=True)  # Field name made lowercase.
    q_co2_12 = models.FloatField(db_column='Q_CO2_12', blank=True, null=True)  # Field name made lowercase.
    q_co1_1 = models.FloatField(db_column='Q_CO1_1', blank=True, null=True)  # Field name made lowercase.
    q_co1_2 = models.FloatField(db_column='Q_CO1_2', blank=True, null=True)  # Field name made lowercase.
    q_co1_3 = models.FloatField(db_column='Q_CO1_3', blank=True, null=True)  # Field name made lowercase.
    q_co1_4 = models.FloatField(db_column='Q_CO1_4', blank=True, null=True)  # Field name made lowercase.
    q_co1_5 = models.FloatField(db_column='Q_CO1_5', blank=True, null=True)  # Field name made lowercase.
    q_co1_6 = models.FloatField(db_column='Q_CO1_6', blank=True, null=True)  # Field name made lowercase.
    q_co1_7 = models.FloatField(db_column='Q_CO1_7', blank=True, null=True)  # Field name made lowercase.
    q_co1_8 = models.FloatField(db_column='Q_CO1_8', blank=True, null=True)  # Field name made lowercase.
    q_co1_9 = models.FloatField(db_column='Q_CO1_9', blank=True, null=True)  # Field name made lowercase.
    q_co1_10 = models.FloatField(db_column='Q_CO1_10', blank=True, null=True)  # Field name made lowercase.
    q_co1_11 = models.FloatField(db_column='Q_CO1_11', blank=True, null=True)  # Field name made lowercase.
    q_co1_12 = models.FloatField(db_column='Q_CO1_12', blank=True, null=True)  # Field name made lowercase.
    ve_fr_1 = models.FloatField(db_column='VE_FR_1', blank=True, null=True)  # Field name made lowercase.
    ve_fr_2 = models.FloatField(db_column='VE_FR_2', blank=True, null=True)  # Field name made lowercase.
    ve_fr_3 = models.FloatField(db_column='VE_FR_3', blank=True, null=True)  # Field name made lowercase.
    ve_fr_4 = models.FloatField(db_column='VE_FR_4', blank=True, null=True)  # Field name made lowercase.
    ve_fr_5 = models.FloatField(db_column='VE_FR_5', blank=True, null=True)  # Field name made lowercase.
    ve_fr_6 = models.FloatField(db_column='VE_FR_6', blank=True, null=True)  # Field name made lowercase.
    ve_fr_7 = models.FloatField(db_column='VE_FR_7', blank=True, null=True)  # Field name made lowercase.
    ve_fr_8 = models.FloatField(db_column='VE_FR_8', blank=True, null=True)  # Field name made lowercase.
    ve_fr_9 = models.FloatField(db_column='VE_FR_9', blank=True, null=True)  # Field name made lowercase.
    ve_fr_10 = models.FloatField(db_column='VE_FR_10', blank=True, null=True)  # Field name made lowercase.
    ve_fr_11 = models.FloatField(db_column='VE_FR_11', blank=True, null=True)  # Field name made lowercase.
    ve_fr_12 = models.FloatField(db_column='VE_FR_12', blank=True, null=True)  # Field name made lowercase.
    qe_fr_1 = models.FloatField(db_column='QE_FR_1', blank=True, null=True)  # Field name made lowercase.
    qe_fr_2 = models.FloatField(db_column='QE_FR_2', blank=True, null=True)  # Field name made lowercase.
    qe_fr_3 = models.FloatField(db_column='QE_FR_3', blank=True, null=True)  # Field name made lowercase.
    qe_fr_4 = models.FloatField(db_column='QE_FR_4', blank=True, null=True)  # Field name made lowercase.
    qe_fr_5 = models.FloatField(db_column='QE_FR_5', blank=True, null=True)  # Field name made lowercase.
    qe_fr_6 = models.FloatField(db_column='QE_FR_6', blank=True, null=True)  # Field name made lowercase.
    qe_fr_7 = models.FloatField(db_column='QE_FR_7', blank=True, null=True)  # Field name made lowercase.
    qe_fr_8 = models.FloatField(db_column='QE_FR_8', blank=True, null=True)  # Field name made lowercase.
    qe_fr_9 = models.FloatField(db_column='QE_FR_9', blank=True, null=True)  # Field name made lowercase.
    qe_fr_10 = models.FloatField(db_column='QE_FR_10', blank=True, null=True)  # Field name made lowercase.
    qe_fr_11 = models.FloatField(db_column='QE_FR_11', blank=True, null=True)  # Field name made lowercase.
    qe_fr_12 = models.FloatField(db_column='QE_FR_12', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FLASHP'


class Flashr(models.Model):
    code_po = models.CharField(db_column='CODE_PO', max_length=4, blank=True, null=True)  # Field name made lowercase.
    code_nt = models.CharField(db_column='CODE_NT', max_length=4, blank=True, null=True)  # Field name made lowercase.
    code_ac = models.CharField(db_column='CODE_AC', max_length=4, blank=True, null=True)  # Field name made lowercase.
    annee = models.CharField(db_column='ANNEE', max_length=4, blank=True, null=True)  # Field name made lowercase.
    vr_st_1 = models.FloatField(db_column='VR_ST_1', blank=True, null=True)  # Field name made lowercase.
    vr_st_2 = models.FloatField(db_column='VR_ST_2', blank=True, null=True)  # Field name made lowercase.
    vr_st_3 = models.FloatField(db_column='VR_ST_3', blank=True, null=True)  # Field name made lowercase.
    vr_st_4 = models.FloatField(db_column='VR_ST_4', blank=True, null=True)  # Field name made lowercase.
    vr_st_5 = models.FloatField(db_column='VR_ST_5', blank=True, null=True)  # Field name made lowercase.
    vr_st_6 = models.FloatField(db_column='VR_ST_6', blank=True, null=True)  # Field name made lowercase.
    vr_st_7 = models.FloatField(db_column='VR_ST_7', blank=True, null=True)  # Field name made lowercase.
    vr_st_8 = models.FloatField(db_column='VR_ST_8', blank=True, null=True)  # Field name made lowercase.
    vr_st_9 = models.FloatField(db_column='VR_ST_9', blank=True, null=True)  # Field name made lowercase.
    vr_st_10 = models.FloatField(db_column='VR_ST_10', blank=True, null=True)  # Field name made lowercase.
    vr_st_11 = models.FloatField(db_column='VR_ST_11', blank=True, null=True)  # Field name made lowercase.
    vr_st_12 = models.FloatField(db_column='VR_ST_12', blank=True, null=True)  # Field name made lowercase.
    vr_su_1 = models.FloatField(db_column='VR_SU_1', blank=True, null=True)  # Field name made lowercase.
    vr_su_2 = models.FloatField(db_column='VR_SU_2', blank=True, null=True)  # Field name made lowercase.
    vr_su_3 = models.FloatField(db_column='VR_SU_3', blank=True, null=True)  # Field name made lowercase.
    vr_su_4 = models.FloatField(db_column='VR_SU_4', blank=True, null=True)  # Field name made lowercase.
    vr_su_5 = models.FloatField(db_column='VR_SU_5', blank=True, null=True)  # Field name made lowercase.
    vr_su_6 = models.FloatField(db_column='VR_SU_6', blank=True, null=True)  # Field name made lowercase.
    vr_su_7 = models.FloatField(db_column='VR_SU_7', blank=True, null=True)  # Field name made lowercase.
    vr_su_8 = models.FloatField(db_column='VR_SU_8', blank=True, null=True)  # Field name made lowercase.
    vr_su_9 = models.FloatField(db_column='VR_SU_9', blank=True, null=True)  # Field name made lowercase.
    vr_su_10 = models.FloatField(db_column='VR_SU_10', blank=True, null=True)  # Field name made lowercase.
    vr_su_11 = models.FloatField(db_column='VR_SU_11', blank=True, null=True)  # Field name made lowercase.
    vr_su_12 = models.FloatField(db_column='VR_SU_12', blank=True, null=True)  # Field name made lowercase.
    vr_co_1 = models.FloatField(db_column='VR_CO_1', blank=True, null=True)  # Field name made lowercase.
    vr_co_2 = models.FloatField(db_column='VR_CO_2', blank=True, null=True)  # Field name made lowercase.
    vr_co_3 = models.FloatField(db_column='VR_CO_3', blank=True, null=True)  # Field name made lowercase.
    vr_co_4 = models.FloatField(db_column='VR_CO_4', blank=True, null=True)  # Field name made lowercase.
    vr_co_5 = models.FloatField(db_column='VR_CO_5', blank=True, null=True)  # Field name made lowercase.
    vr_co_6 = models.FloatField(db_column='VR_CO_6', blank=True, null=True)  # Field name made lowercase.
    vr_co_7 = models.FloatField(db_column='VR_CO_7', blank=True, null=True)  # Field name made lowercase.
    vr_co_8 = models.FloatField(db_column='VR_CO_8', blank=True, null=True)  # Field name made lowercase.
    vr_co_9 = models.FloatField(db_column='VR_CO_9', blank=True, null=True)  # Field name made lowercase.
    vr_co_10 = models.FloatField(db_column='VR_CO_10', blank=True, null=True)  # Field name made lowercase.
    vr_co_11 = models.FloatField(db_column='VR_CO_11', blank=True, null=True)  # Field name made lowercase.
    vr_co_12 = models.FloatField(db_column='VR_CO_12', blank=True, null=True)  # Field name made lowercase.
    qr_su_1 = models.FloatField(db_column='QR_SU_1', blank=True, null=True)  # Field name made lowercase.
    qr_su_2 = models.FloatField(db_column='QR_SU_2', blank=True, null=True)  # Field name made lowercase.
    qr_su_3 = models.FloatField(db_column='QR_SU_3', blank=True, null=True)  # Field name made lowercase.
    qr_su_4 = models.FloatField(db_column='QR_SU_4', blank=True, null=True)  # Field name made lowercase.
    qr_su_5 = models.FloatField(db_column='QR_SU_5', blank=True, null=True)  # Field name made lowercase.
    qr_su_6 = models.FloatField(db_column='QR_SU_6', blank=True, null=True)  # Field name made lowercase.
    qr_su_7 = models.FloatField(db_column='QR_SU_7', blank=True, null=True)  # Field name made lowercase.
    qr_su_8 = models.FloatField(db_column='QR_SU_8', blank=True, null=True)  # Field name made lowercase.
    qr_su_9 = models.FloatField(db_column='QR_SU_9', blank=True, null=True)  # Field name made lowercase.
    qr_su_10 = models.FloatField(db_column='QR_SU_10', blank=True, null=True)  # Field name made lowercase.
    qr_su_11 = models.FloatField(db_column='QR_SU_11', blank=True, null=True)  # Field name made lowercase.
    qr_su_12 = models.FloatField(db_column='QR_SU_12', blank=True, null=True)  # Field name made lowercase.
    qr_co_1 = models.FloatField(db_column='QR_CO_1', blank=True, null=True)  # Field name made lowercase.
    qr_co_2 = models.FloatField(db_column='QR_CO_2', blank=True, null=True)  # Field name made lowercase.
    qr_co_3 = models.FloatField(db_column='QR_CO_3', blank=True, null=True)  # Field name made lowercase.
    qr_co_4 = models.FloatField(db_column='QR_CO_4', blank=True, null=True)  # Field name made lowercase.
    qr_co_5 = models.FloatField(db_column='QR_CO_5', blank=True, null=True)  # Field name made lowercase.
    qr_co_6 = models.FloatField(db_column='QR_CO_6', blank=True, null=True)  # Field name made lowercase.
    qr_co_7 = models.FloatField(db_column='QR_CO_7', blank=True, null=True)  # Field name made lowercase.
    qr_co_8 = models.FloatField(db_column='QR_CO_8', blank=True, null=True)  # Field name made lowercase.
    qr_co_9 = models.FloatField(db_column='QR_CO_9', blank=True, null=True)  # Field name made lowercase.
    qr_co_10 = models.FloatField(db_column='QR_CO_10', blank=True, null=True)  # Field name made lowercase.
    qr_co_11 = models.FloatField(db_column='QR_CO_11', blank=True, null=True)  # Field name made lowercase.
    qr_co_12 = models.FloatField(db_column='QR_CO_12', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FLASHR'


class Factures(models.Model):
    num_facture = models.CharField(db_column='Num_Facture', primary_key=True, max_length=800)  # Field name made lowercase.
    num_situation = models.IntegerField(db_column='Num_Situation')  # Field name made lowercase.
    date_debut = models.DateField(db_column='Date_Debut')  # Field name made lowercase.
    date_fin = models.DateField(db_column='Date_Fin')  # Field name made lowercase.
    date_facture = models.DateField(db_column='Date_Facture')  # Field name made lowercase.
    montant_mois = models.FloatField(db_column='Montant_Mois', blank=True, null=True)  # Field name made lowercase.
    montant_rb = models.FloatField(db_column='Montant_RB', blank=True, null=True)  # Field name made lowercase.
    montant_rg = models.FloatField(db_column='Montant_RG', blank=True, null=True)  # Field name made lowercase.
    paye = models.BooleanField(db_column='Paye', blank=True, null=True)  # Field name made lowercase.
    num_marche = models.ForeignKey('Marche', models.DO_NOTHING, db_column='Num_Marche')  # Field name made lowercase.
    est_bloquer = models.BooleanField(db_column='Est_Bloquer')  # Field name made lowercase.
    user_id = models.CharField(db_column='User_ID', max_length=15)  # Field name made lowercase.
    date_modification = models.DateTimeField(db_column='Date_Modification', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Factures'


class Groups(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'Groups'


class GroupsPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(Groups, models.DO_NOTHING)
    permission = models.ForeignKey('Permission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'Groups_permissions'
        unique_together = (('group', 'permission'),)


class Marche(models.Model):
    num_contrat = models.CharField(db_column='Num_Contrat', primary_key=True, max_length=500)  # Field name made lowercase.
    num_avenant = models.IntegerField(db_column='Num_Avenant')  # Field name made lowercase.
    code_site = models.ForeignKey('TabNt', models.DO_NOTHING, db_column='Code_Site', to_field='NT')  # Field name made lowercase.
    nt = models.ForeignKey('TabNt', models.DO_NOTHING, db_column='NT', to_field='NT', related_name='marche_nt_set')  # Field name made lowercase.
    libelle = models.TextField(db_column='Libelle')  # Field name made lowercase.
    ods_depart = models.DateField(db_column='Ods_Depart')  # Field name made lowercase.
    delais = models.IntegerField(db_column='Delais', blank=True, null=True)  # Field name made lowercase.
    revisable = models.BooleanField(db_column='Revisable', blank=True, null=True)  # Field name made lowercase.
    actualisable = models.BooleanField(db_column='Actualisable', blank=True, null=True)  # Field name made lowercase.
    delai_paiement_f = models.IntegerField(db_column='Delai_Paiement_F', blank=True, null=True)  # Field name made lowercase.
    rabais = models.FloatField(db_column='Rabais', blank=True, null=True)  # Field name made lowercase.
    tva = models.FloatField(db_column='Tva', blank=True, null=True)  # Field name made lowercase.
    rg = models.FloatField(db_column='Rg', blank=True, null=True)  # Field name made lowercase.
    date_signature = models.DateField(db_column='Date_Signature')  # Field name made lowercase.
    est_bloquer = models.BooleanField(db_column='Est_Bloquer')  # Field name made lowercase.
    user_id = models.CharField(db_column='User_ID', max_length=15, blank=True, null=True)  # Field name made lowercase.
    date_modification = models.DateTimeField(db_column='Date_Modification', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Marche'


class MarcheAvenant(models.Model):
    num_contrat = models.CharField(db_column='Num_Contrat', primary_key=True, max_length=500)  # Field name made lowercase. The composite primary key (Num_Contrat, Num_Avenant) found, that is not supported. The first column is selected.
    num_avenant = models.IntegerField(db_column='Num_Avenant')  # Field name made lowercase.
    code_site = models.ForeignKey('TabNt', models.DO_NOTHING, db_column='Code_Site', to_field='NT')  # Field name made lowercase.
    nt = models.ForeignKey('TabNt', models.DO_NOTHING, db_column='NT', to_field='NT', related_name='marcheavenant_nt_set')  # Field name made lowercase.
    libelle = models.TextField(db_column='Libelle')  # Field name made lowercase.
    ods_depart = models.DateField(db_column='Ods_Depart')  # Field name made lowercase.
    delais = models.IntegerField(db_column='Delais', blank=True, null=True)  # Field name made lowercase.
    revisable = models.BooleanField(db_column='Revisable', blank=True, null=True)  # Field name made lowercase.
    actualisable = models.BooleanField(db_column='Actualisable', blank=True, null=True)  # Field name made lowercase.
    delai_paiement_f = models.IntegerField(db_column='Delai_Paiement_F', blank=True, null=True)  # Field name made lowercase.
    rabais = models.FloatField(db_column='Rabais', blank=True, null=True)  # Field name made lowercase.
    tva = models.FloatField(db_column='Tva', blank=True, null=True)  # Field name made lowercase.
    rg = models.FloatField(db_column='Rg', blank=True, null=True)  # Field name made lowercase.
    date_signature = models.DateField(db_column='Date_Signature')  # Field name made lowercase.
    est_bloquer = models.BooleanField(db_column='Est_Bloquer')  # Field name made lowercase.
    user_id = models.CharField(db_column='User_ID', max_length=15, blank=True, null=True)  # Field name made lowercase.
    date_modification = models.DateTimeField(db_column='Date_Modification', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Marche_Avenant'
        unique_together = (('num_contrat', 'num_avenant'),)


class ModePaiement(models.Model):
    id_mode = models.AutoField(db_column='Id_Mode', primary_key=True)  # Field name made lowercase.
    libelle = models.CharField(max_length=500)
    est_bloquer = models.BooleanField(db_column='Est_Bloquer')  # Field name made lowercase.
    user_id = models.CharField(db_column='User_ID', max_length=15)  # Field name made lowercase.
    date_modification = models.DateTimeField(db_column='Date_Modification', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Mode_Paiement'


class Nt(models.Model):
    code_nt = models.CharField(db_column='CODE_NT', max_length=4, blank=True, null=True)  # Field name made lowercase.
    lib_lg_nt = models.CharField(db_column='LIB_LG_NT', max_length=30, blank=True, null=True)  # Field name made lowercase.
    lib_cr_nt = models.CharField(db_column='LIB_CR_NT', max_length=15, blank=True, null=True)  # Field name made lowercase.
    code_an = models.FloatField(db_column='CODE_AN', blank=True, null=True)  # Field name made lowercase.
    dat_ouv_nt = models.CharField(db_column='DAT_OUV_NT', max_length=6, blank=True, null=True)  # Field name made lowercase.
    sit_nt = models.FloatField(db_column='SIT_NT', blank=True, null=True)  # Field name made lowercase.
    dat_fer_nt = models.CharField(db_column='DAT_FER_NT', max_length=6, blank=True, null=True)  # Field name made lowercase.
    code_cl = models.CharField(db_column='CODE_CL', max_length=8, blank=True, null=True)  # Field name made lowercase.
    code_po = models.CharField(db_column='CODE_PO', max_length=4, blank=True, null=True)  # Field name made lowercase.
    intext_nt = models.CharField(db_column='INTEXT_NT', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'NT'


class Planchar(models.Model):
    nat_ch = models.CharField(db_column='NAT_CH', max_length=2, blank=True, null=True)  # Field name made lowercase.
    type_ch = models.CharField(db_column='TYPE_CH', max_length=1, blank=True, null=True)  # Field name made lowercase.
    code_ch = models.CharField(db_column='CODE_CH', max_length=3, blank=True, null=True)  # Field name made lowercase.
    annee = models.CharField(db_column='ANNEE', max_length=4, blank=True, null=True)  # Field name made lowercase.
    code_po = models.CharField(db_column='CODE_PO', max_length=4, blank=True, null=True)  # Field name made lowercase.
    code_nt = models.CharField(db_column='CODE_NT', max_length=4, blank=True, null=True)  # Field name made lowercase.
    val_pc_1 = models.FloatField(db_column='VAL_PC_1', blank=True, null=True)  # Field name made lowercase.
    val_pc_2 = models.FloatField(db_column='VAL_PC_2', blank=True, null=True)  # Field name made lowercase.
    val_pc_3 = models.FloatField(db_column='VAL_PC_3', blank=True, null=True)  # Field name made lowercase.
    val_pc_4 = models.FloatField(db_column='VAL_PC_4', blank=True, null=True)  # Field name made lowercase.
    val_pc_5 = models.FloatField(db_column='VAL_PC_5', blank=True, null=True)  # Field name made lowercase.
    val_pc_6 = models.FloatField(db_column='VAL_PC_6', blank=True, null=True)  # Field name made lowercase.
    val_pc_7 = models.FloatField(db_column='VAL_PC_7', blank=True, null=True)  # Field name made lowercase.
    val_pc_8 = models.FloatField(db_column='VAL_PC_8', blank=True, null=True)  # Field name made lowercase.
    val_pc_9 = models.FloatField(db_column='VAL_PC_9', blank=True, null=True)  # Field name made lowercase.
    val_pc_10 = models.FloatField(db_column='VAL_PC_10', blank=True, null=True)  # Field name made lowercase.
    val_pc_11 = models.FloatField(db_column='VAL_PC_11', blank=True, null=True)  # Field name made lowercase.
    val_pc_12 = models.FloatField(db_column='VAL_PC_12', blank=True, null=True)  # Field name made lowercase.
    classification_charge = models.CharField(db_column='Classification_Charge', max_length=5, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PLANCHAR'


class Pole(models.Model):
    code_po = models.CharField(db_column='CODE_PO', max_length=4, blank=True, null=True)  # Field name made lowercase.
    lib_lg_po = models.CharField(db_column='LIB_LG_PO', max_length=30, blank=True, null=True)  # Field name made lowercase.
    lib_cr_po = models.CharField(db_column='LIB_CR_PO', max_length=15, blank=True, null=True)  # Field name made lowercase.
    nom_res_po = models.CharField(db_column='NOM_RES_PO', max_length=20, blank=True, null=True)  # Field name made lowercase.
    wilaya_po = models.CharField(db_column='WILAYA_PO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    dat_ouv_po = models.CharField(db_column='DAT_OUV_PO', max_length=6, blank=True, null=True)  # Field name made lowercase.
    sit_po = models.FloatField(db_column='SIT_PO', blank=True, null=True)  # Field name made lowercase.
    dat_fer_po = models.CharField(db_column='DAT_FER_PO', max_length=6, blank=True, null=True)  # Field name made lowercase.
    code_di = models.CharField(db_column='CODE_DI', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'POLE'


class Prestat(models.Model):
    nat_ch = models.CharField(db_column='NAT_CH', max_length=2, blank=True, null=True)  # Field name made lowercase.
    type_ch = models.CharField(db_column='TYPE_CH', max_length=1, blank=True, null=True)  # Field name made lowercase.
    code_ch = models.CharField(db_column='CODE_CH', max_length=3, blank=True, null=True)  # Field name made lowercase.
    cdvent_pr = models.CharField(db_column='CDVENT_PR', max_length=1, blank=True, null=True)  # Field name made lowercase.
    qte_pr_1 = models.FloatField(db_column='QTE_PR_1', blank=True, null=True)  # Field name made lowercase.
    qte_pr_2 = models.FloatField(db_column='QTE_PR_2', blank=True, null=True)  # Field name made lowercase.
    qte_pr_3 = models.FloatField(db_column='QTE_PR_3', blank=True, null=True)  # Field name made lowercase.
    qte_pr_4 = models.FloatField(db_column='QTE_PR_4', blank=True, null=True)  # Field name made lowercase.
    qte_pr_5 = models.FloatField(db_column='QTE_PR_5', blank=True, null=True)  # Field name made lowercase.
    qte_pr_6 = models.FloatField(db_column='QTE_PR_6', blank=True, null=True)  # Field name made lowercase.
    qte_pr_7 = models.FloatField(db_column='QTE_PR_7', blank=True, null=True)  # Field name made lowercase.
    qte_pr_8 = models.FloatField(db_column='QTE_PR_8', blank=True, null=True)  # Field name made lowercase.
    qte_pr_9 = models.FloatField(db_column='QTE_PR_9', blank=True, null=True)  # Field name made lowercase.
    qte_pr_10 = models.FloatField(db_column='QTE_PR_10', blank=True, null=True)  # Field name made lowercase.
    qte_pr_11 = models.FloatField(db_column='QTE_PR_11', blank=True, null=True)  # Field name made lowercase.
    qte_pr_12 = models.FloatField(db_column='QTE_PR_12', blank=True, null=True)  # Field name made lowercase.
    val_pr_1 = models.FloatField(db_column='VAL_PR_1', blank=True, null=True)  # Field name made lowercase.
    val_pr_2 = models.FloatField(db_column='VAL_PR_2', blank=True, null=True)  # Field name made lowercase.
    val_pr_3 = models.FloatField(db_column='VAL_PR_3', blank=True, null=True)  # Field name made lowercase.
    val_pr_4 = models.FloatField(db_column='VAL_PR_4', blank=True, null=True)  # Field name made lowercase.
    val_pr_5 = models.FloatField(db_column='VAL_PR_5', blank=True, null=True)  # Field name made lowercase.
    val_pr_6 = models.FloatField(db_column='VAL_PR_6', blank=True, null=True)  # Field name made lowercase.
    val_pr_7 = models.FloatField(db_column='VAL_PR_7', blank=True, null=True)  # Field name made lowercase.
    val_pr_8 = models.FloatField(db_column='VAL_PR_8', blank=True, null=True)  # Field name made lowercase.
    val_pr_9 = models.FloatField(db_column='VAL_PR_9', blank=True, null=True)  # Field name made lowercase.
    val_pr_10 = models.FloatField(db_column='VAL_PR_10', blank=True, null=True)  # Field name made lowercase.
    val_pr_11 = models.FloatField(db_column='VAL_PR_11', blank=True, null=True)  # Field name made lowercase.
    val_pr_12 = models.FloatField(db_column='VAL_PR_12', blank=True, null=True)  # Field name made lowercase.
    annee = models.CharField(db_column='ANNEE', max_length=4, blank=True, null=True)  # Field name made lowercase.
    code_po = models.CharField(db_column='CODE_PO', max_length=4, blank=True, null=True)  # Field name made lowercase.
    cle_pr = models.CharField(db_column='CLE_PR', max_length=12, blank=True, null=True)  # Field name made lowercase.
    cle_prod = models.CharField(db_column='CLE_PROD', max_length=14, blank=True, null=True)  # Field name made lowercase.
    recepteur = models.CharField(db_column='Recepteur', max_length=15, blank=True, null=True)  # Field name made lowercase.
    nt = models.CharField(db_column='NT', max_length=15, blank=True, null=True)  # Field name made lowercase.
    classification_charge = models.CharField(db_column='Classification_Charge', max_length=5, blank=True, null=True)  # Field name made lowercase.
    code_activite = models.CharField(db_column='Code_Activite', max_length=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PRESTAT'


class Prestat2017(models.Model):
    nat_ch = models.CharField(db_column='NAT_CH', max_length=2, blank=True, null=True)  # Field name made lowercase.
    type_ch = models.CharField(db_column='TYPE_CH', max_length=1, blank=True, null=True)  # Field name made lowercase.
    code_ch = models.CharField(db_column='CODE_CH', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cdvent_pr = models.CharField(db_column='CDVENT_PR', max_length=1, blank=True, null=True)  # Field name made lowercase.
    qte_pr_1 = models.FloatField(db_column='QTE_PR_1', blank=True, null=True)  # Field name made lowercase.
    qte_pr_2 = models.FloatField(db_column='QTE_PR_2', blank=True, null=True)  # Field name made lowercase.
    qte_pr_3 = models.FloatField(db_column='QTE_PR_3', blank=True, null=True)  # Field name made lowercase.
    qte_pr_4 = models.FloatField(db_column='QTE_PR_4', blank=True, null=True)  # Field name made lowercase.
    qte_pr_5 = models.FloatField(db_column='QTE_PR_5', blank=True, null=True)  # Field name made lowercase.
    qte_pr_6 = models.FloatField(db_column='QTE_PR_6', blank=True, null=True)  # Field name made lowercase.
    qte_pr_7 = models.FloatField(db_column='QTE_PR_7', blank=True, null=True)  # Field name made lowercase.
    qte_pr_8 = models.FloatField(db_column='QTE_PR_8', blank=True, null=True)  # Field name made lowercase.
    qte_pr_9 = models.FloatField(db_column='QTE_PR_9', blank=True, null=True)  # Field name made lowercase.
    qte_pr_10 = models.FloatField(db_column='QTE_PR_10', blank=True, null=True)  # Field name made lowercase.
    qte_pr_11 = models.FloatField(db_column='QTE_PR_11', blank=True, null=True)  # Field name made lowercase.
    qte_pr_12 = models.FloatField(db_column='QTE_PR_12', blank=True, null=True)  # Field name made lowercase.
    val_pr_1 = models.FloatField(db_column='VAL_PR_1', blank=True, null=True)  # Field name made lowercase.
    val_pr_2 = models.FloatField(db_column='VAL_PR_2', blank=True, null=True)  # Field name made lowercase.
    val_pr_3 = models.FloatField(db_column='VAL_PR_3', blank=True, null=True)  # Field name made lowercase.
    val_pr_4 = models.FloatField(db_column='VAL_PR_4', blank=True, null=True)  # Field name made lowercase.
    val_pr_5 = models.FloatField(db_column='VAL_PR_5', blank=True, null=True)  # Field name made lowercase.
    val_pr_6 = models.FloatField(db_column='VAL_PR_6', blank=True, null=True)  # Field name made lowercase.
    val_pr_7 = models.FloatField(db_column='VAL_PR_7', blank=True, null=True)  # Field name made lowercase.
    val_pr_8 = models.FloatField(db_column='VAL_PR_8', blank=True, null=True)  # Field name made lowercase.
    val_pr_9 = models.FloatField(db_column='VAL_PR_9', blank=True, null=True)  # Field name made lowercase.
    val_pr_10 = models.FloatField(db_column='VAL_PR_10', blank=True, null=True)  # Field name made lowercase.
    val_pr_11 = models.FloatField(db_column='VAL_PR_11', blank=True, null=True)  # Field name made lowercase.
    val_pr_12 = models.FloatField(db_column='VAL_PR_12', blank=True, null=True)  # Field name made lowercase.
    annee = models.CharField(db_column='ANNEE', max_length=4, blank=True, null=True)  # Field name made lowercase.
    code_po = models.CharField(db_column='CODE_PO', max_length=4, blank=True, null=True)  # Field name made lowercase.
    cle_pr = models.CharField(db_column='CLE_PR', max_length=12, blank=True, null=True)  # Field name made lowercase.
    cle_prod = models.CharField(db_column='CLE_PROD', max_length=14, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PRESTAT2017'


class Prestat2018(models.Model):
    nat_ch = models.CharField(db_column='NAT_CH', max_length=2, blank=True, null=True)  # Field name made lowercase.
    type_ch = models.CharField(db_column='TYPE_CH', max_length=1, blank=True, null=True)  # Field name made lowercase.
    code_ch = models.CharField(db_column='CODE_CH', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cdvent_pr = models.CharField(db_column='CDVENT_PR', max_length=1, blank=True, null=True)  # Field name made lowercase.
    qte_pr_1 = models.FloatField(db_column='QTE_PR_1', blank=True, null=True)  # Field name made lowercase.
    qte_pr_2 = models.FloatField(db_column='QTE_PR_2', blank=True, null=True)  # Field name made lowercase.
    qte_pr_3 = models.FloatField(db_column='QTE_PR_3', blank=True, null=True)  # Field name made lowercase.
    qte_pr_4 = models.FloatField(db_column='QTE_PR_4', blank=True, null=True)  # Field name made lowercase.
    qte_pr_5 = models.FloatField(db_column='QTE_PR_5', blank=True, null=True)  # Field name made lowercase.
    qte_pr_6 = models.FloatField(db_column='QTE_PR_6', blank=True, null=True)  # Field name made lowercase.
    qte_pr_7 = models.FloatField(db_column='QTE_PR_7', blank=True, null=True)  # Field name made lowercase.
    qte_pr_8 = models.FloatField(db_column='QTE_PR_8', blank=True, null=True)  # Field name made lowercase.
    qte_pr_9 = models.FloatField(db_column='QTE_PR_9', blank=True, null=True)  # Field name made lowercase.
    qte_pr_10 = models.FloatField(db_column='QTE_PR_10', blank=True, null=True)  # Field name made lowercase.
    qte_pr_11 = models.FloatField(db_column='QTE_PR_11', blank=True, null=True)  # Field name made lowercase.
    qte_pr_12 = models.FloatField(db_column='QTE_PR_12', blank=True, null=True)  # Field name made lowercase.
    val_pr_1 = models.FloatField(db_column='VAL_PR_1', blank=True, null=True)  # Field name made lowercase.
    val_pr_2 = models.FloatField(db_column='VAL_PR_2', blank=True, null=True)  # Field name made lowercase.
    val_pr_3 = models.FloatField(db_column='VAL_PR_3', blank=True, null=True)  # Field name made lowercase.
    val_pr_4 = models.FloatField(db_column='VAL_PR_4', blank=True, null=True)  # Field name made lowercase.
    val_pr_5 = models.FloatField(db_column='VAL_PR_5', blank=True, null=True)  # Field name made lowercase.
    val_pr_6 = models.FloatField(db_column='VAL_PR_6', blank=True, null=True)  # Field name made lowercase.
    val_pr_7 = models.FloatField(db_column='VAL_PR_7', blank=True, null=True)  # Field name made lowercase.
    val_pr_8 = models.FloatField(db_column='VAL_PR_8', blank=True, null=True)  # Field name made lowercase.
    val_pr_9 = models.FloatField(db_column='VAL_PR_9', blank=True, null=True)  # Field name made lowercase.
    val_pr_10 = models.FloatField(db_column='VAL_PR_10', blank=True, null=True)  # Field name made lowercase.
    val_pr_11 = models.FloatField(db_column='VAL_PR_11', blank=True, null=True)  # Field name made lowercase.
    val_pr_12 = models.FloatField(db_column='VAL_PR_12', blank=True, null=True)  # Field name made lowercase.
    annee = models.CharField(db_column='ANNEE', max_length=4, blank=True, null=True)  # Field name made lowercase.
    code_po = models.CharField(db_column='CODE_PO', max_length=4, blank=True, null=True)  # Field name made lowercase.
    cle_pr = models.CharField(db_column='CLE_PR', max_length=12, blank=True, null=True)  # Field name made lowercase.
    cle_prod = models.CharField(db_column='CLE_PROD', max_length=14, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PRESTAT2018'


class Prestat2019(models.Model):
    nat_ch = models.CharField(db_column='NAT_CH', max_length=2, blank=True, null=True)  # Field name made lowercase.
    type_ch = models.CharField(db_column='TYPE_CH', max_length=1, blank=True, null=True)  # Field name made lowercase.
    code_ch = models.CharField(db_column='CODE_CH', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cdvent_pr = models.CharField(db_column='CDVENT_PR', max_length=1, blank=True, null=True)  # Field name made lowercase.
    qte_pr_1 = models.FloatField(db_column='QTE_PR_1', blank=True, null=True)  # Field name made lowercase.
    qte_pr_2 = models.FloatField(db_column='QTE_PR_2', blank=True, null=True)  # Field name made lowercase.
    qte_pr_3 = models.FloatField(db_column='QTE_PR_3', blank=True, null=True)  # Field name made lowercase.
    qte_pr_4 = models.FloatField(db_column='QTE_PR_4', blank=True, null=True)  # Field name made lowercase.
    qte_pr_5 = models.FloatField(db_column='QTE_PR_5', blank=True, null=True)  # Field name made lowercase.
    qte_pr_6 = models.FloatField(db_column='QTE_PR_6', blank=True, null=True)  # Field name made lowercase.
    qte_pr_7 = models.FloatField(db_column='QTE_PR_7', blank=True, null=True)  # Field name made lowercase.
    qte_pr_8 = models.FloatField(db_column='QTE_PR_8', blank=True, null=True)  # Field name made lowercase.
    qte_pr_9 = models.FloatField(db_column='QTE_PR_9', blank=True, null=True)  # Field name made lowercase.
    qte_pr_10 = models.FloatField(db_column='QTE_PR_10', blank=True, null=True)  # Field name made lowercase.
    qte_pr_11 = models.FloatField(db_column='QTE_PR_11', blank=True, null=True)  # Field name made lowercase.
    qte_pr_12 = models.FloatField(db_column='QTE_PR_12', blank=True, null=True)  # Field name made lowercase.
    val_pr_1 = models.FloatField(db_column='VAL_PR_1', blank=True, null=True)  # Field name made lowercase.
    val_pr_2 = models.FloatField(db_column='VAL_PR_2', blank=True, null=True)  # Field name made lowercase.
    val_pr_3 = models.FloatField(db_column='VAL_PR_3', blank=True, null=True)  # Field name made lowercase.
    val_pr_4 = models.FloatField(db_column='VAL_PR_4', blank=True, null=True)  # Field name made lowercase.
    val_pr_5 = models.FloatField(db_column='VAL_PR_5', blank=True, null=True)  # Field name made lowercase.
    val_pr_6 = models.FloatField(db_column='VAL_PR_6', blank=True, null=True)  # Field name made lowercase.
    val_pr_7 = models.FloatField(db_column='VAL_PR_7', blank=True, null=True)  # Field name made lowercase.
    val_pr_8 = models.FloatField(db_column='VAL_PR_8', blank=True, null=True)  # Field name made lowercase.
    val_pr_9 = models.FloatField(db_column='VAL_PR_9', blank=True, null=True)  # Field name made lowercase.
    val_pr_10 = models.FloatField(db_column='VAL_PR_10', blank=True, null=True)  # Field name made lowercase.
    val_pr_11 = models.FloatField(db_column='VAL_PR_11', blank=True, null=True)  # Field name made lowercase.
    val_pr_12 = models.FloatField(db_column='VAL_PR_12', blank=True, null=True)  # Field name made lowercase.
    annee = models.CharField(db_column='ANNEE', max_length=4, blank=True, null=True)  # Field name made lowercase.
    code_po = models.CharField(db_column='CODE_PO', max_length=4, blank=True, null=True)  # Field name made lowercase.
    cle_pr = models.CharField(db_column='CLE_PR', max_length=12, blank=True, null=True)  # Field name made lowercase.
    cle_prod = models.CharField(db_column='CLE_PROD', max_length=14, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PRESTAT2019'


class Prestat2020(models.Model):
    nat_ch = models.CharField(db_column='NAT_CH', max_length=2, blank=True, null=True)  # Field name made lowercase.
    type_ch = models.CharField(db_column='TYPE_CH', max_length=1, blank=True, null=True)  # Field name made lowercase.
    code_ch = models.CharField(db_column='CODE_CH', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cdvent_pr = models.CharField(db_column='CDVENT_PR', max_length=1, blank=True, null=True)  # Field name made lowercase.
    qte_pr_1 = models.FloatField(db_column='QTE_PR_1', blank=True, null=True)  # Field name made lowercase.
    qte_pr_2 = models.FloatField(db_column='QTE_PR_2', blank=True, null=True)  # Field name made lowercase.
    qte_pr_3 = models.FloatField(db_column='QTE_PR_3', blank=True, null=True)  # Field name made lowercase.
    qte_pr_4 = models.FloatField(db_column='QTE_PR_4', blank=True, null=True)  # Field name made lowercase.
    qte_pr_5 = models.FloatField(db_column='QTE_PR_5', blank=True, null=True)  # Field name made lowercase.
    qte_pr_6 = models.FloatField(db_column='QTE_PR_6', blank=True, null=True)  # Field name made lowercase.
    qte_pr_7 = models.FloatField(db_column='QTE_PR_7', blank=True, null=True)  # Field name made lowercase.
    qte_pr_8 = models.FloatField(db_column='QTE_PR_8', blank=True, null=True)  # Field name made lowercase.
    qte_pr_9 = models.FloatField(db_column='QTE_PR_9', blank=True, null=True)  # Field name made lowercase.
    qte_pr_10 = models.FloatField(db_column='QTE_PR_10', blank=True, null=True)  # Field name made lowercase.
    qte_pr_11 = models.FloatField(db_column='QTE_PR_11', blank=True, null=True)  # Field name made lowercase.
    qte_pr_12 = models.FloatField(db_column='QTE_PR_12', blank=True, null=True)  # Field name made lowercase.
    val_pr_1 = models.FloatField(db_column='VAL_PR_1', blank=True, null=True)  # Field name made lowercase.
    val_pr_2 = models.FloatField(db_column='VAL_PR_2', blank=True, null=True)  # Field name made lowercase.
    val_pr_3 = models.FloatField(db_column='VAL_PR_3', blank=True, null=True)  # Field name made lowercase.
    val_pr_4 = models.FloatField(db_column='VAL_PR_4', blank=True, null=True)  # Field name made lowercase.
    val_pr_5 = models.FloatField(db_column='VAL_PR_5', blank=True, null=True)  # Field name made lowercase.
    val_pr_6 = models.FloatField(db_column='VAL_PR_6', blank=True, null=True)  # Field name made lowercase.
    val_pr_7 = models.FloatField(db_column='VAL_PR_7', blank=True, null=True)  # Field name made lowercase.
    val_pr_8 = models.FloatField(db_column='VAL_PR_8', blank=True, null=True)  # Field name made lowercase.
    val_pr_9 = models.FloatField(db_column='VAL_PR_9', blank=True, null=True)  # Field name made lowercase.
    val_pr_10 = models.FloatField(db_column='VAL_PR_10', blank=True, null=True)  # Field name made lowercase.
    val_pr_11 = models.FloatField(db_column='VAL_PR_11', blank=True, null=True)  # Field name made lowercase.
    val_pr_12 = models.FloatField(db_column='VAL_PR_12', blank=True, null=True)  # Field name made lowercase.
    annee = models.CharField(db_column='ANNEE', max_length=4, blank=True, null=True)  # Field name made lowercase.
    code_po = models.CharField(db_column='CODE_PO', max_length=4, blank=True, null=True)  # Field name made lowercase.
    cle_pr = models.CharField(db_column='CLE_PR', max_length=12, blank=True, null=True)  # Field name made lowercase.
    cle_prod = models.CharField(db_column='CLE_PROD', max_length=14, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PRESTAT2020'


class Prestat2021(models.Model):
    nat_ch = models.CharField(db_column='NAT_CH', max_length=2, blank=True, null=True)  # Field name made lowercase.
    type_ch = models.CharField(db_column='TYPE_CH', max_length=1, blank=True, null=True)  # Field name made lowercase.
    code_ch = models.CharField(db_column='CODE_CH', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cdvent_pr = models.CharField(db_column='CDVENT_PR', max_length=1, blank=True, null=True)  # Field name made lowercase.
    qte_pr_1 = models.FloatField(db_column='QTE_PR_1', blank=True, null=True)  # Field name made lowercase.
    qte_pr_2 = models.FloatField(db_column='QTE_PR_2', blank=True, null=True)  # Field name made lowercase.
    qte_pr_3 = models.FloatField(db_column='QTE_PR_3', blank=True, null=True)  # Field name made lowercase.
    qte_pr_4 = models.FloatField(db_column='QTE_PR_4', blank=True, null=True)  # Field name made lowercase.
    qte_pr_5 = models.FloatField(db_column='QTE_PR_5', blank=True, null=True)  # Field name made lowercase.
    qte_pr_6 = models.FloatField(db_column='QTE_PR_6', blank=True, null=True)  # Field name made lowercase.
    qte_pr_7 = models.FloatField(db_column='QTE_PR_7', blank=True, null=True)  # Field name made lowercase.
    qte_pr_8 = models.FloatField(db_column='QTE_PR_8', blank=True, null=True)  # Field name made lowercase.
    qte_pr_9 = models.FloatField(db_column='QTE_PR_9', blank=True, null=True)  # Field name made lowercase.
    qte_pr_10 = models.FloatField(db_column='QTE_PR_10', blank=True, null=True)  # Field name made lowercase.
    qte_pr_11 = models.FloatField(db_column='QTE_PR_11', blank=True, null=True)  # Field name made lowercase.
    qte_pr_12 = models.FloatField(db_column='QTE_PR_12', blank=True, null=True)  # Field name made lowercase.
    val_pr_1 = models.FloatField(db_column='VAL_PR_1', blank=True, null=True)  # Field name made lowercase.
    val_pr_2 = models.FloatField(db_column='VAL_PR_2', blank=True, null=True)  # Field name made lowercase.
    val_pr_3 = models.FloatField(db_column='VAL_PR_3', blank=True, null=True)  # Field name made lowercase.
    val_pr_4 = models.FloatField(db_column='VAL_PR_4', blank=True, null=True)  # Field name made lowercase.
    val_pr_5 = models.FloatField(db_column='VAL_PR_5', blank=True, null=True)  # Field name made lowercase.
    val_pr_6 = models.FloatField(db_column='VAL_PR_6', blank=True, null=True)  # Field name made lowercase.
    val_pr_7 = models.FloatField(db_column='VAL_PR_7', blank=True, null=True)  # Field name made lowercase.
    val_pr_8 = models.FloatField(db_column='VAL_PR_8', blank=True, null=True)  # Field name made lowercase.
    val_pr_9 = models.FloatField(db_column='VAL_PR_9', blank=True, null=True)  # Field name made lowercase.
    val_pr_10 = models.FloatField(db_column='VAL_PR_10', blank=True, null=True)  # Field name made lowercase.
    val_pr_11 = models.FloatField(db_column='VAL_PR_11', blank=True, null=True)  # Field name made lowercase.
    val_pr_12 = models.FloatField(db_column='VAL_PR_12', blank=True, null=True)  # Field name made lowercase.
    annee = models.CharField(db_column='ANNEE', max_length=4, blank=True, null=True)  # Field name made lowercase.
    code_po = models.CharField(db_column='CODE_PO', max_length=4, blank=True, null=True)  # Field name made lowercase.
    cle_pr = models.CharField(db_column='CLE_PR', max_length=12, blank=True, null=True)  # Field name made lowercase.
    cle_prod = models.CharField(db_column='CLE_PROD', max_length=14, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PRESTAT2021'


class Prestat2022(models.Model):
    nat_ch = models.CharField(db_column='NAT_CH', max_length=2, blank=True, null=True)  # Field name made lowercase.
    type_ch = models.CharField(db_column='TYPE_CH', max_length=1, blank=True, null=True)  # Field name made lowercase.
    code_ch = models.CharField(db_column='CODE_CH', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cdvent_pr = models.CharField(db_column='CDVENT_PR', max_length=1, blank=True, null=True)  # Field name made lowercase.
    qte_pr_1 = models.FloatField(db_column='QTE_PR_1', blank=True, null=True)  # Field name made lowercase.
    qte_pr_2 = models.FloatField(db_column='QTE_PR_2', blank=True, null=True)  # Field name made lowercase.
    qte_pr_3 = models.FloatField(db_column='QTE_PR_3', blank=True, null=True)  # Field name made lowercase.
    qte_pr_4 = models.FloatField(db_column='QTE_PR_4', blank=True, null=True)  # Field name made lowercase.
    qte_pr_5 = models.FloatField(db_column='QTE_PR_5', blank=True, null=True)  # Field name made lowercase.
    qte_pr_6 = models.FloatField(db_column='QTE_PR_6', blank=True, null=True)  # Field name made lowercase.
    qte_pr_7 = models.FloatField(db_column='QTE_PR_7', blank=True, null=True)  # Field name made lowercase.
    qte_pr_8 = models.FloatField(db_column='QTE_PR_8', blank=True, null=True)  # Field name made lowercase.
    qte_pr_9 = models.FloatField(db_column='QTE_PR_9', blank=True, null=True)  # Field name made lowercase.
    qte_pr_10 = models.FloatField(db_column='QTE_PR_10', blank=True, null=True)  # Field name made lowercase.
    qte_pr_11 = models.FloatField(db_column='QTE_PR_11', blank=True, null=True)  # Field name made lowercase.
    qte_pr_12 = models.FloatField(db_column='QTE_PR_12', blank=True, null=True)  # Field name made lowercase.
    val_pr_1 = models.FloatField(db_column='VAL_PR_1', blank=True, null=True)  # Field name made lowercase.
    val_pr_2 = models.FloatField(db_column='VAL_PR_2', blank=True, null=True)  # Field name made lowercase.
    val_pr_3 = models.FloatField(db_column='VAL_PR_3', blank=True, null=True)  # Field name made lowercase.
    val_pr_4 = models.FloatField(db_column='VAL_PR_4', blank=True, null=True)  # Field name made lowercase.
    val_pr_5 = models.FloatField(db_column='VAL_PR_5', blank=True, null=True)  # Field name made lowercase.
    val_pr_6 = models.FloatField(db_column='VAL_PR_6', blank=True, null=True)  # Field name made lowercase.
    val_pr_7 = models.FloatField(db_column='VAL_PR_7', blank=True, null=True)  # Field name made lowercase.
    val_pr_8 = models.FloatField(db_column='VAL_PR_8', blank=True, null=True)  # Field name made lowercase.
    val_pr_9 = models.FloatField(db_column='VAL_PR_9', blank=True, null=True)  # Field name made lowercase.
    val_pr_10 = models.FloatField(db_column='VAL_PR_10', blank=True, null=True)  # Field name made lowercase.
    val_pr_11 = models.FloatField(db_column='VAL_PR_11', blank=True, null=True)  # Field name made lowercase.
    val_pr_12 = models.FloatField(db_column='VAL_PR_12', blank=True, null=True)  # Field name made lowercase.
    annee = models.CharField(db_column='ANNEE', max_length=4, blank=True, null=True)  # Field name made lowercase.
    code_po = models.CharField(db_column='CODE_PO', max_length=4, blank=True, null=True)  # Field name made lowercase.
    cle_pr = models.CharField(db_column='CLE_PR', max_length=12, blank=True, null=True)  # Field name made lowercase.
    cle_prod = models.CharField(db_column='CLE_PROD', max_length=14, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PRESTAT2022'


class Prestat2023(models.Model):
    nat_ch = models.CharField(db_column='NAT_CH', max_length=2, blank=True, null=True)  # Field name made lowercase.
    type_ch = models.CharField(db_column='TYPE_CH', max_length=1, blank=True, null=True)  # Field name made lowercase.
    code_ch = models.CharField(db_column='CODE_CH', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cdvent_pr = models.CharField(db_column='CDVENT_PR', max_length=1, blank=True, null=True)  # Field name made lowercase.
    qte_pr_1 = models.FloatField(db_column='QTE_PR_1', blank=True, null=True)  # Field name made lowercase.
    qte_pr_2 = models.FloatField(db_column='QTE_PR_2', blank=True, null=True)  # Field name made lowercase.
    qte_pr_3 = models.FloatField(db_column='QTE_PR_3', blank=True, null=True)  # Field name made lowercase.
    qte_pr_4 = models.FloatField(db_column='QTE_PR_4', blank=True, null=True)  # Field name made lowercase.
    qte_pr_5 = models.FloatField(db_column='QTE_PR_5', blank=True, null=True)  # Field name made lowercase.
    qte_pr_6 = models.FloatField(db_column='QTE_PR_6', blank=True, null=True)  # Field name made lowercase.
    qte_pr_7 = models.FloatField(db_column='QTE_PR_7', blank=True, null=True)  # Field name made lowercase.
    qte_pr_8 = models.FloatField(db_column='QTE_PR_8', blank=True, null=True)  # Field name made lowercase.
    qte_pr_9 = models.FloatField(db_column='QTE_PR_9', blank=True, null=True)  # Field name made lowercase.
    qte_pr_10 = models.FloatField(db_column='QTE_PR_10', blank=True, null=True)  # Field name made lowercase.
    qte_pr_11 = models.FloatField(db_column='QTE_PR_11', blank=True, null=True)  # Field name made lowercase.
    qte_pr_12 = models.FloatField(db_column='QTE_PR_12', blank=True, null=True)  # Field name made lowercase.
    val_pr_1 = models.FloatField(db_column='VAL_PR_1', blank=True, null=True)  # Field name made lowercase.
    val_pr_2 = models.FloatField(db_column='VAL_PR_2', blank=True, null=True)  # Field name made lowercase.
    val_pr_3 = models.FloatField(db_column='VAL_PR_3', blank=True, null=True)  # Field name made lowercase.
    val_pr_4 = models.FloatField(db_column='VAL_PR_4', blank=True, null=True)  # Field name made lowercase.
    val_pr_5 = models.FloatField(db_column='VAL_PR_5', blank=True, null=True)  # Field name made lowercase.
    val_pr_6 = models.FloatField(db_column='VAL_PR_6', blank=True, null=True)  # Field name made lowercase.
    val_pr_7 = models.FloatField(db_column='VAL_PR_7', blank=True, null=True)  # Field name made lowercase.
    val_pr_8 = models.FloatField(db_column='VAL_PR_8', blank=True, null=True)  # Field name made lowercase.
    val_pr_9 = models.FloatField(db_column='VAL_PR_9', blank=True, null=True)  # Field name made lowercase.
    val_pr_10 = models.FloatField(db_column='VAL_PR_10', blank=True, null=True)  # Field name made lowercase.
    val_pr_11 = models.FloatField(db_column='VAL_PR_11', blank=True, null=True)  # Field name made lowercase.
    val_pr_12 = models.FloatField(db_column='VAL_PR_12', blank=True, null=True)  # Field name made lowercase.
    annee = models.CharField(db_column='ANNEE', max_length=4, blank=True, null=True)  # Field name made lowercase.
    code_po = models.CharField(db_column='CODE_PO', max_length=4, blank=True, null=True)  # Field name made lowercase.
    cle_pr = models.CharField(db_column='CLE_PR', max_length=12, blank=True, null=True)  # Field name made lowercase.
    cle_prod = models.CharField(db_column='CLE_PROD', max_length=14, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PRESTAT2023'


class Permission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey(ContentType, models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'Permission'


class Remboursement(models.Model):
    id_remb = models.AutoField(db_column='Id_Remb', primary_key=True)  # Field name made lowercase.
    montant = models.FloatField(db_column='Montant')  # Field name made lowercase.
    avance = models.ForeignKey(Avances, models.DO_NOTHING, db_column='Avance', blank=True, null=True)  # Field name made lowercase.
    num_facture = models.ForeignKey(Factures, models.DO_NOTHING, db_column='Num_Facture', blank=True, null=True)  # Field name made lowercase.
    est_bloquer = models.BooleanField(db_column='Est_Bloquer')  # Field name made lowercase.
    user_id = models.CharField(db_column='User_ID', max_length=15, blank=True, null=True)  # Field name made lowercase.
    date_modification = models.DateTimeField(db_column='Date_Modification', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Remboursement'


class Session(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'Session'


class TabActivite(models.Model):
    code_activite = models.CharField(db_column='Code_Activite', primary_key=True, max_length=4)  # Field name made lowercase.
    libelle_activite = models.CharField(db_column='Libelle_Activite', max_length=50, blank=True, null=True)  # Field name made lowercase.
    je_l_utilise = models.BooleanField(db_column='Je_L_Utilise', blank=True, null=True)  # Field name made lowercase.
    est_bloquer = models.BooleanField(db_column='Est_Bloquer', blank=True, null=True)  # Field name made lowercase.
    user_id = models.CharField(db_column='User_ID', max_length=15, blank=True, null=True)  # Field name made lowercase.
    date_modification = models.DateTimeField(db_column='Date_Modification', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tab_Activite'


class TabActiviteTaches(models.Model):
    code_site = models.OneToOneField('TabNtTaches', models.DO_NOTHING, db_column='Code_site', primary_key=True)  # Field name made lowercase. The composite primary key (Code_site, NT, Code_GroupeActivite, Code_Activite, Code_Tache) found, that is not supported. The first column is selected.
    nt = models.ForeignKey('TabNtTaches', models.DO_NOTHING, db_column='NT', to_field='NT', related_name='tabactivitetaches_nt_set')  # Field name made lowercase.
    code_groupeactivite = models.ForeignKey('TabGroupeactiviteActivite', models.DO_NOTHING, db_column='Code_GroupeActivite')  # Field name made lowercase.
    code_activite = models.ForeignKey('TabGroupeactiviteActivite', models.DO_NOTHING, db_column='Code_Activite', related_name='tabactivitetaches_code_activite_set')  # Field name made lowercase.
    code_tache = models.ForeignKey('TabNtTaches', models.DO_NOTHING, db_column='Code_Tache', to_field='NT', related_name='tabactivitetaches_code_tache_set')  # Field name made lowercase.
    est_bloquer = models.BooleanField(db_column='Est_Bloquer', blank=True, null=True)  # Field name made lowercase.
    user_id = models.CharField(db_column='User_ID', max_length=15, blank=True, null=True)  # Field name made lowercase.
    date_modification = models.DateTimeField(db_column='Date_Modification', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tab_Activite_Taches'
        unique_together = (('code_site', 'nt', 'code_groupeactivite', 'code_activite', 'code_tache'),)


class TabAffectationAgent(models.Model):
    id_affectation_agent = models.AutoField(db_column='ID_Affectation_Agent', primary_key=True)  # Field name made lowercase.
    matricule = models.ForeignKey('TabAgent', models.DO_NOTHING, db_column='Matricule')  # Field name made lowercase.
    code_contrat = models.ForeignKey('TabAgentContrat', models.DO_NOTHING, db_column='Code_Contrat', blank=True, null=True)  # Field name made lowercase.
    code_structure = models.ForeignKey('TabStructures', models.DO_NOTHING, db_column='Code_Structure', blank=True, null=True)  # Field name made lowercase.
    motif_affectation = models.TextField(db_column='Motif_Affectation', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    date_affectation = models.DateField(db_column='Date_Affectation', blank=True, null=True)  # Field name made lowercase.
    date_fin_affectation = models.DateField(db_column='Date_Fin_Affectation', blank=True, null=True)  # Field name made lowercase.
    nbr_affectation = models.IntegerField(db_column='Nbr_Affectation')  # Field name made lowercase.
    code_decision = models.CharField(db_column='Code_Decision', max_length=18, blank=True, null=True)  # Field name made lowercase.
    est_bloquer = models.BooleanField(db_column='Est_Bloquer', blank=True, null=True)  # Field name made lowercase.
    user_id = models.CharField(db_column='User_ID', max_length=15, blank=True, null=True)  # Field name made lowercase.
    date_modification = models.DateTimeField(db_column='Date_Modification', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tab_Affectation_Agent'
        unique_together = (('matricule', 'nbr_affectation'),)


class TabAgence(models.Model):
    code_agence = models.CharField(db_column='Code_Agence', primary_key=True, max_length=15)  # Field name made lowercase.
