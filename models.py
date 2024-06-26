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
    id_attachement = models.CharField(db_column='Id_Attachement', primary_key=True, max_length=30)  # Field name made lowercase.
    num_marche = models.ForeignKey('Marche', models.DO_NOTHING, db_column='Num_Marche', blank=True, null=True)  # Field name made lowercase.
    code_site = models.ForeignKey('TabNtTaches', models.DO_NOTHING, db_column='Code_Site', to_field='NT')  # Field name made lowercase.
    nt = models.ForeignKey('TabNtTaches', models.DO_NOTHING, db_column='NT', to_field='NT', related_name='attachements_nt_set')  # Field name made lowercase.
    code_tache = models.ForeignKey('TabNtTaches', models.DO_NOTHING, db_column='Code_Tache', to_field='NT', related_name='attachements_code_tache_set')  # Field name made lowercase.
    quantite = models.FloatField(db_column='Quantite', blank=True, null=True)  # Field name made lowercase.
    prix_unitaire = models.FloatField(db_column='Prix_Unitaire', blank=True, null=True)  # Field name made lowercase.
    montant = models.FloatField(db_column='Montant', blank=True, null=True)  # Field name made lowercase.
    mmaa = models.DateField(db_column='Mmaa')  # Field name made lowercase.
    est_bloquer = models.BooleanField(db_column='Est_Bloquer', blank=True, null=True)  # Field name made lowercase.
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
    id_avance = models.CharField(db_column='Id_Avance', primary_key=True, max_length=30)  # Field name made lowercase.
    num_avance = models.IntegerField(db_column='Num_Avance')  # Field name made lowercase.
    montant = models.FloatField(db_column='Montant')  # Field name made lowercase.
    taux_debut_remb = models.FloatField(db_column='Taux_Debut_Remb', blank=True, null=True)  # Field name made lowercase.
    taux_fin_remb = models.FloatField(db_column='Taux_Fin_Remb', blank=True, null=True)  # Field name made lowercase.
    date_avance = models.DateField(db_column='Date_Avance')  # Field name made lowercase.
    remboursee = models.BooleanField(db_column='Remboursee', blank=True, null=True)  # Field name made lowercase.
    num_marche_field = models.ForeignKey('Marche', models.DO_NOTHING, db_column='Num_Marche ')  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    type_avance = models.ForeignKey('TypeAvance', models.DO_NOTHING, db_column='Type_Avance')  # Field name made lowercase.
    est_bloquer = models.BooleanField(db_column='Est_Bloquer', blank=True, null=True)  # Field name made lowercase.
    user_id = models.CharField(db_column='User_ID', max_length=15, blank=True, null=True)  # Field name made lowercase.
    date_modification = models.DateTimeField(db_column='Date_Modification', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Avances'


class Cautions(models.Model):
    id_caution = models.CharField(db_column='Id_Caution', primary_key=True, max_length=30)  # Field name made lowercase.
    date_soumission = models.DateField(db_column='Date_Soumission')  # Field name made lowercase.
    montant = models.FloatField(db_column='Montant')  # Field name made lowercase.
    est_recupere = models.BooleanField(db_column='Est_Recupere', blank=True, null=True)  # Field name made lowercase.
    agence = models.ForeignKey('TabAgence', models.DO_NOTHING, db_column='Agence')  # Field name made lowercase.
    avance = models.ForeignKey(Avances, models.DO_NOTHING, db_column='Avance', blank=True, null=True)  # Field name made lowercase.
    num_marche = models.ForeignKey('Marche', models.DO_NOTHING, db_column='Num_Marche', blank=True, null=True)  # Field name made lowercase.
    type_caution = models.ForeignKey('TypeCaution', models.DO_NOTHING, db_column='Type_Caution')  # Field name made lowercase.
    est_bloquer = models.BooleanField(db_column='Est_Bloquer', blank=True, null=True)  # Field name made lowercase.
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
    num_facture = models.ForeignKey('Factures', models.DO_NOTHING, db_column='Num_Facture')  # Field name made lowercase.
    detail = models.ForeignKey(Attachements, models.DO_NOTHING, db_column='Detail')  # Field name made lowercase.
    est_bloquer = models.BooleanField(db_column='Est_Bloquer', blank=True, null=True)  # Field name made lowercase.
    user_id = models.CharField(db_column='User_ID', max_length=15, blank=True, null=True)  # Field name made lowercase.
    date_modification = models.DateTimeField(db_column='Date_Modification', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Detail_Facture'


class DetailFactureAnnule(models.Model):
    id_df = models.AutoField(db_column='Id_Df', primary_key=True)  # Field name made lowercase.
    num_facture = models.CharField(db_column='Num_Facture', max_length=30, blank=True, null=True)  # Field name made lowercase.
    detail = models.CharField(db_column='Detail', max_length=30, blank=True, null=True)  # Field name made lowercase.
    est_bloquer = models.BooleanField(db_column='Est_Bloquer', blank=True, null=True)  # Field name made lowercase.
    user_id = models.CharField(db_column='User_ID', max_length=15, blank=True, null=True)  # Field name made lowercase.
    date_modification = models.DateTimeField(db_column='Date_Modification', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Detail_Facture_Annule'


class Encaissements(models.Model):
    id_enc = models.BigAutoField(db_column='Id_Enc', primary_key=True)  # Field name made lowercase.
    date_encaissement = models.DateField(db_column='Date_Encaissement')  # Field name made lowercase.
    montant_encaisse = models.FloatField(db_column='Montant_Encaisse')  # Field name made lowercase.
    numero_piece = models.CharField(db_column='Numero_Piece', max_length=30)  # Field name made lowercase.
    agence = models.ForeignKey('TabAgence', models.DO_NOTHING, db_column='Agence', blank=True, null=True)  # Field name made lowercase.
    facture = models.ForeignKey('Factures', models.DO_NOTHING, db_column='Facture')  # Field name made lowercase.
    mode_paiement = models.ForeignKey('ModePaiement', models.DO_NOTHING, db_column='Mode_Paiement', blank=True, null=True)  # Field name made lowercase.
    est_bloquer = models.BooleanField(db_column='Est_Bloquer', blank=True, null=True)  # Field name made lowercase.
    user_id = models.CharField(db_column='User_ID', max_length=15, blank=True, null=True)  # Field name made lowercase.
    date_modification = models.DateTimeField(db_column='Date_Modification', blank=True, null=True)  # Field name made lowercase.

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
    num_facture = models.CharField(db_column='Num_Facture', primary_key=True, max_length=30)  # Field name made lowercase.
    num_situation = models.IntegerField(db_column='Num_Situation')  # Field name made lowercase.
    date_debut = models.DateField(db_column='Date_Debut')  # Field name made lowercase.
    date_fin = models.DateField(db_column='Date_Fin')  # Field name made lowercase.
    date_facture = models.DateField(db_column='Date_Facture')  # Field name made lowercase.
    montant_mois = models.FloatField(db_column='Montant_Mois', blank=True, null=True)  # Field name made lowercase.
    montant_rb = models.FloatField(db_column='Montant_RB', blank=True, null=True)  # Field name made lowercase.
    montant_rg = models.FloatField(db_column='Montant_RG', blank=True, null=True)  # Field name made lowercase.
    paye = models.BooleanField(db_column='Paye', blank=True, null=True)  # Field name made lowercase.
    num_marche = models.ForeignKey('Marche', models.DO_NOTHING, db_column='Num_Marche')  # Field name made lowercase.
    est_bloquer = models.BooleanField(db_column='Est_Bloquer', blank=True, null=True)  # Field name made lowercase.
    user_id = models.CharField(db_column='User_ID', max_length=15, blank=True, null=True)  # Field name made lowercase.
    date_modification = models.DateTimeField(db_column='Date_Modification', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Factures'


class FacturesAnnulees(models.Model):
    num_facture = models.CharField(db_column='Num_Facture', max_length=30)  # Field name made lowercase.
    num_situation = models.IntegerField(db_column='Num_Situation')  # Field name made lowercase.
    date_debut = models.DateField(db_column='Date_Debut')  # Field name made lowercase.
    date_fin = models.DateField(db_column='Date_Fin')  # Field name made lowercase.
    date_facture = models.DateField(db_column='Date_Facture')  # Field name made lowercase.
    montant_mois = models.FloatField(db_column='Montant_Mois', blank=True, null=True)  # Field name made lowercase.
    montant_rb = models.FloatField(db_column='Montant_RB', blank=True, null=True)  # Field name made lowercase.
    montant_rg = models.FloatField(db_column='Montant_RG', blank=True, null=True)  # Field name made lowercase.
    paye = models.BooleanField(db_column='Paye', blank=True, null=True)  # Field name made lowercase.
    num_marche = models.CharField(db_column='Num_Marche', max_length=25)  # Field name made lowercase.
    est_bloquer = models.BooleanField(db_column='Est_Bloquer', blank=True, null=True)  # Field name made lowercase.
    user_id = models.CharField(db_column='User_ID', max_length=15, blank=True, null=True)  # Field name made lowercase.
    date_modification = models.DateTimeField(db_column='Date_Modification', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Factures_Annulees'


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
    num_contrat = models.CharField(db_column='Num_Contrat', primary_key=True, max_length=25)  # Field name made lowercase.
    num_avenant = models.IntegerField(db_column='Num_Avenant', blank=True, null=True)  # Field name made lowercase.
    code_site = models.ForeignKey('TabNt', models.DO_NOTHING, db_column='Code_Site', to_field='NT')  # Field name made lowercase.
    nt = models.ForeignKey('TabNt', models.DO_NOTHING, db_column='NT', to_field='NT', related_name='marche_nt_set')  # Field name made lowercase.
    libelle = models.TextField(db_column='Libelle', blank=True, null=True)  # Field name made lowercase.
    ods_depart = models.DateField(db_column='Ods_Depart')  # Field name made lowercase.
    delais = models.IntegerField(db_column='Delais', blank=True, null=True)  # Field name made lowercase.
    revisable = models.BooleanField(db_column='Revisable', blank=True, null=True)  # Field name made lowercase.
    actualisable = models.BooleanField(db_column='Actualisable', blank=True, null=True)  # Field name made lowercase.
    delai_paiement_f = models.IntegerField(db_column='Delai_Paiement_F', blank=True, null=True)  # Field name made lowercase.
    rabais = models.FloatField(db_column='Rabais', blank=True, null=True)  # Field name made lowercase.
    tva = models.FloatField(db_column='Tva', blank=True, null=True)  # Field name made lowercase.
    rg = models.FloatField(db_column='Rg', blank=True, null=True)  # Field name made lowercase.
    date_signature = models.DateField(db_column='Date_Signature')  # Field name made lowercase.
    est_bloquer = models.BooleanField(db_column='Est_Bloquer', blank=True, null=True)  # Field name made lowercase.
    user_id = models.CharField(db_column='User_ID', max_length=15, blank=True, null=True)  # Field name made lowercase.
    date_modification = models.DateTimeField(db_column='Date_Modification', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Marche'


class MarcheAvenant(models.Model):
    num_contrat = models.CharField(db_column='Num_Contrat', primary_key=True, max_length=25)  # Field name made lowercase. The composite primary key (Num_Contrat, Num_Avenant) found, that is not supported. The first column is selected.
    num_avenant = models.IntegerField(db_column='Num_Avenant')  # Field name made lowercase.
    code_site = models.ForeignKey('TabNt', models.DO_NOTHING, db_column='Code_Site', to_field='NT')  # Field name made lowercase.
    nt = models.ForeignKey('TabNt', models.DO_NOTHING, db_column='NT', to_field='NT', related_name='marcheavenant_nt_set')  # Field name made lowercase.
    libelle = models.TextField(db_column='Libelle', blank=True, null=True)  # Field name made lowercase.
    ods_depart = models.DateField(db_column='Ods_Depart')  # Field name made lowercase.
    delais = models.IntegerField(db_column='Delais', blank=True, null=True)  # Field name made lowercase.
    revisable = models.BooleanField(db_column='Revisable', blank=True, null=True)  # Field name made lowercase.
    actualisable = models.BooleanField(db_column='Actualisable', blank=True, null=True)  # Field name made lowercase.
    delai_paiement_f = models.IntegerField(db_column='Delai_Paiement_F', blank=True, null=True)  # Field name made lowercase.
    rabais = models.FloatField(db_column='Rabais', blank=True, null=True)  # Field name made lowercase.
    tva = models.FloatField(db_column='Tva', blank=True, null=True)  # Field name made lowercase.
    rg = models.FloatField(db_column='Rg', blank=True, null=True)  # Field name made lowercase.
    date_signature = models.DateField(db_column='Date_Signature')  # Field name made lowercase.
    est_bloquer = models.BooleanField(db_column='Est_Bloquer', blank=True, null=True)  # Field name made lowercase.
    user_id = models.CharField(db_column='User_ID', max_length=15, blank=True, null=True)  # Field name made lowercase.
    date_modification = models.DateTimeField(db_column='Date_Modification', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Marche_Avenant'
        unique_together = (('num_contrat', 'num_avenant'),)


class ModePaiement(models.Model):
    id_mode = models.CharField(db_column='Id_Mode', primary_key=True, max_length=3)  # Field name made lowercase.
    libelle = models.CharField(max_length=50)
    est_bloquer = models.BooleanField(db_column='Est_Bloquer', blank=True, null=True)  # Field name made lowercase.
    user_id = models.CharField(db_column='User_ID', max_length=15, blank=True, null=True)  # Field name made lowercase.
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


class PenaliteRetard(models.Model):
    id_penalite = models.AutoField(db_column='Id_Penalite', primary_key=True)  # Field name made lowercase.
    montant = models.FloatField(db_column='Montant')  # Field name made lowercase.
    num_facture = models.ForeignKey(Factures, models.DO_NOTHING, db_column='Num_Facture', blank=True, null=True)  # Field name made lowercase.
    est_bloquer = models.BooleanField(db_column='Est_Bloquer', blank=True, null=True)  # Field name made lowercase.
    user_id = models.CharField(db_column='User_ID', max_length=15, blank=True, null=True)  # Field name made lowercase.
    date_modification = models.DateTimeField(db_column='Date_Modification', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Penalite_Retard'


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
    est_bloquer = models.BooleanField(db_column='Est_Bloquer', blank=True, null=True)  # Field name made lowercase.
    user_id = models.CharField(db_column='User_ID', max_length=15, blank=True, null=True)  # Field name made lowercase.
    date_modification = models.DateTimeField(db_column='Date_Modification', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Remboursement'


class RemboursementAnnule(models.Model):
    id_remb_annuler = models.AutoField(db_column='Id_Remb_Annuler', primary_key=True)  # Field name made lowercase.
    montant = models.FloatField(db_column='Montant')  # Field name made lowercase.
    avance = models.CharField(db_column='Avance', max_length=30, blank=True, null=True)  # Field name made lowercase.
    num_facture = models.CharField(db_column='Num_Facture', max_length=30, blank=True, null=True)  # Field name made lowercase.
    est_bloquer = models.BooleanField(db_column='Est_Bloquer', blank=True, null=True)  # Field name made lowercase.
    user_id = models.CharField(db_column='User_ID', max_length=15, blank=True, null=True)  # Field name made lowercase.
    date_modification = models.DateTimeField(db_column='Date_Modification', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Remboursement_Annule'


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
    code_banque = models.ForeignKey('TabBanque', models.DO_NOTHING, db_column='Code_banque')  # Field name made lowercase.
    libelle_agence = models.CharField(db_column='Libelle_Agence', max_length=50)  # Field name made lowercase.
    compte_comptable = models.CharField(db_column='Compte_Comptable', max_length=10, blank=True, null=True)  # Field name made lowercase.
    est_bloquer = models.BooleanField(db_column='Est_Bloquer', blank=True, null=True)  # Field name made lowercase.
    user_id = models.CharField(db_column='User_ID', max_length=15, blank=True, null=True)  # Field name made lowercase.
    date_modification = models.DateTimeField(db_column='Date_Modification', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tab_Agence'


class TabAgent(models.Model):
    matricule = models.CharField(db_column='Matricule', primary_key=True, max_length=15)  # Field name made lowercase.
    prenom = models.CharField(db_column='Prenom', max_length=30, blank=True, null=True)  # Field name made lowercase.
    nom = models.CharField(db_column='Nom', max_length=30, blank=True, null=True)  # Field name made lowercase.
    code_commune_residence = models.CharField(db_column='Code_Commune_Residence', max_length=10, blank=True, null=True)  # Field name made lowercase.
    code_commune_naissance = models.CharField(db_column='Code_Commune_Naissance', max_length=10, blank=True, null=True)  # Field name made lowercase.
    date_naissance = models.DateField(db_column='Date_Naissance', blank=True, null=True)  # Field name made lowercase.
    num_ss = models.CharField(db_column='Num_SS', max_length=20, blank=True, null=True)  # Field name made lowercase.
    nationalite = models.CharField(db_column='Nationalite', max_length=15, blank=True, null=True)  # Field name made lowercase.
    nbr_enfant = models.SmallIntegerField(db_column='Nbr_Enfant', blank=True, null=True)  # Field name made lowercase.
    observation = models.TextField(db_column='Observation', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    photo = models.BinaryField(db_column='Photo', blank=True, null=True)  # Field name made lowercase.
    nbr_annee_exp_hors_entreprise = models.SmallIntegerField(db_column='Nbr_Annee_Exp_Hors_Entreprise', blank=True, null=True)  # Field name made lowercase.
    distance_km = models.FloatField(db_column='Distance_KM', blank=True, null=True)  # Field name made lowercase.
    code_dossier = models.CharField(db_column='Code_Dossier', max_length=15, blank=True, null=True)  # Field name made lowercase.
    type_charge_agent = models.SmallIntegerField(db_column='Type_Charge_Agent', blank=True, null=True)  # Field name made lowercase.
    nbr_annee_exp_entreprise = models.SmallIntegerField(db_column='Nbr_Annee_Exp_Entreprise', blank=True, null=True)  # Field name made lowercase.
    civilite = models.SmallIntegerField(db_column='Civilite', blank=True, null=True)  # Field name made lowercase.
    genre = models.CharField(db_column='Genre', max_length=1, blank=True, null=True)  # Field name made lowercase.
    code_caisse = models.ForeignKey('TabCaisseCotisation', models.DO_NOTHING, db_column='Code_Caisse', blank=True, null=True)  # Field name made lowercase.
    annee_presumee = models.IntegerField(db_column='Annee_Presumee', blank=True, null=True)  # Field name made lowercase.
    ancien_matricule = models.ForeignKey('self', models.DO_NOTHING, db_column='Ancien_Matricule', blank=True, null=True)  # Field name made lowercase.
    avec_mutuel = models.BooleanField(db_column='Avec_Mutuel', blank=True, null=True)  # Field name made lowercase.
    montant_assurance_groupe = models.DecimalField(db_column='Montant_Assurance_Groupe', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    avec_cacobath = models.BooleanField(db_column='Avec_Cacobath', blank=True, null=True)  # Field name made lowercase.
    avec_chomage_intemperie = models.BooleanField(db_column='Avec_Chomage_Intemperie', blank=True, null=True)  # Field name made lowercase.
    avec_oprebat = models.BooleanField(db_column='Avec_Oprebat', blank=True, null=True)  # Field name made lowercase.
    groupe_sanguine = models.CharField(db_column='Groupe_Sanguine', max_length=3, blank=True, null=True)  # Field name made lowercase.
    est_apprenti = models.BooleanField(db_column='Est_Apprenti', blank=True, null=True)  # Field name made lowercase.
    est_maitre_apprentissage = models.BooleanField(db_column='Est_Maitre_Apprentissage', blank=True, null=True)  # Field name made lowercase.
    est_formateur = models.BooleanField(db_column='Est_Formateur', blank=True, null=True)  # Field name made lowercase.
    handicap = models.BooleanField(db_column='Handicap', blank=True, null=True)  # Field name made lowercase.
    abattement_irg = models.FloatField(db_column='Abattement_IRG', blank=True, null=True)  # Field name made lowercase.
    taux_cnas = models.FloatField(db_column='TAUX_CNAS', blank=True, null=True)  # Field name made lowercase.
    avec_abattement_cnas = models.BooleanField(db_column='Avec_Abattement_CNAS', blank=True, null=True)  # Field name made lowercase.
    nin = models.CharField(db_column='NIN', max_length=30, blank=True, null=True)  # Field name made lowercase.
    idnat = models.CharField(db_column='IdNat', max_length=30, blank=True, null=True)  # Field name made lowercase.
    user_id = models.CharField(db_column='User_ID', max_length=15, blank=True, null=True)  # Field name made lowercase.
    date_modification = models.DateTimeField(db_column='Date_Modification', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tab_Agent'


class TabAgentCarriere(models.Model):
    id_agent_carriere = models.AutoField(db_column='ID_Agent_Carriere', primary_key=True)  # Field name made lowercase.
    matricule = models.ForeignKey(TabAgent, models.DO_NOTHING, db_column='Matricule')  # Field name made lowercase.
    nature = models.IntegerField(db_column='Nature', blank=True, null=True)  # Field name made lowercase.
    mat_exper = models.CharField(db_column='Mat_Exper', max_length=15, blank=True, null=True)  # Field name made lowercase.
    code_filiale = models.CharField(db_column='Code_Filiale', max_length=5, blank=True, null=True)  # Field name made lowercase.
    code_site = models.CharField(db_column='Code_site', max_length=10, blank=True, null=True)  # Field name made lowercase.
    raison_social = models.CharField(db_column='Raison_Social', max_length=50, blank=True, null=True)  # Field name made lowercase.
    libelle_poste_travail = models.CharField(db_column='Libelle_poste_travail', max_length=50, blank=True, null=True)  # Field name made lowercase.
    code_poste_travail = models.ForeignKey('TabPosteTravail', models.DO_NOTHING, db_column='Code_Poste_Travail', blank=True, null=True)  # Field name made lowercase.
    date_debut = models.DateField(db_column='Date_Debut', blank=True, null=True)  # Field name made lowercase.
    date_fin = models.DateField(db_column='Date_Fin', blank=True, null=True)  # Field name made lowercase.
    est_bloquer = models.BooleanField(db_column='Est_Bloquer', blank=True, null=True)  # Field name made lowercase.
    user_id = models.CharField(db_column='User_ID', max_length=15, blank=True, null=True)  # Field name made lowercase.
    date_modification = models.DateTimeField(db_column='Date_Modification', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tab_Agent_Carriere'
        unique_together = (('matricule', 'date_debut', 'date_fin', 'est_bloquer'),)


class TabAgentCompetences(models.Model):
    id_agent_competence = models.AutoField(db_column='ID_Agent_Competence', primary_key=True)  # Field name made lowercase.
    matricule = models.ForeignKey(TabAgent, models.DO_NOTHING, db_column='Matricule')  # Field name made lowercase.
    code_competence = models.ForeignKey('TabCompetences', models.DO_NOTHING, db_column='Code_Competence')  # Field name made lowercase.
    niveau_competence = models.SmallIntegerField(db_column='Niveau_Competence', blank=True, null=True)  # Field name made lowercase.
    est_bloquer = models.BooleanField(db_column='Est_Bloquer', blank=True, null=True)  # Field name made lowercase.
    user_id = models.CharField(db_column='User_ID', max_length=15, blank=True, null=True)  # Field name made lowercase.
    date_modification = models.DateTimeField(db_column='Date_Modification', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tab_Agent_Competences'
        unique_together = (('matricule', 'code_competence'),)


class TabAgentCongeAnnuel(models.Model):
    id_agent_conge_annuel = models.AutoField(db_column='ID_Agent_Conge_Annuel', primary_key=True)  # Field name made lowercase.
    matricule = models.ForeignKey(TabAgent, models.DO_NOTHING, db_column='Matricule')  # Field name made lowercase.
    date_debut_conge = models.DateField(db_column='Date_Debut_Conge', blank=True, null=True)  # Field name made lowercase.
    date_retour_prevu = models.DateField(db_column='Date_Retour_Prevu', blank=True, null=True)  # Field name made lowercase.
    date_retour_reel = models.DateField(db_column='Date_Retour_Reel', blank=True, null=True)  # Field name made lowercase.
    exercice = models.CharField(db_column='Exercice', max_length=10, blank=True, null=True)  # Field name made lowercase.
    nbr_jours_demander = models.SmallIntegerField(db_column='Nbr_Jours_Demander', blank=True, null=True)  # Field name made lowercase.
    nbr_jours_effectif = models.SmallIntegerField(db_column='Nbr_Jours_Effectif', blank=True, null=True)  # Field name made lowercase.
    etat_conge = models.SmallIntegerField(db_column='Etat_Conge', blank=True, null=True)  # Field name made lowercase.
    code_decision = models.CharField(db_column='Code_Decision', max_length=18, blank=True, null=True)  # Field name made lowercase.
    est_bloquer = models.BooleanField(db_column='Est_Bloquer', blank=True, null=True)  # Field name made lowercase.
    user_id = models.CharField(db_column='User_ID', max_length=15, blank=True, null=True)  # Field name made lowercase.
    date_modification = models.DateTimeField(db_column='Date_Modification', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tab_Agent_Conge_Annuel'
        unique_together = (('matricule', 'date_debut_conge'),)


class TabAgentConjoint(models.Model):
    code_agent_conjoint = models.CharField(db_column='Code_Agent_Conjoint', primary_key=True, max_length=18)  # Field name made lowercase.
    matricule = models.ForeignKey(TabAgent, models.DO_NOTHING, db_column='Matricule')  # Field name made lowercase.
    nom_conjoint = models.CharField(db_column='Nom_Conjoint', max_length=30, blank=True, null=True)  # Field name made lowercase.
    prenom_conjoint = models.CharField(db_column='Prenom_Conjoint', max_length=30, blank=True, null=True)  # Field name made lowercase.
    date_naissance_conjoint = models.DateField(db_column='Date_Naissance_Conjoint', blank=True, null=True)  # Field name made lowercase.
    code_commune_naissance = models.CharField(db_column='Code_Commune_Naissance', max_length=10, blank=True, null=True)  # Field name made lowercase.
    date_mariage = models.DateField(db_column='Date_Mariage', blank=True, null=True)  # Field name made lowercase.
    date_divorce = models.DateField(db_column='Date_Divorce', blank=True, null=True)  # Field name made lowercase.
    date_deces = models.DateField(db_column='Date_Deces', blank=True, null=True)  # Field name made lowercase.
    avec_emploi = models.BooleanField(db_column='Avec_Emploi', blank=True, null=True)  # Field name made lowercase.
    new_situation_famille = models.CharField(db_column='New_Situation_Famille', max_length=1, blank=True, null=True)  # Field name made lowercase.
    est_bloquer = models.BooleanField(db_column='Est_Bloquer', blank=True, null=True)  # Field name made lowercase.
    user_id = models.CharField(db_column='User_ID', max_length=15, blank=True, null=True)  # Field name made lowercase.
    date_modification = models.DateTimeField(db_column='Date_Modification', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tab_Agent_Conjoint'


class TabAgentContrat(models.Model):
    code_contrat = models.CharField(db_column='Code_Contrat', primary_key=True, max_length=18)  # Field name made lowercase.
    ref_contrat = models.CharField(db_column='Ref_Contrat', max_length=30, blank=True, null=True)  # Field name made lowercase.
    matricule = models.ForeignKey(TabAgent, models.DO_NOTHING, db_column='Matricule', blank=True, null=True)  # Field name made lowercase.
    nbr_contrat = models.SmallIntegerField(db_column='Nbr_Contrat', blank=True, null=True)  # Field name made lowercase.
    code_statut_horaire = models.ForeignKey('TabStatutHoraire', models.DO_NOTHING, db_column='Code_Statut_Horaire', blank=True, null=True)  # Field name made lowercase.
    date_debut_contrat = models.DateField(db_column='Date_Debut_Contrat', blank=True, null=True)  # Field name made lowercase.
    date_fin_contrat = models.DateField(db_column='Date_Fin_Contrat', blank=True, null=True)  # Field name made lowercase.
    duree_essai = models.SmallIntegerField(db_column='Duree_Essai', blank=True, null=True)  # Field name made lowercase.
    code_type_contrat = models.ForeignKey('TabTypeContrat', models.DO_NOTHING, db_column='Code_Type_Contrat', blank=True, null=True)  # Field name made lowercase.
    situation_contrat = models.SmallIntegerField(db_column='Situation_Contrat', blank=True, null=True)  # Field name made lowercase.
    observation = models.TextField(db_column='Observation', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    est_bloquer = models.BooleanField(db_column='Est_Bloquer', blank=True, null=True)  # Field name made lowercase.
    user_id = models.CharField(db_column='User_ID', max_length=15, blank=True, null=True)  # Field name made lowercase.
    date_modification = models.DateTimeField(db_column='Date_Modification', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tab_Agent_Contrat'


class TabAgentEnfants(models.Model):
    code_agent_enfant = models.CharField(db_column='Code_Agent_Enfant', primary_key=True, max_length=18)  # Field name made lowercase.
    matricule = models.ForeignKey(TabAgent, models.DO_NOTHING, db_column='Matricule')  # Field name made lowercase.
    genre = models.CharField(db_column='Genre', max_length=1, blank=True, null=True)  # Field name made lowercase.
    nom_enfant = models.CharField(db_column='Nom_Enfant', max_length=30, blank=True, null=True)  # Field name made lowercase.
    prenom_enfant = models.CharField(db_column='Prenom_Enfant', max_length=30, blank=True, null=True)  # Field name made lowercase.
    date_naissance_enfant = models.DateField(db_column='Date_Naissance_Enfant', blank=True, null=True)  # Field name made lowercase.
    code_commune_naissance = models.CharField(db_column='Code_Commune_Naissance', max_length=10, blank=True, null=True)  # Field name made lowercase.
    date_deces_enfant = models.DateField(db_column='Date_Deces_Enfant', blank=True, null=True)  # Field name made lowercase.
    scolarise = models.BooleanField(db_column='Scolarise', blank=True, null=True)  # Field name made lowercase.
    est_bloquer = models.BooleanField(db_column='Est_Bloquer', blank=True, null=True)  # Field name made lowercase.
    user_id = models.CharField(db_column='User_ID', max_length=15, blank=True, null=True)  # Field name made lowercase.
    date_modification = models.DateTimeField(db_column='Date_Modification', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tab_Agent_Enfants'


class TabAgentFormation(models.Model):
    id_agent_formation = models.AutoField(db_column='ID_Agent_Formation', primary_key=True)  # Field name made lowercase.
    code_agent_formation = models.CharField(db_column='Code_Agent_Formation', unique=True, max_length=25)  # Field name made lowercase.
    matricule = models.ForeignKey(TabAgent, models.DO_NOTHING, db_column='Matricule')  # Field name made lowercase.
    code_formation = models.ForeignKey('TabFormations', models.DO_NOTHING, db_column='Code_Formation')  # Field name made lowercase.
    obtention_diplome = models.BooleanField(db_column='Obtention_Diplome', blank=True, null=True)  # Field name made lowercase.
    mode_prise_en_charge = models.SmallIntegerField(db_column='Mode_Prise_En_Charge', blank=True, null=True)  # Field name made lowercase.
    est_bloquer = models.BooleanField(db_column='Est_Bloquer', blank=True, null=True)  # Field name made lowercase.
    user_id = models.CharField(db_column='User_ID', max_length=15, blank=True, null=True)  # Field name made lowercase.
    date_modification = models.DateTimeField(db_column='Date_Modification', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tab_Agent_Formation'


class TabAgentInformationComplementaire(models.Model):
    matricule = models.OneToOneField(TabAgent, models.DO_NOTHING, db_column='Matricule', primary_key=True)  # Field name made lowercase.
    etat_sante = models.CharField(db_column='Etat_Sante', max_length=30, blank=True, null=True)  # Field name made lowercase.
    service_national = models.SmallIntegerField(db_column='Service_National', blank=True, null=True)  # Field name made lowercase.
    date_debut_service = models.DateField(db_column='Date_Debut_Service', blank=True, null=True)  # Field name made lowercase.
    date_fin_service = models.DateField(db_column='Date_Fin_Service', blank=True, null=True)  # Field name made lowercase.
    num_passport = models.CharField(db_column='Num_Passport', max_length=20, blank=True, null=True)  # Field name made lowercase.
    date_passport = models.DateField(db_column='Date_Passport', blank=True, null=True)  # Field name made lowercase.
    num_piece_identite = models.CharField(db_column='Num_Piece_Identite', max_length=20, blank=True, null=True)  # Field name made lowercase.
    date_piece_identite = models.DateField(db_column='Date_Piece_Identite', blank=True, null=True)  # Field name made lowercase.
    num_acte_naissance = models.CharField(db_column='Num_Acte_Naissance', max_length=20, blank=True, null=True)  # Field name made lowercase.
    num_equipement = models.CharField(db_column='Num_Equipement', max_length=20, blank=True, null=True)  # Field name made lowercase.
    num_notification = models.CharField(db_column='Num_Notification', max_length=20, blank=True, null=True)  # Field name made lowercase.
    date_notification = models.DateField(db_column='Date_Notification', blank=True, null=True)  # Field name made lowercase.
    pointure = models.CharField(db_column='Pointure', max_length=5, blank=True, null=True)  # Field name made lowercase.
    taille_veste = models.CharField(db_column='Taille_Veste', max_length=5, blank=True, null=True)  # Field name made lowercase.
    taille_pantalon = models.CharField(db_column='Taille_Pantalon', max_length=5, blank=True, null=True)  # Field name made lowercase.
    taille_tour_tete = models.CharField(db_column='Taille_Tour_Tete', max_length=5, blank=True, null=True)  # Field name made lowercase.
    nom_papa = models.CharField(db_column='Nom_Papa', max_length=30, blank=True, null=True)  # Field name made lowercase.
    prenom_papa = models.CharField(db_column='Prenom_Papa', max_length=30, blank=True, null=True)  # Field name made lowercase.
    nom_mere = models.CharField(db_column='Nom_Mere', max_length=30, blank=True, null=True)  # Field name made lowercase.
    prenom_mere = models.CharField(db_column='Prenom_Mere', max_length=30, blank=True, null=True)  # Field name made lowercase.
    code_commune_pp = models.CharField(db_column='Code_Commune_PP', max_length=10, blank=True, null=True)  # Field name made lowercase.
    code_commune_pi = models.CharField(db_column='Code_Commune_PI', max_length=10, blank=True, null=True)  # Field name made lowercase.
    est_bloquer = models.BooleanField(db_column='Est_Bloquer', blank=True, null=True)  # Field name made lowercase.
    user_id = models.CharField(db_column='User_ID', max_length=15, blank=True, null=True)  # Field name made lowercase.
    date_modification = models.DateTimeField(db_column='Date_Modification', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tab_Agent_Information_Complementaire'


class TabAgentMoisArchive(models.Model):
    mmaa = models.ForeignKey('TabMoisPaieArchive', models.DO_NOTHING, db_column='Mmaa')  # Field name made lowercase.
    matricule = models.CharField(db_column='Matricule', primary_key=True, max_length=15)  # Field name made lowercase. The composite primary key (Matricule, Mmaa) found, that is not supported. The first column is selected.
    est_bloquer = models.BooleanField(db_column='Est_Bloquer', blank=True, null=True)  # Field name made lowercase.
    user_id = models.CharField(db_column='User_ID', max_length=15, blank=True, null=True)  # Field name made lowercase.
    date_modification = models.DateTimeField(db_column='Date_Modification', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tab_Agent_Mois_Archive'
        unique_together = (('matricule', 'mmaa'),)


class TabAgentPermisConduire(models.Model):
    numero_permis = models.CharField(db_column='Numero_Permis', max_length=30, blank=True, null=True)  # Field name made lowercase.
    matricule = models.OneToOneField(TabAgent, models.DO_NOTHING, db_column='Matricule', primary_key=True)  # Field name made lowercase. The composite primary key (Matricule, Categorie) found, that is not supported. The first column is selected.
    categorie = models.CharField(db_column='Categorie', max_length=5)  # Field name made lowercase.
    date_obtention = models.DateField(db_column='Date_Obtention', blank=True, null=True)  # Field name made lowercase.
    code_commune_pc = models.CharField(db_column='Code_Commune_PC', max_length=10, blank=True, null=True)  # Field name made lowercase.
    est_bloquer = models.BooleanField(db_column='Est_Bloquer', blank=True, null=True)  # Field name made lowercase.
    user_id = models.CharField(db_column='User_ID', max_length=15, blank=True, null=True)  # Field name made lowercase.
    date_modification = models.DateTimeField(db_column='Date_Modification', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tab_Agent_Permis_Conduire'
        unique_together = (('matricule', 'categorie'),)


class TabAgentPret(models.Model):
    id_agent_pret = models.AutoField(db_column='ID_Agent_Pret', primary_key=True)  # Field name made lowercase.
    code_pret = models.CharField(db_column='Code_Pret', unique=True, max_length=18)  # Field name made lowercase.
    type_pret = models.SmallIntegerField(db_column='Type_Pret', blank=True, null=True)  # Field name made lowercase.
    date_effectif_pret = models.DateField(db_column='Date_Effectif_Pret', blank=True, null=True)  # Field name made lowercase.
    date_debut = models.DateField(db_column='Date_Debut', blank=True, null=True)  # Field name made lowercase.
    date_fin_pret = models.DateField(db_column='Date_Fin_Pret', blank=True, null=True)  # Field name made lowercase.
    montant_pret = models.DecimalField(db_column='Montant_Pret', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    montant_mensuel = models.DecimalField(db_column='Montant_Mensuel', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    cumule_rembourse = models.DecimalField(db_column='Cumule_Rembourse', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    etat_pret = models.SmallIntegerField(db_column='Etat_Pret', blank=True, null=True)  # Field name made lowercase.
    matricule = models.ForeignKey(TabAgent, models.DO_NOTHING, db_column='Matricule', blank=True, null=True)  # Field name made lowercase.
    code_decision = models.CharField(db_column='Code_Decision', max_length=18, blank=True, null=True)  # Field name made lowercase.
    code_rubrique = models.ForeignKey('TabPlanRubriques', models.DO_NOTHING, db_column='Code_Rubrique', blank=True, null=True)  # Field name made lowercase.
    est_bloquer = models.BooleanField(db_column='Est_Bloquer', blank=True, null=True)  # Field name made lowercase.
    user_id = models.CharField(db_column='User_ID', max_length=15, blank=True, null=True)  # Field name made lowercase.
    date_modification = models.DateTimeField(db_column='Date_Modification', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tab_Agent_Pret'


class TabAgentQualification(models.Model):
    matricule = models.OneToOneField(TabAgent, models.DO_NOTHING, db_column='Matricule', primary_key=True)  # Field name made lowercase. The composite primary key (Matricule, Code_Qualification) found, that is not supported. The first column is selected.
    code_qualification = models.ForeignKey('TabQualification', models.DO_NOTHING, db_column='Code_Qualification')  # Field name made lowercase.
    est_principal = models.BooleanField(db_column='Est_Principal', blank=True, null=True)  # Field name made lowercase.
    est_bloquer = models.BooleanField(db_column='Est_Bloquer', blank=True, null=True)  # Field name made lowercase.
    user_id = models.CharField(db_column='User_ID', max_length=15, blank=True, null=True)  # Field name made lowercase.
    date_modification = models.DateTimeField(db_column='Date_Modification', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tab_Agent_Qualification'
        unique_together = (('matricule', 'code_qualification'),)


class TabApprentiMaitreApprenti(models.Model):
    id_apprenti_maitre_appr = models.AutoField(db_column='ID_Apprenti_Maitre_Appr', primary_key=True)  # Field name made lowercase.
    matricule_apprenti = models.ForeignKey(TabAgent, models.DO_NOTHING, db_column='Matricule_Apprenti', blank=True, null=True)  # Field name made lowercase.
    matricule_maitre_apprenti = models.ForeignKey(TabAgent, models.DO_NOTHING, db_column='Matricule_Maitre_Apprenti', related_name='tabapprentimaitreapprenti_matricule_maitre_apprenti_set', blank=True, null=True)  # Field name made lowercase.
    est_bloquer = models.BooleanField(db_column='Est_Bloquer', blank=True, null=True)  # Field name made lowercase.
    user_id = models.CharField(db_column='User_ID', max_length=15, blank=True, null=True)  # Field name made lowercase.
    date_modification = models.DateTimeField(db_column='Date_Modification', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tab_Apprenti_Maitre_Apprenti'
        unique_together = (('matricule_apprenti', 'matricule_maitre_apprenti', 'est_bloquer'),)


class TabArchivePaie(models.Model):
    id_archive_paie = models.AutoField(db_column='ID_Archive_Paie', primary_key=True)  # Field name made lowercase.
    code_information_bulletin_agent = models.ForeignKey('TabInformationBulletinAgent', models.DO_NOTHING, db_column='Code_Information_Bulletin_Agent', blank=True, null=True)  # Field name made lowercase.
    matricule = models.ForeignKey(TabAgentMoisArchive, models.DO_NOTHING, db_column='Matricule', to_field='Mmaa')  # Field name made lowercase.
    code_rubrique = models.ForeignKey('TabPlanRubriques', models.DO_NOTHING, db_column='Code_Rubrique')  # Field name made lowercase.
    mmaa = models.ForeignKey(TabAgentMoisArchive, models.DO_NOTHING, db_column='Mmaa', to_field='Mmaa', related_name='tabarchivepaie_mmaa_set')  # Field name made lowercase.
    base = models.DecimalField(db_column='Base', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    taux = models.FloatField(db_column='Taux', blank=True, null=True)  # Field name made lowercase.
    mmaad = models.DateField(db_column='Mmaad', blank=True, null=True)  # Field name made lowercase.
    mmaaf = models.DateField(db_column='Mmaaf', blank=True, null=True)  # Field name made lowercase.
    montant = models.DecimalField(db_column='Montant', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    observation = models.CharField(db_column='Observation', max_length=100, blank=True, null=True)  # Field name made lowercase.
    mode_saisie = models.SmallIntegerField(db_column='Mode_Saisie', blank=True, null=True)  # Field name made lowercase.
    user_id = models.CharField(db_column='User_ID', max_length=15, blank=True, null=True)  # Field name made lowercase.
    date_modification = models.DateTimeField(db_column='Date_Modification', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tab_Archive_Paie'
        unique_together = (('matricule', 'code_rubrique', 'mmaa', 'mmaad'),)


class TabAtelierproductionDestination(models.Model):
    code_structure = models.ForeignKey('TabStructures', models.DO_NOTHING, db_column='Code_Structure', blank=True, null=True)  # Field name made lowercase.
    code_structure_destination = models.CharField(db_column='Code_Structure_Destination', max_length=15, blank=True, null=True)  # Field name made lowercase.
    code_produit = models.ForeignKey('TabProduitManufacture', models.DO_NOTHING, db_column='Code_Produit', blank=True, null=True)  # Field name made lowercase.
    vers_atelier = models.BooleanField(db_column='Vers_Atelier', blank=True, null=True)  # Field name made lowercase.
    vers_nt = models.BooleanField(db_column='Vers_NT', blank=True, null=True)  # Field name made lowercase.
    vers_client_externe = models.BooleanField(db_column='Vers_Client_Externe', blank=True, null=True)  # Field name made lowercase.
    est_bloquer = models.BooleanField(db_column='Est_Bloquer', blank=True, null=True)  # Field name made lowercase.
    user_id = models.CharField(db_column='User_ID', max_length=15, blank=True, null=True)  # Field name made lowercase.
    date_modification = models.DateTimeField(db_column='Date_Modification', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tab_AtelierProduction_Destination'
        unique_together = (('code_structure', 'code_structure_destination', 'code_produit'),)


class TabBanque(models.Model):
    code_banque = models.CharField(db_column='Code_Banque', primary_key=True, max_length=15)  # Field name made lowercase.
    libelle_banque = models.CharField(db_column='Libelle_Banque', max_length=50, blank=True, null=True)  # Field name made lowercase.
    acronyme = models.CharField(db_column='Acronyme', max_length=20, blank=True, null=True)  # Field name made lowercase.
    est_bloquer = models.BooleanField(db_column='Est_Bloquer', blank=True, null=True)  # Field name made lowercase.
    user_id = models.CharField(db_column='User_ID', max_length=15, blank=True, null=True)  # Field name made lowercase.
    date_modification = models.DateTimeField(db_column='Date_Modification', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tab_Banque'


class TabCaisseCotisation(models.Model):
    code_caisse = models.CharField(db_column='Code_Caisse', primary_key=True, max_length=15)  # Field name made lowercase.
    libelle_caisse = models.CharField(db_column='Libelle_Caisse', max_length=50, blank=True, null=True)  # Field name made lowercase.
    num_ss_employeur = models.CharField(db_column='Num_SS_Employeur', max_length=20, blank=True, null=True)  # Field name made lowercase.
    est_bloquer = models.BooleanField(db_column='Est_Bloquer', blank=True, null=True)  # Field name made lowercase.
    user_id = models.CharField(db_column='User_ID', max_length=15, blank=True, null=True)  # Field name made lowercase.
    date_modification = models.DateTimeField(db_column='Date_Modification', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tab_Caisse_Cotisation'


class TabCalculPaie(models.Model):
    id_calcul_paie = models.AutoField(db_column='ID_Calcul_Paie', primary_key=True)  # Field name made lowercase.
    matricule = models.ForeignKey(TabAgent, models.DO_NOTHING, db_column='Matricule')  # Field name made lowercase.
    code_rubrique = models.ForeignKey('TabPlanRubriques', models.DO_NOTHING, db_column='Code_Rubrique')  # Field name made lowercase.
    base = models.DecimalField(db_column='Base', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    taux = models.FloatField(db_column='Taux', blank=True, null=True)  # Field name made lowercase.
    montant = models.DecimalField(db_column='Montant', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    mmaadb = models.DateField(db_column='Mmaadb', blank=True, null=True)  # Field name made lowercase.
    mmaadf = models.DateField(db_column='Mmaadf', blank=True, null=True)  # Field name made lowercase.
    observation = models.CharField(db_column='Observation', max_length=100, blank=True, null=True)  # Field name made lowercase.
    mode_saisie = models.SmallIntegerField(db_column='Mode_Saisie', blank=True, null=True)  # Field name made lowercase.
    user_id = models.CharField(db_column='User_ID', max_length=15, blank=True, null=True)  # Field name made lowercase.
    date_modification = models.DateTimeField(db_column='Date_Modification', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tab_Calcul_Paie'
        unique_together = (('matricule', 'code_rubrique', 'mmaadb'),)


class TabCharge(models.Model):
    code_charge = models.CharField(db_column='Code_Charge', primary_key=True, max_length=4)  # Field name made lowercase.
    libelle_charge = models.CharField(db_column='Libelle_Charge', max_length=50, blank=True, null=True)  # Field name made lowercase.
    code_type_charge = models.ForeignKey('TabTypeCharge', models.DO_NOTHING, db_column='Code_Type_Charge', blank=True, null=True)  # Field name made lowercase.
    code_nature_charge = models.CharField(db_column='Code_Nature_Charge', max_length=200, blank=True, null=True)  # Field name made lowercase.
    code_classification_charge = models.CharField(db_column='Code_Classification_Charge', max_length=200, blank=True, null=True)  # Field name made lowercase.
    type_location = models.SmallIntegerField(db_column='Type_Location', blank=True, null=True)  # Field name made lowercase.
    code_unite_mesure = models.ForeignKey('TabUniteDeMesure', models.DO_NOTHING, db_column='Code_Unite_Mesure', blank=True, null=True)  # Field name made lowercase.
    avec_quantite = models.BooleanField(db_column='Avec_Quantite', blank=True, null=True)  # Field name made lowercase.
    est_bloquer = models.BooleanField(db_column='Est_Bloquer', blank=True, null=True)  # Field name made lowercase.
    user_id = models.CharField(db_column='User_ID', max_length=15, blank=True, null=True)  # Field name made lowercase.
    date_modification = models.DateTimeField(db_column='Date_Modification', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tab_Charge'


class TabClassification(models.Model):
    code_categorie = models.CharField(db_column='Code_Categorie', max_length=10)  # Field name made lowercase.
    code_groupe = models.CharField(db_column='Code_Groupe', max_length=10)  # Field name made lowercase.
    code_section = models.CharField(db_column='Code_Section', max_length=20)  # Field name made lowercase.
    classification = models.CharField(db_column='Classification', primary_key=True, max_length=10)  # Field name made lowercase.
    montant = models.DecimalField(db_column='Montant', max_digits=19, decimal_places=4)  # Field name made lowercase.
    est_bloquer = models.BooleanField(db_column='Est_Bloquer')  # Field name made lowercase.
    user_id = models.CharField(db_column='User_ID', max_length=15, blank=True, null=True)  # Field name made lowercase.
    date_modification = models.DateTimeField(db_column='Date_Modification', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tab_Classification'


class TabClassificationCharge(models.Model):
    code_classification_charge = models.CharField(db_column='Code_Classification_Charge', primary_key=True, max_length=5)  # Field name made lowercase.
    libelle_classification_charge = models.CharField(db_column='Libelle_Classification_Charge', max_length=50, blank=True, null=True)  # Field name made lowercase.
    est_bloquer = models.BooleanField(db_column='Est_Bloquer', blank=True, null=True)  # Field name made lowercase.
    user_id = models.CharField(db_column='User_ID', max_length=15, blank=True, null=True)  # Field name made lowercase.
    date_modification = models.DateTimeField(db_column='Date_Modification', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tab_Classification_Charge'


class TabClient(models.Model):
    code_client = models.CharField(db_column='Code_Client', primary_key=True, max_length=20)  # Field name made lowercase.
    type_client = models.SmallIntegerField(db_column='Type_Client', blank=True, null=True)  # Field name made lowercase.
    est_client_cosider = models.BooleanField(db_column='Est_Client_Cosider', blank=True, null=True)  # Field name made lowercase.
    libelle_client = models.CharField(db_column='Libelle_Client', max_length=300, blank=True, null=True)  # Field name made lowercase.
    nif = models.CharField(db_column='NIF', unique=True, max_length=50, blank=True, null=True)  # Field name made lowercase.
    raison_social = models.CharField(db_column='Raison_Social', max_length=50, blank=True, null=True)  # Field name made lowercase.
    num_registre_commerce = models.CharField(db_column='Num_Registre_Commerce', max_length=20, blank=True, null=True)  # Field name made lowercase.
    est_bloquer = models.BooleanField(db_column='Est_Bloquer', blank=True, null=True)  # Field name made lowercase.
    user_id = models.CharField(db_column='User_ID', max_length=15, blank=True, null=True)  # Field name made lowercase.
    date_modification = models.DateTimeField(db_column='Date_Modification', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tab_Client'


class TabCommune(models.Model):
    code_commune_ons = models.CharField(db_column='Code_Commune_Ons', primary_key=True, max_length=10)  # Field name made lowercase.
    code_commune_id = models.CharField(db_column='Code_Commune_ID', unique=True, max_length=10, blank=True, null=True)  # Field name made lowercase.
    code_postal = models.CharField(db_column='Code_Postal', unique=True, max_length=10, blank=True, null=True)  # Field name made lowercase.
    code_wilaya = models.ForeignKey('TabWilaya', models.DO_NOTHING, db_column='Code_Wilaya')  # Field name made lowercase.
    libelle_commune = models.CharField(db_column='Libelle_Commune', max_length=50, blank=True, null=True)  # Field name made lowercase.
    est_bloquer = models.BooleanField(db_column='Est_Bloquer', blank=True, null=True)  # Field name made lowercase.
    user_id = models.CharField(db_column='User_ID', max_length=15, blank=True, null=True)  # Field name made lowercase.
    date_modification = models.DateTimeField(db_column='Date_Modification', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tab_Commune'


class TabCompetences(models.Model):
    code_competence = models.CharField(db_column='Code_Competence', primary_key=True, max_length=15)  # Field name made lowercase.
    code_domaine_competence = models.ForeignKey('TabDomaineCompetences', models.DO_NOTHING, db_column='Code_Domaine_Competence')  # Field name made lowercase.
    code_qualification = models.ForeignKey('TabQualification', models.DO_NOTHING, db_column='Code_Qualification')  # Field name made lowercase.
    libelle_competence = models.CharField(db_column='Libelle_Competence', max_length=50, blank=True, null=True)  # Field name made lowercase.
    est_bloquer = models.BooleanField(db_column='Est_Bloquer', blank=True, null=True)  # Field name made lowercase.
    user_id = models.CharField(db_column='User_ID', max_length=15, blank=True, null=True)  # Field name made lowercase.
    date_modification = models.DateTimeField(db_column='Date_Modification', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tab_Competences'


class TabConstantesParametrables(models.Model):
    code_parametre = models.CharField(db_column='Code_Parametre', primary_key=True, max_length=10)  # Field name made lowercase.
    libelle_parametre = models.CharField(db_column='Libelle_Parametre', max_length=30)  # Field name made lowercase.
    descreption_parametre = models.TextField(db_column='Descreption_Parametre')  # Field name made lowercase. This field type is a guess.
    contenue_parametre = models.CharField(db_column='Contenue_Parametre', max_length=250)  # Field name made lowercase.
    est_bloquer = models.BooleanField(db_column='Est_Bloquer', blank=True, null=True)  # Field name made lowercase.
    user_id = models.CharField(db_column='User_ID', max_length=15, blank=True, null=True)  # Field name made lowercase.
    date_modification = models.DateTimeField(db_column='Date_Modification', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tab_Constantes_Parametrables'


class TabConsultant(models.Model):
    id_consultant = models.AutoField(db_column='ID_Consultant', primary_key=True)  # Field name made lowercase.
    mot_passe = models.CharField(db_column='Mot_Passe', max_length=100)  # Field name made lowercase.
    nom_prenom = models.CharField(db_column='Nom_Prenom', max_length=60, blank=True, null=True)  # Field name made lowercase.
    login_consultant = models.CharField(db_column='Login_Consultant', unique=True, max_length=30)  # Field name made lowercase.
    est_bloquer = models.BooleanField(db_column='Est_Bloquer', blank=True, null=True)  # Field name made lowercase.
    user_creator = models.CharField(db_column='User_Creator', max_length=15, blank=True, null=True)  # Field name made lowercase.
    date_modification = models.DateTimeField(db_column='Date_Modification', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tab_Consultant'


class TabCoordonnees(models.Model):
    id_coordonnee = models.AutoField(db_column='Id_Coordonnee', primary_key=True)  # Field name made lowercase.
    code_famille_coordonnee = models.ForeignKey('TabFamilleCoordonnees', models.DO_NOTHING, db_column='Code_Famille_Coordonnee')  # Field name made lowercase.
    contenue = models.CharField(db_column='Contenue', max_length=250, blank=True, null=True)  # Field name made lowercase.
    matricule = models.CharField(db_column='Matricule', max_length=15, blank=True, null=True)  # Field name made lowercase.
    code_agence = models.CharField(db_column='Code_Agence', max_length=15, blank=True, null=True)  # Field name made lowercase.
    code_entreprise = models.CharField(db_column='Code_Entreprise', max_length=2, blank=True, null=True)  # Field name made lowercase.
    code_filiale = models.CharField(db_column='Code_Filiale', max_length=5, blank=True, null=True)  # Field name made lowercase.
    code_site = models.CharField(db_column='Code_site', max_length=10, blank=True, null=True)  # Field name made lowercase.
    code_banque = models.CharField(db_column='Code_Banque', max_length=15, blank=True, null=True)  # Field name made lowercase.
    code_caisse = models.CharField(db_column='Code_Caisse', max_length=5, blank=True, null=True)  # Field name made lowercase.
    code_organisme = models.CharField(db_column='Code_Organisme', max_length=10, blank=True, null=True)  # Field name made lowercase.
    code_tiers = models.CharField(db_column='Code_Tiers', max_length=15, blank=True, null=True)  # Field name made lowercase.
    nature = models.IntegerField(db_column='Nature', blank=True, null=True)  # Field name made lowercase.
    occ = models.SmallIntegerField(db_column='Occ', blank=True, null=True)  # Field name made lowercase.
    est_bloquer = models.BooleanField(db_column='Est_Bloquer', blank=True, null=True)  # Field name made lowercase.
    user_id = models.CharField(db_column='User_ID', max_length=15, blank=True, null=True)  # Field name made lowercase.
    date_modification = models.DateTimeField(db_column='Date_Modification', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tab_Coordonnees'
        unique_together = (('code_famille_coordonnee', 'matricule', 'code_agence', 'code_entreprise', 'code_filiale', 'code_site', 'code_banque', 'code_caisse', 'code_organisme', 'code_tiers', 'nature', 'occ', 'est_bloquer'),)


class TabCriteresEvaluationFormations(models.Model):
    code_criteres_evaluation_formation = models.CharField(db_column='Code_Criteres_Evaluation_Formation', primary_key=True, max_length=15)  # Field name made lowercase.
    libelle_criteres_evaluation_formation = models.CharField(db_column='Libelle_Criteres_Evaluation_Formation', max_length=50, blank=True, null=True)  # Field name made lowercase.
    taux_evaluation_max = models.IntegerField(db_column='Taux_Evaluation_Max', blank=True, null=True)  # Field name made lowercase.
    est_bloquer = models.BooleanField(db_column='Est_Bloquer', blank=True, null=True)  # Field name made lowercase.
    user_id = models.CharField(db_column='User_ID', max_length=15, blank=True, null=True)  # Field name made lowercase.
    date_modification = models.DateTimeField(db_column='Date_Modification', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tab_Criteres_Evaluation_Formations'


class TabDecisions(models.Model):
    code_decision = models.CharField(db_column='Code_Decision', primary_key=True, max_length=18)  # Field name made lowercase.
    ref_decision = models.CharField(db_column='Ref_Decision', max_length=35, blank=True, null=True)  # Field name made lowercase.
    matricule = models.ForeignKey(TabAgent, models.DO_NOTHING, db_column='Matricule', blank=True, null=True)  # Field name made lowercase.
    date_decision = models.DateField(db_column='Date_Decision', blank=True, null=True)  # Field name made lowercase.
    code_structure_emettrice_doc = models.ForeignKey('TabStructures', models.DO_NOTHING, db_column='Code_Structure_Emettrice_Doc', blank=True, null=True)  # Field name made lowercase.
    matricule_responsable_legalisation = models.ForeignKey(TabAgent, models.DO_NOTHING, db_column='Matricule_Responsable_Legalisation', related_name='tabdecisions_matricule_responsable_legalisation_set', blank=True, null=True)  # Field name made lowercase.
    est_bloquer = models.BooleanField(db_column='Est_Bloquer', blank=True, null=True)  # Field name made lowercase.
    user_id = models.CharField(db_column='User_ID', max_length=15, blank=True, null=True)  # Field name made lowercase.
    date_modification = models.DateTimeField(db_column='Date_Modification', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tab_Decisions'


class TabDetailleCharge(models.Model):
    id_detaille_charge = models.AutoField(db_column='ID_Detaille_Charge', primary_key=True)  # Field name made lowercase.
    code_filiale = models.CharField(db_column='Code_Filiale', max_length=5, blank=True, null=True)  # Field name made lowercase.
    code_site = models.ForeignKey('TabStructureMateriaux', models.DO_NOTHING, db_column='Code_site', to_field='Code_Structure')  # Field name made lowercase.
    nt = models.ForeignKey('TabNtCharges', models.DO_NOTHING, db_column='NT', to_field='NT', blank=True, null=True)  # Field name made lowercase.
    code_structure = models.ForeignKey('TabStructureMateriaux', models.DO_NOTHING, db_column='Code_Structure', to_field='Code_Structure', related_name='tabdetaillecharge_code_structure_set', blank=True, null=True)  # Field name made lowercase.
    code_charge = models.ForeignKey('TabStructureMateriaux', models.DO_NOTHING, db_column='Code_Charge', to_field='Code_Structure', related_name='tabdetaillecharge_code_charge_set', blank=True, null=True)  # Field name made lowercase.
    code_type_charge = models.ForeignKey('TabTypeCharge', models.DO_NOTHING, db_column='Code_Type_Charge', blank=True, null=True)  # Field name made lowercase.
    code_nature_charge = models.ForeignKey('TabNatureCharge', models.DO_NOTHING, db_column='Code_Nature_Charge', blank=True, null=True)  # Field name made lowercase.
    code_classification_charge = models.ForeignKey(TabClassificationCharge, models.DO_NOTHING, db_column='Code_Classification_Charge', blank=True, null=True)  # Field name made lowercase.
    type_location = models.SmallIntegerField(db_column='Type_Location', blank=True, null=True)  # Field name made lowercase.
    code_unite_mesure = models.ForeignKey('TabUniteDeMesure', models.DO_NOTHING, db_column='Code_Unite_Mesure', blank=True, null=True)  # Field name made lowercase.
    code_groupeactivite = models.ForeignKey(TabActiviteTaches, models.DO_NOTHING, db_column='Code_GroupeActivite', to_field='NT', blank=True, null=True)  # Field name made lowercase.
    code_activite = models.ForeignKey(TabActiviteTaches, models.DO_NOTHING, db_column='Code_Activite', to_field='NT', related_name='tabdetaillecharge_code_activite_set', blank=True, null=True)  # Field name made lowercase.
    code_tache = models.ForeignKey(TabActiviteTaches, models.DO_NOTHING, db_column='Code_Tache', to_field='NT', related_name='tabdetaillecharge_code_tache_set', blank=True, null=True)  # Field name made lowercase.
    type_prestation = models.SmallIntegerField(db_column='Type_Prestation', blank=True, null=True)  # Field name made lowercase.
    recepteur = models.CharField(db_column='Recepteur', max_length=20, blank=True, null=True)  # Field name made lowercase.
    quantite = models.FloatField(db_column='Quantite', blank=True, null=True)  # Field name made lowercase.
    valeur = models.DecimalField(db_column='Valeur', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    prevu_realiser = models.CharField(db_column='Prevu_Realiser', max_length=1, blank=True, null=True)  # Field name made lowercase.
    mmaa = models.DateField(db_column='Mmaa')  # Field name made lowercase.
    est_cloturer = models.BooleanField(db_column='Est_Cloturer', blank=True, null=True)  # Field name made lowercase.
    user_id = models.CharField(db_column='User_ID', max_length=15, blank=True, null=True)  # Field name made lowercase.
    date_modification = models.DateTimeField(db_column='Date_Modification', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tab_Detaille_Charge'


class TabDetailleVentilationQuantite(models.Model):
    code_site = models.OneToOneField('TabSortieMagasinVesrsNt', models.DO_NOTHING, db_column='Code_site', primary_key=True)  # Field name made lowercase. The composite primary key (Code_site, NT, Code_Charge, Code_Charge, Code_Activite, Mmaa) found, that is not supported. The first column is selected.
    nt = models.ForeignKey('TabSortieMagasinVesrsNt', models.DO_NOTHING, db_column='NT', to_field='NT', related_name='tabdetailleventilationquantite_nt_set')  # Field name made lowercase.
    code_charge = models.ForeignKey('TabSortieMagasinVesrsNt', models.DO_NOTHING, db_column='Code_Charge', to_field='NT', related_name='tabdetailleventilationquantite_code_charge_set')  # Field name made lowercase.
    code_activite = models.ForeignKey('TabMateriauxActivite', models.DO_NOTHING, db_column='Code_Activite')  # Field name made lowercase.
    mmaa = models.ForeignKey('TabSortieMagasinVesrsNt', models.DO_NOTHING, db_column='Mmaa', to_field='NT', related_name='tabdetailleventilationquantite_mmaa_set')  # Field name made lowercase.
    quantite = models.FloatField(db_column='Quantite', blank=True, null=True)  # Field name made lowercase.
    est_cloturer = models.BooleanField(db_column='Est_Cloturer', blank=True, null=True)  # Field name made lowercase.
    user_id = models.CharField(db_column='User_ID', max_length=15, blank=True, null=True)  # Field name made lowercase.
    date_modification = models.DateTimeField(db_column='Date_Modification', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tab_Detaille_Ventilation_Quantite'
        unique_together = (('code_site', 'nt', 'code_charge', 'code_charge', 'code_activite', 'mmaa'),)


class TabDiplome(models.Model):
    code_diplome = models.CharField(db_column='Code_diplome', primary_key=True, max_length=10)  # Field name made lowercase.
    libelle_diplome = models.CharField(db_column='Libelle_Diplome', max_length=50, blank=True, null=True)  # Field name made lowercase.
    acronyme = models.CharField(db_column='Acronyme', max_length=20, blank=True, null=True)  # Field name made lowercase.
    code_niveau_etudes = models.ForeignKey('TabNiveauEtudes', models.DO_NOTHING, db_column='Code_Niveau_Etudes', blank=True, null=True)  # Field name made lowercase.
    est_bloquer = models.BooleanField(db_column='Est_Bloquer', blank=True, null=True)  # Field name made lowercase.
    user_id = models.CharField(db_column='User_ID', max_length=15, blank=True, null=True)  # Field name made lowercase.
    date_modification = models.DateTimeField(db_column='Date_Modification', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tab_Diplome'


class TabDirecteurProjet(models.Model):
    matricule = models.OneToOneField(TabAgent, models.DO_NOTHING, db_column='Matricule', primary_key=True)  # Field name made lowercase. The composite primary key (Matricule, Code_site, Date_Nomination) found, that is not supported. The first column is selected.
    code_poste_travail = models.ForeignKey('TabPosteTravail', models.DO_NOTHING, db_column='Code_Poste_Travail')  # Field name made lowercase.
    code_site = models.ForeignKey('TabSite', models.DO_NOTHING, db_column='Code_site')  # Field name made lowercase.
    reference = models.CharField(db_column='Reference', max_length=30, blank=True, null=True)  # Field name made lowercase.
    date_nomination = models.DateField(db_column='Date_Nomination')  # Field name made lowercase.
    date_fin_nomination = models.DateField(db_column='Date_Fin_Nomination', blank=True, null=True)  # Field name made lowercase.
    est_cloturer = models.BooleanField(db_column='Est_Cloturer', blank=True, null=True)  # Field name made lowercase.
    user_id = models.CharField(db_column='User_ID', max_length=15, blank=True, null=True)  # Field name made lowercase.
    date_modification = models.DateTimeField(db_column='Date_Modification', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tab_Directeur_Projet'
        unique_together = (('matricule', 'code_site', 'date_nomination'),)


class TabDivision(models.Model):
    code_division = models.CharField(db_column='Code_Division', primary_key=True, max_length=15)  # Field name made lowercase.
    code_filiale = models.ForeignKey('TabFiliale', models.DO_NOTHING, db_column='Code_Filiale', blank=True, null=True)  # Field name made lowercase.
    libelle_division = models.CharField(db_column='Libelle_Division', max_length=100, blank=True, null=True)  # Field name made lowercase.
    est_bloquer = models.BooleanField(db_column='Est_Bloquer', blank=True, null=True)  # Field name made lowercase.
    user_id = models.CharField(db_column='User_ID', max_length=15, blank=True, null=True)  # Field name made lowercase.
    date_modification = models.DateTimeField(db_column='Date_Modification', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tab_Division'


class TabDocumentWord(models.Model):
    id_document = models.AutoField(db_column='ID_Document', primary_key=True)  # Field name made lowercase.
    nom_document = models.CharField(db_column='Nom_Document', unique=True, max_length=100, blank=True, null=True)  # Field name made lowercase.
    requete_sql = models.TextField(db_column='Requete_Sql', blank=True, null=True)  # Field name made lowercase.
    chemin = models.CharField(db_column='Chemin', max_length=200, blank=True, null=True)  # Field name made lowercase.
    date_modification = models.DateTimeField(db_column='Date_Modification', blank=True, null=True)  # Field name made lowercase.
    user_id = models.CharField(db_column='User_ID', max_length=15, blank=True, null=True)  # Field name made lowercase.
    document_pour = models.IntegerField(db_column='Document_Pour', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tab_Document_Word'


class TabDomaine(models.Model):
    code_domaine = models.CharField(db_column='Code_Domaine', primary_key=True, max_length=15)  # Field name made lowercase.
    libelle_domaine = models.CharField(db_column='Libelle_Domaine', max_length=50, blank=True, null=True)  # Field name made lowercase.
    acronyme = models.CharField(db_column='Acronyme', max_length=20, blank=True, null=True)  # Field name made lowercase.
    est_bloquer = models.BooleanField(db_column='Est_Bloquer', blank=True, null=True)  # Field name made lowercase.
    user_id = models.CharField(db_column='User_ID', max_length=15, blank=True, null=True)  # Field name made lowercase.
    date_modification = models.DateTimeField(db_column='Date_Modification', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tab_Domaine'


class TabDomaineCompetences(models.Model):
    code_domaine_competence = models.CharField(db_column='Code_Domaine_Competence', primary_key=True, max_length=15)  # Field name made lowercase.
    code_domaine = models.ForeignKey(TabDomaine, models.DO_NOTHING, db_column='Code_Domaine')  # Field name made lowercase.
    libelle_domaine_competence = models.CharField(db_column='Libelle_Domaine_Competence', max_length=50, blank=True, null=True)  # Field name made lowercase.
    est_bloquer = models.BooleanField(db_column='Est_Bloquer', blank=True, null=True)  # Field name made lowercase.
    user_id = models.CharField(db_column='User_ID', max_length=15, blank=True, null=True)  # Field name made lowercase.
    date_modification = models.DateTimeField(db_column='Date_Modification', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tab_Domaine_Competences'


class TabDqeTemp(models.Model):
    code_site = models.CharField(db_column='Code_site', primary_key=True, max_length=10)  # Field name made lowercase. The composite primary key (Code_site, NT, Code_Tache) found, that is not supported. The first column is selected.
    nt = models.CharField(db_column='NT', max_length=20)  # Field name made lowercase.
    code_tache = models.CharField(db_column='Code_Tache', max_length=30)  # Field name made lowercase.
    libelle_tache = models.TextField(db_column='Libelle_Tache', blank=True, null=True)  # Field name made lowercase.
    code_unite_mesure = models.CharField(db_column='Code_Unite_Mesure', max_length=4, blank=True, null=True)  # Field name made lowercase.
    est_tache_composite = models.BooleanField(db_column='Est_Tache_Composite', blank=True, null=True)  # Field name made lowercase.
    est_tache_complementaire = models.BooleanField(db_column='Est_Tache_Complementaire', blank=True, null=True)  # Field name made lowercase.
    quantite = models.FloatField(db_column='Quantite', blank=True, null=True)  # Field name made lowercase.
    prix_unitaire = models.DecimalField(db_column='Prix_Unitaire', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    est_bloquer = models.BooleanField(db_column='Est_Bloquer', blank=True, null=True)  # Field name made lowercase.
    user_id = models.CharField(db_column='User_ID', max_length=15, blank=True, null=True)  # Field name made lowercase.
    date_modification = models.DateTimeField(db_column='Date_Modification', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tab_Dqe_Temp'
        unique_together = (('code_site', 'nt', 'code_tache'),)


class TabDroitRubriquesAgent(models.Model):
    id_droit_rubrique_agent = models.AutoField(db_column='ID_Droit_Rubrique_Agent', primary_key=True)  # Field name made lowercase.
    matricule = models.ForeignKey(TabAgent, models.DO_NOTHING, db_column='Matricule')  # Field name made lowercase.
    code_rubrique = models.ForeignKey('TabPlanRubriques', models.DO_NOTHING, db_column='Code_Rubrique')  # Field name made lowercase.
    code_decision = models.CharField(db_column='Code_Decision', max_length=18, blank=True, null=True)  # Field name made lowercase.
    code_decision_suppression = models.CharField(db_column='Code_Decision_Suppression', max_length=18, blank=True, null=True)  # Field name made lowercase.
    est_bloquer = models.BooleanField(db_column='Est_Bloquer', blank=True, null=True)  # Field name made lowercase.
    user_id = models.CharField(db_column='User_ID', max_length=15, blank=True, null=True)  # Field name made lowercase.
    date_modification = models.DateTimeField(db_column='Date_Modification', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tab_Droit_Rubriques_Agent'


class TabEntreprise(models.Model):
    code_entreprise = models.CharField(db_column='Code_Entreprise', primary_key=True, max_length=2)  # Field name made lowercase.
    raison_social = models.CharField(db_column='Raison_Social', max_length=50, blank=True, null=True)  # Field name made lowercase.
    num_fiscal = models.CharField(db_column='Num_Fiscal', max_length=20, blank=True, null=True)  # Field name made lowercase.
    num_article = models.CharField(db_column='Num_Article', max_length=20, blank=True, null=True)  # Field name made lowercase.
    num_registre_commerce = models.CharField(db_column='Num_Registre_Commerce', max_length=20, blank=True, null=True)  # Field name made lowercase.
    num_compte = models.CharField(db_column='Num_Compte', max_length=20, blank=True, null=True)  # Field name made lowercase.
    capital = models.DecimalField(db_column='Capital', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    entete = models.TextField(db_column='Entete', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    date_registre_commerce = models.DateField(db_column='Date_Registre_Commerce', blank=True, null=True)  # Field name made lowercase.
    logo = models.BinaryField(db_column='Logo', blank=True, null=True)  # Field name made lowercase.
    type_dossier = models.SmallIntegerField(db_column='Type_Dossier')  # Field name made lowercase.
    est_bloquer = models.BooleanField(db_column='Est_Bloquer', blank=True, null=True)  # Field name made lowercase.
    user_id = models.CharField(db_column='User_ID', max_length=15, blank=True, null=True)  # Field name made lowercase.
    date_modification = models.DateTimeField(db_column='Date_Modification', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tab_Entreprise'


class TabEvaluationAgentFormation(models.Model):
    id_evaluation_agent_formation = models.AutoField(db_column='ID_Evaluation_Agent_Formation', primary_key=True)  # Field name made lowercase.
    code_agent_formation = models.ForeignKey(TabAgentFormation, models.DO_NOTHING, db_column='Code_Agent_Formation', to_field='Code_Agent_Formation', blank=True, null=True)  # Field name made lowercase.
    code_objectifs_formation = models.ForeignKey('TabObjectifsFormation', models.DO_NOTHING, db_column='Code_Objectifs_Formation', to_field='Code_Objectifs_Formation', blank=True, null=True)  # Field name made lowercase.
    taux_evaluation = models.IntegerField(db_column='Taux_Evaluation', blank=True, null=True)  # Field name made lowercase.
    est_bloquer = models.BooleanField(db_column='Est_Bloquer', blank=True, null=True)  # Field name made lowercase.
    user_id = models.CharField(db_column='User_ID', max_length=15, blank=True, null=True)  # Field name made lowercase.
    date_modification = models.DateTimeField(db_column='Date_Modification', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tab_Evaluation_Agent_Formation'
        unique_together = (('code_agent_formation', 'code_objectifs_formation'),)


class TabEvenementAgent(models.Model):
    code_evenement_agent = models.CharField(db_column='Code_Evenement_Agent', primary_key=True, max_length=18)  # Field name made lowercase.
    matricule = models.ForeignKey(TabAgent, models.DO_NOTHING, db_column='Matricule')  # Field name made lowercase.
    code_evenement = models.ForeignKey('TabEvenementRh', models.DO_NOTHING, db_column='Code_Evenement')  # Field name made lowercase.
    date_evenement = models.DateField(db_column='Date_Evenement', blank=True, null=True)  # Field name made lowercase.
    motif_evenement = models.CharField(db_column='Motif_Evenement', max_length=200, blank=True, null=True)  # Field name made lowercase.
    avec_blocage_paie = models.BooleanField(db_column='Avec_Blocage_Paie', blank=True, null=True)  # Field name made lowercase.
    avec_deblocage_provisoire_paie = models.BooleanField(db_column='Avec_Deblocage_Provisoire_Paie', blank=True, null=True)  # Field name made lowercase.
    date_retour_reel = models.DateField(db_column='Date_Retour_Reel', blank=True, null=True)  # Field name made lowercase.
    date_fin_evenement_prevu = models.DateField(db_column='Date_Fin_Evenement_Prevu', blank=True, null=True)  # Field name made lowercase.
    nbr_heures = models.FloatField(db_column='Nbr_Heures', blank=True, null=True)  # Field name made lowercase.
    nbr_jours = models.IntegerField(db_column='Nbr_Jours', blank=True, null=True)  # Field name made lowercase.
    est_archiver = models.BooleanField(db_column='Est_Archiver', blank=True, null=True)  # Field name made lowercase.
    est_correction_evenement = models.BooleanField(db_column='Est_Correction_Evenement', blank=True, null=True)  # Field name made lowercase.
    code_parent = models.ForeignKey('self', models.DO_NOTHING, db_column='Code_Parent', blank=True, null=True)  # Field name made lowercase.
    code_decision = models.CharField(db_column='Code_Decision', max_length=18, blank=True, null=True)  # Field name made lowercase.
    est_bloquer = models.BooleanField(db_column='Est_Bloquer', blank=True, null=True)  # Field name made lowercase.
    user_id = models.CharField(db_column='User_ID', max_length=15, blank=True, null=True)  # Field name made lowercase.
    date_modification = models.DateTimeField(db_column='Date_Modification', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tab_Evenement_Agent'


class TabEvenementRh(models.Model):
    code_evenement = models.CharField(db_column='Code_Evenement', primary_key=True, max_length=10)  # Field name made lowercase.
    code_type_evenement = models.ForeignKey('TabTypeEvenementRh', models.DO_NOTHING, db_column='Code_Type_Evenement')  # Field name made lowercase.
    libelle_evenement = models.CharField(db_column='Libelle_Evenement', max_length=30, blank=True, null=True)  # Field name made lowercase.
    avec_reintegration = models.BooleanField(db_column='Avec_Reintegration', blank=True, null=True)  # Field name made lowercase.
    avec_retour = models.BooleanField(db_column='Avec_Retour', blank=True, null=True)  # Field name made lowercase.
    avec_depart = models.BooleanField(db_column='Avec_Depart', blank=True, null=True)  # Field name made lowercase.
    type_changement = models.SmallIntegerField(db_column='Type_Changement', blank=True, null=True)  # Field name made lowercase.
    impacte_paie = models.BooleanField(db_column='Impacte_Paie', blank=True, null=True)  # Field name made lowercase.
    type_blocage_paie = models.SmallIntegerField(db_column='Type_Blocage_Paie', blank=True, null=True)  # Field name made lowercase.
    avec_decision = models.BooleanField(db_column='Avec_Decision', blank=True, null=True)  # Field name made lowercase.
    type_horaire = models.IntegerField(db_column='Type_Horaire', blank=True, null=True)  # Field name made lowercase.
    inclu_week_end = models.BooleanField(db_column='Inclu_Week_End', blank=True, null=True)  # Field name made lowercase.
    inclu_jour_ferier = models.BooleanField(db_column='Inclu_Jour_Ferier', blank=True, null=True)  # Field name made lowercase.
    est_bloquer = models.BooleanField(db_column='Est_Bloquer', blank=True, null=True)  # Field name made lowercase.
    user_id = models.CharField(db_column='User_ID', max_length=15, blank=True, null=True)  # Field name made lowercase.
    date_modification = models.DateTimeField(db_column='Date_Modification', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tab_Evenement_RH'


class TabFamilleCoordonnees(models.Model):
    code_famille_coordonnee = models.CharField(db_column='Code_Famille_Coordonnee', primary_key=True, max_length=5)  # Field name made lowercase.
    libelle_type_coordonnee = models.CharField(db_column='Libelle_Type_Coordonnee', max_length=30, blank=True, null=True)  # Field name made lowercase.
    type_cordonnee = models.SmallIntegerField(db_column='Type_Cordonnee')  # Field name made lowercase.
    avec_commune = models.BooleanField(db_column='Avec_Commune', blank=True, null=True)  # Field name made lowercase.
    est_numerique = models.BooleanField(db_column='Est_Numerique', blank=True, null=True)  # Field name made lowercase.
    est_alphabetique = models.BooleanField(db_column='Est_Alphabetique', blank=True, null=True)  # Field name made lowercase.
    est_alphanumerique = models.BooleanField(db_column='Est_AlphaNumerique', blank=True, null=True)  # Field name made lowercase.
    est_bloquer = models.BooleanField(db_column='Est_Bloquer', blank=True, null=True)  # Field name made lowercase.
    user_id = models.CharField(db_column='User_ID', max_length=15, blank=True, null=True)  # Field name made lowercase.
    date_modification = models.DateTimeField(db_column='Date_Modification', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tab_Famille_Coordonnees'


class TabFamillePosteTravail(models.Model):
    code_famille_poste_travail = models.CharField(db_column='Code_Famille_Poste_Travail', primary_key=True, max_length=10)  # Field name made lowercase.
    libelle_famille_poste_travail = models.CharField(db_column='Libelle_Famille_Poste_Travail', max_length=50, blank=True, null=True)  # Field name made lowercase.
    acronyme = models.CharField(db_column='Acronyme', max_length=20, blank=True, null=True)  # Field name made lowercase.
    est_bloquer = models.BooleanField(db_column='Est_Bloquer', blank=True, null=True)  # Field name made lowercase.
    user_id = models.CharField(db_column='User_ID', max_length=15, blank=True, null=True)  # Field name made lowercase.
    date_modification = models.DateTimeField(db_column='Date_Modification', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tab_Famille_Poste_Travail'


class TabFamilleStructures(models.Model):
    code_famille_structure = models.CharField(db_column='Code_Famille_Structure', primary_key=True, max_length=5)  # Field name made lowercase.
    libelle_famille_structure = models.CharField(db_column='Libelle_Famille_Structure', max_length=50, blank=True, null=True)  # Field name made lowercase.
    numero_ordre = models.SmallIntegerField(db_column='Numero_Ordre', blank=True, null=True)  # Field name made lowercase.
    est_bloquer = models.BooleanField(db_column='Est_Bloquer', blank=True, null=True)  # Field name made lowercase.
    user_id = models.CharField(db_column='User_ID', max_length=15, blank=True, null=True)  # Field name made lowercase.
    date_modification = models.DateTimeField(db_column='Date_Modification', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tab_Famille_Structures'


class TabFamillesFonctions(models.Model):
    code_famille_fonction = models.CharField(db_column='Code_Famille_Fonction', primary_key=True, max_length=5)  # Field name made lowercase.
    libelle_famille_fonction = models.CharField(db_column='Libelle_Famille_Fonction', max_length=50, blank=True, null=True)  # Field name made lowercase.
    code_module = models.ForeignKey('TabModules', models.DO_NOTHING, db_column='Code_Module')  # Field name made lowercase.
    est_bloquer = models.BooleanField(db_column='Est_Bloquer', blank=True, null=True)  # Field name made lowercase.
    user_id = models.CharField(db_column='User_ID', max_length=15, blank=True, null=True)  # Field name made lowercase.
    date_modification = models.DateTimeField(db_column='Date_Modification', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tab_Familles_Fonctions'


class TabFiliale(models.Model):
    code_filiale = models.CharField(db_column='Code_Filiale', primary_key=True, max_length=5)  # Field name made lowercase.
    code_entreprise = models.ForeignKey(TabEntreprise, models.DO_NOTHING, db_column='Code_Entreprise')  # Field name made lowercase.
    libelle_filiale = models.CharField(db_column='Libelle_Filiale', max_length=50, blank=True, null=True)  # Field name made lowercase.
    est_bloquer = models.BooleanField(db_column='Est_Bloquer', blank=True, null=True)  # Field name made lowercase.
    user_id = models.CharField(db_column='User_ID', max_length=15, blank=True, null=True)  # Field name made lowercase.
    date_modification = models.DateTimeField(db_column='Date_Modification', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tab_Filiale'


class TabFonctionsInterface(models.Model):
    code_fonction = models.CharField(db_column='Code_Fonction', primary_key=True, max_length=5)  # Field name made lowercase.
    code_famille_fonction = models.ForeignKey(TabFamillesFonctions, models.DO_NOTHING, db_column='Code_Famille_Fonction', blank=True, null=True)  # Field name made lowercase.
    libelle_fonction = models.CharField(db_column='Libelle_Fonction', max_length=50, blank=True, null=True)  # Field name made lowercase.
    activation = models.CharField(db_column='Activation', max_length=5, blank=True, null=True)  # Field name made lowercase.
    description = models.TextField(db_column='Description', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    est_bloquer = models.BooleanField(db_column='Est_Bloquer', blank=True, null=True)  # Field name made lowercase.
    user_id = models.CharField(db_column='User_ID', max_length=15, blank=True, null=True)  # Field name made lowercase.
    date_modification = models.DateTimeField(db_column='Date_Modification', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tab_Fonctions_Interface'


class TabFonctionsInterfaceUsers(models.Model):
    code_fonction = models.OneToOneField(TabFonctionsInterface, models.DO_NOTHING, db_column='Code_Fonction', primary_key=True)  # Field name made lowercase. The composite primary key (Code_Fonction, Code_Profil_User) found, that is not supported. The first column is selected.
    code_profil_user = models.ForeignKey('TabProfilsUsers', models.DO_NOTHING, db_column='Code_Profil_User')  # Field name made lowercase.
    est_bloquer = models.BooleanField(db_column='Est_Bloquer', blank=True, null=True)  # Field name made lowercase.
    user_id = models.CharField(db_column='User_ID', max_length=15, blank=True, null=True)  # Field name made lowercase.
    date_modification = models.DateTimeField(db_column='Date_Modification', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tab_Fonctions_Interface_Users'
        unique_together = (('code_fonction', 'code_profil_user'),)


class TabFormationCompetence(models.Model):
    code_competence = models.ForeignKey(TabCompetences, models.DO_NOTHING, db_column='Code_Competence')  # Field name made lowercase.
    code_formation = models.OneToOneField('TabFormations', models.DO_NOTHING, db_column='Code_Formation', primary_key=True)  # Field name made lowercase. The composite primary key (Code_Formation, Code_Competence) found, that is not supported. The first column is selected.
    niveau_competence = models.SmallIntegerField(db_column='Niveau_Competence', blank=True, null=True)  # Field name made lowercase.
    est_bloquer = models.BooleanField(db_column='Est_Bloquer', blank=True, null=True)  # Field name made lowercase.
    user_id = models.CharField(db_column='User_ID', max_length=15, blank=True, null=True)  # Field name made lowercase.
    date_modification = models.DateTimeField(db_column='Date_Modification', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tab_Formation_Competence'
        unique_together = (('code_formation', 'code_competence'),)


class TabFormationEvaluation(models.Model):
    id_formation_evaluation = models.AutoField(db_column='ID_Formation_Evaluation', primary_key=True)  # Field name made lowercase.
    code_formation = models.ForeignKey('TabFormations', models.DO_NOTHING, db_column='Code_Formation')  # Field name made lowercase.
    code_criteres_evaluation_formation = models.ForeignKey(TabCriteresEvaluationFormations, models.DO_NOTHING, db_column='Code_Criteres_Evaluation_Formation')  # Field name made lowercase.
    taux_evaluation = models.IntegerField(db_column='Taux_Evaluation', blank=True, null=True)  # Field name made lowercase.
    est_bloquer = models.BooleanField(db_column='Est_Bloquer', blank=True, null=True)  # Field name made lowercase.
    user_id = models.CharField(db_column='User_ID', max_length=15, blank=True, null=True)  # Field name made lowercase.
    date_modification = models.DateTimeField(db_column='Date_Modification', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tab_Formation_Evaluation'
        unique_together = (('code_formation', 'code_criteres_evaluation_formation'),)


class TabFormations(models.Model):
    code_formation = models.CharField(db_column='Code_Formation', primary_key=True, max_length=18)  # Field name made lowercase.
    code_specialite = models.ForeignKey('TabSpecialite', models.DO_NOTHING, db_column='Code_Specialite', blank=True, null=True)  # Field name made lowercase.
    code_type_formation = models.ForeignKey('TabTypeFormation', models.DO_NOTHING, db_column='Code_Type_Formation', blank=True, null=True)  # Field name made lowercase.
    code_diplome = models.ForeignKey(TabDiplome, models.DO_NOTHING, db_column='Code_diplome', blank=True, null=True)  # Field name made lowercase.
    code_mode_formation = models.ForeignKey('TabModeFormation', models.DO_NOTHING, db_column='Code_Mode_Formation', blank=True, null=True)  # Field name made lowercase.
    code_organisme = models.CharField(db_column='Code_Organisme', max_length=20, blank=True, null=True)  # Field name made lowercase.
    niveau_formation = models.SmallIntegerField(db_column='Niveau_Formation', blank=True, null=True)  # Field name made lowercase.
    libelle_formation = models.CharField(db_column='Libelle_Formation', max_length=150, blank=True, null=True)  # Field name made lowercase.
    date_debut_formation = models.DateField(db_column='Date_Debut_Formation', blank=True, null=True)  # Field name made lowercase.
    date_fin_formation = models.DateField(db_column='Date_Fin_Formation', blank=True, null=True)  # Field name made lowercase.
    nbr_jours_prevu = models.IntegerField(db_column='Nbr_Jours_Prevu', blank=True, null=True)  # Field name made lowercase.
    nbr_jour_reel = models.IntegerField(db_column='Nbr_Jour_Reel', blank=True, null=True)  # Field name made lowercase.
    etat_formation = models.SmallIntegerField(db_column='Etat_Formation', blank=True, null=True)  # Field name made lowercase.
    observation = models.TextField(db_column='Observation', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    lieu_formation = models.CharField(db_column='Lieu_Formation', max_length=50, blank=True, null=True)  # Field name made lowercase.
    nbr_heures_jour = models.IntegerField(db_column='Nbr_Heures_Jour', blank=True, null=True)  # Field name made lowercase.
    matricule_formateur_interne = models.CharField(db_column='Matricule_Formateur_Interne', max_length=15, blank=True, null=True)  # Field name made lowercase.
    type_organisme = models.SmallIntegerField(db_column='Type_Organisme', blank=True, null=True)  # Field name made lowercase.
    montant_formation = models.DecimalField(db_column='Montant_Formation', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    est_bloquer = models.BooleanField(db_column='Est_Bloquer', blank=True, null=True)  # Field name made lowercase.
    user_id = models.CharField(db_column='User_ID', max_length=15, blank=True, null=True)  # Field name made lowercase.
    date_modification = models.DateTimeField(db_column='Date_Modification', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tab_Formations'


class TabGroupeactivite(models.Model):
    code_groupeactivite = models.CharField(db_column='Code_GroupeActivite', primary_key=True, max_length=4)  # Field name made lowercase.
    libelle_groupeactivite = models.CharField(db_column='Libelle_GroupeActivite', max_length=50, blank=True, null=True)  # Field name made lowercase.
    je_l_utilise = models.BooleanField(db_column='Je_L_Utilise', blank=True, null=True)  # Field name made lowercase.
    est_bloquer = models.BooleanField(db_column='Est_Bloquer', blank=True, null=True)  # Field name made lowercase.
    user_id = models.CharField(db_column='User_ID', max_length=15, blank=True, null=True)  # Field name made lowercase.
    date_modification = models.DateTimeField(db_column='Date_Modification', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tab_GroupeActivite'


class TabGroupeactiviteActivite(models.Model):
    code_groupeactivite = models.OneToOneField(TabGroupeactivite, models.DO_NOTHING, db_column='Code_GroupeActivite', primary_key=True)  # Field name made lowercase. The composite primary key (Code_GroupeActivite, Code_Activite) found, that is not supported. The first column is selected.
    code_activite = models.ForeignKey(TabActivite, models.DO_NOTHING, db_column='Code_Activite')  # Field name made lowercase.
    est_bloquer = models.BooleanField(db_column='Est_Bloquer', blank=True, null=True)  # Field name made lowercase.
    user_id = models.CharField(db_column='User_ID', max_length=15, blank=True, null=True)  # Field name made lowercase.
    date_modification = models.DateTimeField(db_column='Date_Modification', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tab_GroupeActivite_Activite'
        unique_together = (('code_groupeactivite', 'code_activite'),)


class TabHistoriqueImpactEvenementPaie(models.Model):
    code_evenement_agent = models.OneToOneField(TabEvenementAgent, models.DO_NOTHING, db_column='Code_Evenement_Agent', primary_key=True)  # Field name made lowercase. The composite primary key (Code_Evenement_Agent, Mmaa, Code_Rubrique) found, that is not supported. The first column is selected.
    mmaa = models.DateField(db_column='Mmaa')  # Field name made lowercase.
    code_rubrique = models.ForeignKey('TabPlanRubriques', models.DO_NOTHING, db_column='Code_Rubrique')  # Field name made lowercase.
    taux_impact = models.FloatField(db_column='Taux_Impact', blank=True, null=True)  # Field name made lowercase.
    mode_saisie = models.SmallIntegerField(db_column='Mode_Saisie', blank=True, null=True)  # Field name made lowercase.
    est_bloquer = models.BooleanField(db_column='Est_Bloquer', blank=True, null=True)  # Field name made lowercase.
    user_id = models.CharField(db_column='User_ID', max_length=15, blank=True, null=True)  # Field name made lowercase.
    date_modification = models.DateTimeField(db_column='Date_Modification', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tab_Historique_Impact_Evenement_Paie'
        unique_together = (('code_evenement_agent', 'mmaa', 'code_rubrique'),)


class TabHistoriqueInformationCaisseCotisation(models.Model):
    code_caisse = models.OneToOneField(TabCaisseCotisation, models.DO_NOTHING, db_column='Code_Caisse', primary_key=True)  # Field name made lowercase. The composite primary key (Code_Caisse, Mmaa) found, that is not supported. The first column is selected.
    libelle_caisse = models.CharField(db_column='Libelle_Caisse', max_length=50, blank=True, null=True)  # Field name made lowercase.
    mmaa = models.ForeignKey('TabMoisPaieArchive', models.DO_NOTHING, db_column='Mmaa')  # Field name made lowercase.
    num_ss_employeur = models.CharField(db_column='Num_SS_Employeur', max_length=20, blank=True, null=True)  # Field name made lowercase.
    date_interval = models.DateField(db_column='Date_Interval', blank=True, null=True)  # Field name made lowercase.
    est_bloquer = models.BooleanField(db_column='Est_Bloquer', blank=True, null=True)  # Field name made lowercase.
    user_id = models.CharField(db_column='User_ID', max_length=15, blank=True, null=True)  # Field name made lowercase.
    date_modification = models.DateTimeField(db_column='Date_Modification', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tab_Historique_Information_Caisse_Cotisation'
        unique_together = (('code_caisse', 'mmaa'),)


class TabInformationBulletinAgent(models.Model):
    code_information_bulletin_agent = models.CharField(db_column='Code_Information_Bulletin_Agent', primary_key=True, max_length=18)  # Field name made lowercase.
    matricule = models.ForeignKey(TabAgent, models.DO_NOTHING, db_column='Matricule')  # Field name made lowercase.
    nom = models.CharField(db_column='Nom', max_length=30)  # Field name made lowercase.
    prenom = models.CharField(db_column='Prenom', max_length=30)  # Field name made lowercase.
    mmaa = models.DateField(db_column='Mmaa')  # Field name made lowercase.
    classification = models.ForeignKey(TabClassification, models.DO_NOTHING, db_column='Classification', blank=True, null=True)  # Field name made lowercase.
    code_poste_travail = models.ForeignKey('TabPosteTravail', models.DO_NOTHING, db_column='Code_Poste_Travail', blank=True, null=True)  # Field name made lowercase.
    code_evenement_agent = models.ForeignKey(TabEvenementAgent, models.DO_NOTHING, db_column='Code_Evenement_Agent', blank=True, null=True)  # Field name made lowercase.
    code_agence = models.ForeignKey(TabAgence, models.DO_NOTHING, db_column='Code_Agence', blank=True, null=True)  # Field name made lowercase.
    mode_paiement = models.CharField(db_column='Mode_Paiement', max_length=1, blank=True, null=True)  # Field name made lowercase.
    num_compte = models.CharField(db_column='Num_Compte', max_length=20, blank=True, null=True)  # Field name made lowercase.
    date_interval = models.DateField(db_column='Date_Interval', blank=True, null=True)  # Field name made lowercase.
    code_structure = models.ForeignKey('TabStructures', models.DO_NOTHING, db_column='Code_Structure', blank=True, null=True)  # Field name made lowercase.
    code_statut_horaire = models.ForeignKey('TabStatutHoraire', models.DO_NOTHING, db_column='Code_Statut_Horaire', blank=True, null=True)  # Field name made lowercase.
    est_archiver = models.BooleanField(db_column='Est_Archiver', blank=True, null=True)  # Field name made lowercase.
    nbr_enfant = models.SmallIntegerField(db_column='Nbr_Enfant', blank=True, null=True)  # Field name made lowercase.
    situation_famille = models.CharField(db_column='Situation_Famille', max_length=1, blank=True, null=True)  # Field name made lowercase.
    code_caisse = models.ForeignKey(TabCaisseCotisation, models.DO_NOTHING, db_column='Code_Caisse', blank=True, null=True)  # Field name made lowercase.
    est_bloquer = models.BooleanField(db_column='Est_Bloquer', blank=True, null=True)  # Field name made lowercase.
    user_id = models.CharField(db_column='User_ID', max_length=15, blank=True, null=True)  # Field name made lowercase.
    date_modification = models.DateTimeField(db_column='Date_Modification', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tab_Information_Bulletin_Agent'


class TabListeChampDocument(models.Model):
    id_champ = models.AutoField(db_column='ID_Champ', primary_key=True)  # Field name made lowercase.
    id_document = models.ForeignKey(TabDocumentWord, models.DO_NOTHING, db_column='ID_Document', blank=True, null=True)  # Field name made lowercase.
    libelle_champ = models.CharField(db_column='Libelle_Champ', max_length=70, blank=True, null=True)  # Field name made lowercase.
    est_date = models.BooleanField(db_column='Est_Date', blank=True, null=True)  # Field name made lowercase.
    date_modification = models.DateTimeField(db_column='Date_Modification', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tab_Liste_Champ_Document'


class TabListeFiliale(models.Model):
    code_filiale = models.CharField(db_column='Code_Filiale', primary_key=True, max_length=5)  # Field name made lowercase.
    libelle_filiale = models.CharField(db_column='Libelle_Filiale', max_length=50, blank=True, null=True)  # Field name made lowercase.
    est_bloquer = models.BooleanField(db_column='Est_Bloquer', blank=True, null=True)  # Field name made lowercase.
    user_id = models.CharField(db_column='User_ID', max_length=15, blank=True, null=True)  # Field name made lowercase.
    date_modification = models.DateTimeField(db_column='Date_Modification', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tab_Liste_Filiale'


class TabListePoles(models.Model):
    code_filiale = models.OneToOneField(TabListeFiliale, models.DO_NOTHING, db_column='Code_Filiale', primary_key=True)  # Field name made lowercase. The composite primary key (Code_Filiale, Code_site) found, that is not supported. The first column is selected.
    code_site = models.CharField(db_column='Code_site', max_length=10)  # Field name made lowercase.
    libelle_site = models.CharField(db_column='Libelle_Site', max_length=150, blank=True, null=True)  # Field name made lowercase.
    est_bloquer = models.BooleanField(db_column='Est_Bloquer', blank=True, null=True)  # Field name made lowercase.
    user_id = models.CharField(db_column='User_ID', max_length=15, blank=True, null=True)  # Field name made lowercase.
    date_modification = models.DateTimeField(db_column='Date_Modification', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tab_Liste_Poles'
        unique_together = (('code_filiale', 'code_site'),)


class TabMateriauxActivite(models.Model):
    code_charge = models.OneToOneField(TabCharge, models.DO_NOTHING, db_column='Code_Charge', primary_key=True)  # Field name made lowercase. The composite primary key (Code_Charge, Code_Activite) found, that is not supported. The first column is selected.
    code_activite = models.ForeignKey(TabActivite, models.DO_NOTHING, db_column='Code_Activite')  # Field name made lowercase.
    est_bloquer = models.BooleanField(db_column='Est_Bloquer', blank=True, null=True)  # Field name made lowercase.
    user_id = models.CharField(db_column='User_ID', max_length=15, blank=True, null=True)  # Field name made lowercase.
    date_modification = models.DateTimeField(db_column='Date_Modification', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tab_Materiaux_Activite'
        unique_together = (('code_charge', 'code_activite'),)


class TabModeFormation(models.Model):
    code_mode_formation = models.CharField(db_column='Code_Mode_Formation', primary_key=True, max_length=5)  # Field name made lowercase.
    libelle_mode_formation = models.CharField(db_column='Libelle_Mode_Formation', max_length=50, blank=True, null=True)  # Field name made lowercase.
    est_bloquer = models.BooleanField(db_column='Est_Bloquer', blank=True, null=True)  # Field name made lowercase.
    user_id = models.CharField(db_column='User_ID', max_length=15, blank=True, null=True)  # Field name made lowercase.
    date_modification = models.DateTimeField(db_column='Date_Modification', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tab_Mode_Formation'


class TabModules(models.Model):
    code_module = models.CharField(db_column='Code_Module', primary_key=True, max_length=5)  # Field name made lowercase.
    libelle_module = models.CharField(db_column='Libelle_Module', max_length=50)  # Field name made lowercase.
    est_bloquer = models.BooleanField(db_column='Est_Bloquer', blank=True, null=True)  # Field name made lowercase.
    user_id = models.CharField(db_column='User_ID', max_length=15, blank=True, null=True)  # Field name made lowercase.
    date_modification = models.DateTimeField(db_column='Date_Modification', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tab_Modules'


class TabModulesConstantes(models.Model):
    code_module = models.OneToOneField(TabModules, models.DO_NOTHING, db_column='Code_Module', primary_key=True)  # Field name made lowercase. The composite primary key (Code_Module, Code_Parametre) found, that is not supported. The first column is selected.
    code_parametre = models.ForeignKey(TabConstantesParametrables, models.DO_NOTHING, db_column='Code_Parametre')  # Field name made lowercase.
    est_bloquer = models.BooleanField(db_column='Est_Bloquer', blank=True, null=True)  # Field name made lowercase.
    user_id = models.CharField(db_column='User_ID', max_length=15, blank=True, null=True)  # Field name made lowercase.
    date_modification = models.DateTimeField(db_column='Date_Modification', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tab_Modules_Constantes'
        unique_together = (('code_module', 'code_parametre'),)


class TabMoisPaieArchive(models.Model):
    mmaa = models.DateField(db_column='Mmaa', primary_key=True)  # Field name made lowercase.
    est_bloquer = models.BooleanField(db_column='Est_Bloquer', blank=True, null=True)  # Field name made lowercase.
    user_id = models.CharField(db_column='User_ID', max_length=15, blank=True, null=True)  # Field name made lowercase.
    date_modification = models.DateTimeField(db_column='Date_Modification', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tab_Mois_Paie_Archive'


class TabNt(models.Model):
    code_site = models.OneToOneField('TabSite', models.DO_NOTHING, db_column='Code_site', primary_key=True)  # Field name made lowercase. The composite primary key (Code_site, NT) found, that is not supported. The first column is selected.
    nt = models.CharField(db_column='NT', max_length=20)  # Field name made lowercase.
    code_client = models.ForeignKey(TabClient, models.DO_NOTHING, db_column='Code_Client')  # Field name made lowercase.
    code_situation_nt = models.ForeignKey('TabSituationNt', models.DO_NOTHING, db_column='Code_Situation_NT', blank=True, null=True)  # Field name made lowercase.
    libelle_nt = models.TextField(db_column='Libelle_NT', blank=True, null=True)  # Field name made lowercase.
    date_ouverture_nt = models.DateField(db_column='Date_Ouverture_NT', blank=True, null=True)  # Field name made lowercase.
    date_cloture_nt = models.DateField(db_column='Date_Cloture_NT', blank=True, null=True)  # Field name made lowercase.
    est_bloquer = models.BooleanField(db_column='Est_Bloquer', blank=True, null=True)  # Field name made lowercase.
    user_id = models.CharField(db_column='User_ID', max_length=15, blank=True, null=True)  # Field name made lowercase.
    date_modification = models.DateTimeField(db_column='Date_Modification', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tab_NT'
        unique_together = (('code_site', 'nt'),)


class TabNtTaches(models.Model):
    code_site = models.OneToOneField(TabNt, models.DO_NOTHING, db_column='Code_site', primary_key=True)  # Field name made lowercase. The composite primary key (Code_site, NT, Code_Tache) found, that is not supported. The first column is selected.
    nt = models.ForeignKey(TabNt, models.DO_NOTHING, db_column='NT', to_field='NT', related_name='tabnttaches_nt_set')  # Field name made lowercase.
    code_tache = models.CharField(db_column='Code_Tache', max_length=30)  # Field name made lowercase.
    est_tache_composite = models.BooleanField(db_column='Est_Tache_Composite', blank=True, null=True)  # Field name made lowercase.
    est_tache_complementaire = models.BooleanField(db_column='Est_Tache_Complementaire', blank=True, null=True)  # Field name made lowercase.
    libelle_tache = models.TextField(db_column='Libelle_Tache', blank=True, null=True)  # Field name made lowercase.
    code_unite_mesure = models.ForeignKey('TabUniteDeMesure', models.DO_NOTHING, db_column='Code_Unite_Mesure', blank=True, null=True)  # Field name made lowercase.
    quantite = models.FloatField(db_column='Quantite', blank=True, null=True)  # Field name made lowercase.
    prix_unitaire = models.DecimalField(db_column='Prix_Unitaire', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    est_bloquer = models.BooleanField(db_column='Est_Bloquer', blank=True, null=True)  # Field name made lowercase.
    user_id = models.CharField(db_column='User_ID', max_length=15, blank=True, null=True)  # Field name made lowercase.
    date_modification = models.DateTimeField(db_column='Date_Modification', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tab_NT_Taches'
        unique_together = (('code_site', 'nt', 'code_tache'),)


class TabNtTachesAvenant(models.Model):
    code_site = models.OneToOneField(TabNt, models.DO_NOTHING, db_column='Code_Site', primary_key=True)  # Field name made lowercase. The composite primary key (Code_Site, NT, Code_Tache, Num_Avenant) found, that is not supported. The first column is selected.
    nt = models.ForeignKey(TabNt, models.DO_NOTHING, db_column='NT', to_field='NT', related_name='tabnttachesavenant_nt_set')  # Field name made lowercase.
    code_tache = models.CharField(db_column='Code_Tache', max_length=30)  # Field name made lowercase.
    num_avenant = models.IntegerField(db_column='Num_Avenant')  # Field name made lowercase.
    est_tache_composite = models.BooleanField(db_column='Est_Tache_Composite', blank=True, null=True)  # Field name made lowercase.
    est_tache_complementaire = models.BooleanField(db_column='Est_Tache_Complementaire', blank=True, null=True)  # Field name made lowercase.
    libelle_tache = models.TextField(db_column='Libelle_Tache', blank=True, null=True)  # Field name made lowercase.
    code_unite_mesure = models.ForeignKey('TabUniteDeMesure', models.DO_NOTHING, db_column='Code_Unite_Mesure', blank=True, null=True)  # Field name made lowercase.
    quantite = models.FloatField(db_column='Quantite', blank=True, null=True)  # Field name made lowercase.
    prix_unitaire = models.DecimalField(db_column='Prix_Unitaire', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    est_bloquer = models.BooleanField(db_column='Est_Bloquer', blank=True, null=True)  # Field name made lowercase.
    user_id = models.CharField(db_column='User_ID', max_length=15, blank=True, null=True)  # Field name made lowercase.
    date_modification = models.DateTimeField(db_column='Date_Modification', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tab_NT_Taches_Avenant'
        unique_together = (('code_site', 'nt', 'code_tache', 'num_avenant'),)


class TabNatureCharge(models.Model):
    code_nature_charge = models.CharField(db_column='Code_Nature_Charge', primary_key=True, max_length=4)  # Field name made lowercase.
    nature_charge = models.CharField(db_column='Nature_Charge', max_length=50, blank=True, null=True)  # Field name made lowercase.
    est_bloquer = models.BooleanField(db_column='Est_Bloquer', blank=True, null=True)  # Field name made lowercase.
    user_id = models.CharField(db_column='User_ID', max_length=15, blank=True, null=True)  # Field name made lowercase.
    date_modification = models.DateTimeField(db_column='Date_Modification', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tab_Nature_Charge'


class TabNatureRubriques(models.Model):
    code_nature = models.CharField(db_column='Code_Nature', primary_key=True, max_length=5)  # Field name made lowercase.
    libelle_nature = models.CharField(db_column='Libelle_Nature', max_length=30)  # Field name made lowercase.
    impacter_par_evenement_rh = models.BooleanField(db_column='Impacter_Par_Evenement_RH', blank=True, null=True)  # Field name made lowercase.
    est_bloquer = models.BooleanField(db_column='Est_Bloquer', blank=True, null=True)  # Field name made lowercase.
    user_id = models.CharField(db_column='User_ID', max_length=15, blank=True, null=True)  # Field name made lowercase.
    date_modification = models.DateTimeField(db_column='Date_Modification', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tab_Nature_Rubriques'


class TabNiveauEtudes(models.Model):
    code_niveau_etudes = models.CharField(db_column='Code_Niveau_Etudes', primary_key=True, max_length=5)  # Field name made lowercase.
    niveau_etude = models.SmallIntegerField(db_column='Niveau_Etude', blank=True, null=True)  # Field name made lowercase.
    libelle_niveau_etudes = models.CharField(db_column='Libelle_Niveau_Etudes', max_length=50, blank=True, null=True)  # Field name made lowercase.
    description = models.TextField(db_column='Description', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    est_bloquer = models.BooleanField(db_column='Est_Bloquer', blank=True, null=True)  # Field name made lowercase.
    user_id = models.CharField(db_column='User_ID', max_length=15, blank=True, null=True)  # Field name made lowercase.
    date_modification = models.DateTimeField(db_column='Date_Modification', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tab_Niveau_Etudes'


class TabNiveauResponsabilite(models.Model):
    code_niveau_resp = models.CharField(db_column='Code_Niveau_Resp', primary_key=True, max_length=5)  # Field name made lowercase.
    libelle_niveau_resp = models.CharField(db_column='Libelle_Niveau_Resp', max_length=50, blank=True, null=True)  # Field name made lowercase.
    acronyme = models.CharField(db_column='Acronyme', max_length=20, blank=True, null=True)  # Field name made lowercase.
    est_bloquer = models.BooleanField(db_column='Est_Bloquer', blank=True, null=True)  # Field name made lowercase.
    user_id = models.CharField(db_column='User_ID', max_length=15, blank=True, null=True)  # Field name made lowercase.
    date_modification = models.DateTimeField(db_column='Date_Modification', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tab_Niveau_Responsabilite'


class TabNtCharges(models.Model):
    code_site = models.OneToOneField(TabNt, models.DO_NOTHING, db_column='Code_site', primary_key=True)  # Field name made lowercase. The composite primary key (Code_site, NT, Code_Charge) found, that is not supported. The first column is selected.
    nt = models.ForeignKey(TabNt, models.DO_NOTHING, db_column='NT', to_field='NT', related_name='tabntcharges_nt_set')  # Field name made lowercase.
    code_charge = models.ForeignKey(TabCharge, models.DO_NOTHING, db_column='Code_Charge')  # Field name made lowercase.
    est_bloquer = models.BooleanField(db_column='Est_Bloquer', blank=True, null=True)  # Field name made lowercase.
    user_id = models.CharField(db_column='User_ID', max_length=15, blank=True, null=True)  # Field name made lowercase.
    date_modification = models.DateTimeField(db_column='Date_Modification', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tab_Nt_Charges'
        unique_together = (('code_site', 'nt', 'code_charge'),)


class TabObjectifsFormation(models.Model):
    id_objectifs_formation = models.AutoField(db_column='ID_Objectifs_Formation', primary_key=True)  # Field name made lowercase.
    code_objectifs_formation = models.CharField(db_column='Code_Objectifs_Formation', unique=True, max_length=21)  # Field name made lowercase.
    code_formation = models.ForeignKey(TabFormations, models.DO_NOTHING, db_column='Code_Formation')  # Field name made lowercase.
    libelle_objectif = models.CharField(db_column='Libelle_Objectif', max_length=100)  # Field name made lowercase.
    est_bloquer = models.BooleanField(db_column='Est_Bloquer', blank=True, null=True)  # Field name made lowercase.
    user_id = models.CharField(db_column='User_ID', max_length=15, blank=True, null=True)  # Field name made lowercase.
    date_modification = models.DateTimeField(db_column='Date_Modification', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tab_Objectifs_Formation'


class TabOrganismesFormations(models.Model):
    code_organisme = models.CharField(db_column='Code_Organisme', primary_key=True, max_length=20)  # Field name made lowercase.
    libelle_organisme = models.CharField(db_column='Libelle_Organisme', max_length=150, blank=True, null=True)  # Field name made lowercase.
    est_bloquer = models.BooleanField(db_column='Est_Bloquer', blank=True, null=True)  # Field name made lowercase.
    user_id = models.CharField(db_column='User_ID', max_length=15, blank=True, null=True)  # Field name made lowercase.
    date_modification = models.DateTimeField(db_column='Date_Modification', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tab_Organismes_Formations'


class TabPerformanceAgent(models.Model):
    code_performance_agent = models.CharField(db_column='Code_Performance_Agent', primary_key=True, max_length=18)  # Field name made lowercase.
    matricule = models.ForeignKey(TabAgent, models.DO_NOTHING, db_column='Matricule')  # Field name made lowercase.
    date_performance = models.DateField(db_column='Date_Performance', blank=True, null=True)  # Field name made lowercase.
    exercice = models.CharField(db_column='Exercice', max_length=10)  # Field name made lowercase.
    mois = models.CharField(db_column='Mois', max_length=10)  # Field name made lowercase.
    note_globale = models.FloatField(db_column='Note_Globale', blank=True, null=True)  # Field name made lowercase.
    est_correction_performance = models.BooleanField(db_column='Est_Correction_Performance', blank=True, null=True)  # Field name made lowercase.
    est_bloquer = models.BooleanField(db_column='Est_Bloquer', blank=True, null=True)  # Field name made lowercase.
    user_id = models.CharField(db_column='User_ID', max_length=15, blank=True, null=True)  # Field name made lowercase.
    date_modification = models.DateTimeField(db_column='Date_Modification', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tab_Performance_Agent'
        unique_together = (('matricule', 'exercice', 'mois', 'est_correction_performance', 'est_bloquer'),)


class TabPlanRubriques(models.Model):
    code_rubrique = models.CharField(db_column='Code_Rubrique', primary_key=True, max_length=5)  # Field name made lowercase.
    code_type = models.ForeignKey('TabTypeRubriques', models.DO_NOTHING, db_column='Code_Type')  # Field name made lowercase.
    code_nature = models.ForeignKey(TabNatureRubriques, models.DO_NOTHING, db_column='Code_Nature')  # Field name made lowercase.
    libelle_rubrique = models.CharField(db_column='Libelle_Rubrique', max_length=50, blank=True, null=True)  # Field name made lowercase.
    rubrique_parent = models.ForeignKey('self', models.DO_NOTHING, db_column='Rubrique_Parent', blank=True, null=True)  # Field name made lowercase.
    sens = models.SmallIntegerField(db_column='Sens')  # Field name made lowercase.
    avec_nombre = models.BooleanField(db_column='Avec_Nombre', blank=True, null=True)  # Field name made lowercase.
    avec_base = models.BooleanField(db_column='Avec_Base', blank=True, null=True)  # Field name made lowercase.
    avec_taux = models.BooleanField(db_column='Avec_Taux', blank=True, null=True)  # Field name made lowercase.
    avec_montant = models.BooleanField(db_column='Avec_Montant', blank=True, null=True)  # Field name made lowercase.
    formule = models.CharField(db_column='Formule', max_length=250, blank=True, null=True)  # Field name made lowercase.
    soumi_absence = models.BooleanField(db_column='Soumi_Absence', blank=True, null=True)  # Field name made lowercase.
    soumi_irg = models.CharField(db_column='Soumi_IRG', max_length=3)  # Field name made lowercase.
    mode_calcule_irg = models.SmallIntegerField(db_column='Mode_Calcule_IRG')  # Field name made lowercase.
    rubrique_irg = models.CharField(db_column='Rubrique_IRG', max_length=5, blank=True, null=True)  # Field name made lowercase.
    soumi_ss = models.BooleanField(db_column='Soumi_SS')  # Field name made lowercase.
    rubrique_ss = models.CharField(db_column='Rubrique_SS', max_length=5, blank=True, null=True)  # Field name made lowercase.
    impacte_par_stat_h = models.BooleanField(db_column='Impacte_Par_Stat_H', blank=True, null=True)  # Field name made lowercase.
    soumi_chm_intmp = models.BooleanField(db_column='Soumi_CHM_INTMP')  # Field name made lowercase.
    rub_chm_intmp = models.CharField(db_column='Rub_CHM_INTMP', max_length=5, blank=True, null=True)  # Field name made lowercase.
    inclue_brute = models.BooleanField(db_column='Inclue_Brute', blank=True, null=True)  # Field name made lowercase.
    inclu_formation = models.BooleanField(db_column='Inclu_Formation', blank=True, null=True)  # Field name made lowercase.
    inclu_apprentissage = models.BooleanField(db_column='Inclu_Apprentissage', blank=True, null=True)  # Field name made lowercase.
    inclu_mass_sal = models.BooleanField(db_column='Inclu_Mass_Sal', blank=True, null=True)  # Field name made lowercase.
    inclu_oeuvr_socl = models.BooleanField(db_column='Inclu_Oeuvr_Socl', blank=True, null=True)  # Field name made lowercase.
    inclu_opreb = models.BooleanField(db_column='Inclu_OPREB', blank=True, null=True)  # Field name made lowercase.
    afficher_journal_paie = models.BooleanField(db_column='Afficher_Journal_Paie', blank=True, null=True)  # Field name made lowercase.
    afficher_bulletin = models.BooleanField(db_column='Afficher_Bulletin', blank=True, null=True)  # Field name made lowercase.
    afficher_mass_sal = models.BooleanField(db_column='Afficher_Mass_Sal', blank=True, null=True)  # Field name made lowercase.
    comptabiliser = models.BooleanField(db_column='Comptabiliser', blank=True, null=True)  # Field name made lowercase.
    compte_debit = models.CharField(db_column='Compte_Debit', max_length=10, blank=True, null=True)  # Field name made lowercase.
    compte_credit = models.CharField(db_column='Compte_Credit', max_length=10, blank=True, null=True)  # Field name made lowercase.
    avec_decision = models.BooleanField(db_column='Avec_Decision', blank=True, null=True)  # Field name made lowercase.
    commentaire = models.CharField(db_column='Commentaire', max_length=100, blank=True, null=True)  # Field name made lowercase.
    est_bloquer = models.BooleanField(db_column='Est_Bloquer', blank=True, null=True)  # Field name made lowercase.
    user_id = models.CharField(db_column='User_ID', max_length=15, blank=True, null=True)  # Field name made lowercase.
    date_modification = models.DateTimeField(db_column='Date_Modification', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tab_Plan_Rubriques'


class TabPosteTravail(models.Model):
    code_poste_travail = models.CharField(db_column='Code_Poste_Travail', primary_key=True, max_length=10)  # Field name made lowercase.
    code_niveau_resp = models.ForeignKey(TabNiveauResponsabilite, models.DO_NOTHING, db_column='Code_Niveau_Resp')  # Field name made lowercase.
    code_famille_poste_travail = models.ForeignKey(TabFamillePosteTravail, models.DO_NOTHING, db_column='Code_Famille_Poste_Travail')  # Field name made lowercase.
    libelle_poste_travail = models.CharField(db_column='Libelle_poste_travail', max_length=50, blank=True, null=True)  # Field name made lowercase.
    acronyme = models.CharField(db_column='Acronyme', max_length=20, blank=True, null=True)  # Field name made lowercase.
    experience_min = models.CharField(db_column='Experience_Min', max_length=50, blank=True, null=True)  # Field name made lowercase.
    age_min = models.CharField(db_column='Age_Min', max_length=50, blank=True, null=True)  # Field name made lowercase.
    age_max = models.CharField(db_column='Age_Max', max_length=50, blank=True, null=True)  # Field name made lowercase.
    code_classification_min = models.ForeignKey(TabClassification, models.DO_NOTHING, db_column='Code_Classification_Min', blank=True, null=True)  # Field name made lowercase.
    code_classification_max = models.ForeignKey(TabClassification, models.DO_NOTHING, db_column='Code_Classification_Max', related_name='tabpostetravail_code_classification_max_set', blank=True, null=True)  # Field name made lowercase.
    code_fonction_cac = models.CharField(db_column='Code_Fonction_CAC', max_length=5, blank=True, null=True)  # Field name made lowercase.
    libelle_fonction_cac = models.CharField(db_column='Libelle_Fonction_CAC', max_length=100, blank=True, null=True)  # Field name made lowercase.
    est_bloquer = models.BooleanField(db_column='Est_Bloquer', blank=True, null=True)  # Field name made lowercase.
    user_id = models.CharField(db_column='User_ID', max_length=15, blank=True, null=True)  # Field name made lowercase.
    date_modification = models.DateTimeField(db_column='Date_Modification', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tab_Poste_Travail'


class TabProduction(models.Model):
    id_production = models.AutoField(db_column='ID_Production', primary_key=True)  # Field name made lowercase.
    code_type_production = models.ForeignKey('TabTypeProduction', models.DO_NOTHING, db_column='Code_Type_Production')  # Field name made lowercase.
    code_site = models.ForeignKey(TabActiviteTaches, models.DO_NOTHING, db_column='Code_site', to_field='NT')  # Field name made lowercase.
    code_filiale = models.CharField(db_column='Code_Filiale', max_length=5, blank=True, null=True)  # Field name made lowercase.
    nt = models.ForeignKey(TabActiviteTaches, models.DO_NOTHING, db_column='NT', to_field='NT', related_name='tabproduction_nt_set', blank=True, null=True)  # Field name made lowercase.
    code_groupeactivite = models.ForeignKey(TabActiviteTaches, models.DO_NOTHING, db_column='Code_GroupeActivite', to_field='NT', related_name='tabproduction_code_groupeactivite_set', blank=True, null=True)  # Field name made lowercase.
    code_activite = models.ForeignKey(TabActiviteTaches, models.DO_NOTHING, db_column='Code_Activite', to_field='NT', related_name='tabproduction_code_activite_set', blank=True, null=True)  # Field name made lowercase.
    code_tache = models.ForeignKey(TabActiviteTaches, models.DO_NOTHING, db_column='Code_Tache', to_field='NT', related_name='tabproduction_code_tache_set', blank=True, null=True)  # Field name made lowercase.
    recepteur = models.CharField(db_column='Recepteur', max_length=20, blank=True, null=True)  # Field name made lowercase.
    code_produit = models.ForeignKey('TabProduitManufacture', models.DO_NOTHING, db_column='Code_Produit', blank=True, null=True)  # Field name made lowercase.
    code_unite_mesure = models.ForeignKey('TabUniteDeMesure', models.DO_NOTHING, db_column='Code_Unite_Mesure', blank=True, null=True)  # Field name made lowercase.
    type_prestation = models.SmallIntegerField(db_column='Type_Prestation', blank=True, null=True)  # Field name made lowercase.
    mmaa = models.DateField(db_column='Mmaa')  # Field name made lowercase.
    quantite_1 = models.FloatField(db_column='Quantite_1', blank=True, null=True)  # Field name made lowercase.
    valeur_1 = models.DecimalField(db_column='Valeur_1', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    quantite_2 = models.FloatField(db_column='Quantite_2', blank=True, null=True)  # Field name made lowercase.
    valeur_2 = models.DecimalField(db_column='Valeur_2', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    quantite_3 = models.FloatField(db_column='Quantite_3', blank=True, null=True)  # Field name made lowercase.
    valeur_3 = models.DecimalField(db_column='Valeur_3', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    prevu_realiser = models.CharField(db_column='Prevu_Realiser', max_length=1)  # Field name made lowercase.
    est_cloturer = models.BooleanField(db_column='Est_Cloturer', blank=True, null=True)  # Field name made lowercase.
    user_id = models.CharField(db_column='User_ID', max_length=15, blank=True, null=True)  # Field name made lowercase.
    date_modification = models.DateTimeField(db_column='Date_Modification', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tab_Production'


class TabProduitManufacture(models.Model):
    code_produit = models.CharField(db_column='Code_Produit', primary_key=True, max_length=4)  # Field name made lowercase.
    lib_produit = models.CharField(db_column='Lib_Produit', max_length=50, blank=True, null=True)  # Field name made lowercase.
    avec_quantite = models.BooleanField(db_column='Avec_Quantite', blank=True, null=True)  # Field name made lowercase.
    code_unite_mesure = models.ForeignKey('TabUniteDeMesure', models.DO_NOTHING, db_column='Code_Unite_Mesure', blank=True, null=True)  # Field name made lowercase.
    option_affichage = models.SmallIntegerField(db_column='Option_Affichage')  # Field name made lowercase.
    est_bloquer = models.BooleanField(db_column='Est_Bloquer', blank=True, null=True)  # Field name made lowercase.
    user_id = models.CharField(db_column='User_ID', max_length=15, blank=True, null=True)  # Field name made lowercase.
    date_modification = models.DateTimeField(db_column='Date_Modification', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tab_Produit_Manufacture'


class TabProfils(models.Model):
    code_profil = models.CharField(db_column='Code_Profil', primary_key=True, max_length=5)  # Field name made lowercase.
    code_module = models.ForeignKey(TabModules, models.DO_NOTHING, db_column='Code_Module', blank=True, null=True)  # Field name made lowercase.
    code_famille_fonction = models.ForeignKey(TabFamillesFonctions, models.DO_NOTHING, db_column='Code_Famille_Fonction', blank=True, null=True)  # Field name made lowercase.
    libelle_profil = models.CharField(db_column='Libelle_Profil', max_length=50)  # Field name made lowercase.
    type_profil = models.SmallIntegerField(db_column='Type_Profil', blank=True, null=True)  # Field name made lowercase.
    est_bloquer = models.BooleanField(db_column='Est_Bloquer', blank=True, null=True)  # Field name made lowercase.
    user_id = models.CharField(db_column='User_ID', max_length=15, blank=True, null=True)  # Field name made lowercase.
    date_modification = models.DateTimeField(db_column='Date_Modification', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tab_Profils'


class TabProfilsConsultant(models.Model):
    id_consultant = models.ForeignKey(TabConsultant, models.DO_NOTHING, db_column='ID_Consultant')  # Field name made lowercase.
    code_profil = models.OneToOneField(TabProfils, models.DO_NOTHING, db_column='Code_Profil', primary_key=True)  # Field name made lowercase. The composite primary key (Code_Profil, ID_Consultant) found, that is not supported. The first column is selected.
    est_bloquer = models.BooleanField(db_column='Est_Bloquer', blank=True, null=True)  # Field name made lowercase.
    user_creator = models.CharField(db_column='User_Creator', max_length=15, blank=True, null=True)  # Field name made lowercase.
    date_modification = models.DateTimeField(db_column='Date_Modification', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tab_Profils_Consultant'
        unique_together = (('code_profil', 'id_consultant'),)


class TabProfilsFonctions(models.Model):
    code_profil = models.ForeignKey(TabProfils, models.DO_NOTHING, db_column='Code_Profil')  # Field name made lowercase.
    code_fonction = models.OneToOneField(TabFonctionsInterface, models.DO_NOTHING, db_column='Code_Fonction', primary_key=True)  # Field name made lowercase. The composite primary key (Code_Fonction, Code_Profil) found, that is not supported. The first column is selected.
    est_bloquer = models.BooleanField(db_column='Est_Bloquer', blank=True, null=True)  # Field name made lowercase.
    user_id = models.CharField(db_column='User_ID', max_length=15, blank=True, null=True)  # Field name made lowercase.
    date_modification = models.DateTimeField(db_column='Date_Modification', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tab_Profils_Fonctions'
        unique_together = (('code_fonction', 'code_profil'),)


class TabProfilsUsers(models.Model):
    code_profil_user = models.CharField(db_column='Code_Profil_User', primary_key=True, max_length=20)  # Field name made lowercase.
    user = models.ForeignKey('TabUsers', models.DO_NOTHING, db_column='User_ID')  # Field name made lowercase.
    code_profil = models.ForeignKey(TabProfils, models.DO_NOTHING, db_column='Code_Profil')  # Field name made lowercase.
    est_personnaliser = models.BooleanField(db_column='Est_Personnaliser', blank=True, null=True)  # Field name made lowercase.
    est_bloquer = models.BooleanField(db_column='Est_Bloquer', blank=True, null=True)  # Field name made lowercase.
    user_creator = models.CharField(db_column='User_Creator', max_length=15, blank=True, null=True)  # Field name made lowercase.
    date_modification = models.DateTimeField(db_column='Date_Modification', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tab_Profils_Users'


class TabPromotionAgent(models.Model):
    id_promotion_agent = models.AutoField(db_column='ID_Promotion_Agent', primary_key=True)  # Field name made lowercase.
    matricule = models.ForeignKey(TabAgent, models.DO_NOTHING, db_column='Matricule', blank=True, null=True)  # Field name made lowercase.
    code_contrat = models.ForeignKey(TabAgentContrat, models.DO_NOTHING, db_column='Code_Contrat', blank=True, null=True)  # Field name made lowercase.
    classification = models.ForeignKey(TabClassification, models.DO_NOTHING, db_column='Classification', blank=True, null=True)  # Field name made lowercase.
    code_poste_travail = models.ForeignKey(TabPosteTravail, models.DO_NOTHING, db_column='Code_Poste_Travail', blank=True, null=True)  # Field name made lowercase.
    date_classification = models.DateField(db_column='Date_Classification', blank=True, null=True)  # Field name made lowercase.
    date_fonction = models.DateField(db_column='Date_Fonction', blank=True, null=True)  # Field name made lowercase.
    nbr_promtion_agent = models.SmallIntegerField(db_column='Nbr_Promtion_Agent', blank=True, null=True)  # Field name made lowercase.
    type_promotion = models.SmallIntegerField(db_column='Type_Promotion', blank=True, null=True)  # Field name made lowercase.
    motif_promotion = models.CharField(db_column='Motif_Promotion', max_length=100, blank=True, null=True)  # Field name made lowercase.
    code_decision = models.CharField(db_column='Code_Decision', max_length=18, blank=True, null=True)  # Field name made lowercase.
    date_fin_fonction = models.DateField(db_column='Date_Fin_Fonction', blank=True, null=True)  # Field name made lowercase.
    est_bloquer = models.BooleanField(db_column='Est_Bloquer', blank=True, null=True)  # Field name made lowercase.
    user_id = models.CharField(db_column='User_ID', max_length=15, blank=True, null=True)  # Field name made lowercase.
    date_modification = models.DateTimeField(db_column='Date_Modification', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tab_Promotion_Agent'
        unique_together = (('matricule', 'nbr_promtion_agent'),)


class TabQualification(models.Model):
    code_qualification = models.CharField(db_column='Code_Qualification', primary_key=True, max_length=5)  # Field name made lowercase.
    libelle_qualification = models.CharField(db_column='Libelle_Qualification', max_length=50, blank=True, null=True)  # Field name made lowercase.
    acronyme = models.CharField(db_column='Acronyme', max_length=20, blank=True, null=True)  # Field name made lowercase.
    est_bloquer = models.BooleanField(db_column='Est_Bloquer', blank=True, null=True)  # Field name made lowercase.
    user_id = models.CharField(db_column='User_ID', max_length=15, blank=True, null=True)  # Field name made lowercase.
    date_modification = models.DateTimeField(db_column='Date_Modification', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tab_Qualification'


class TabReliquatCongeAnnuel(models.Model):
    id_tab_reliquat_conge_annuel = models.AutoField(db_column='ID_Tab_Reliquat_Conge_Annuel', primary_key=True)  # Field name made lowercase.
    matricule = models.ForeignKey(TabAgent, models.DO_NOTHING, db_column='Matricule')  # Field name made lowercase.
    exercice = models.CharField(db_column='Exercice', max_length=10, blank=True, null=True)  # Field name made lowercase.
    nbr_jours_dus = models.SmallIntegerField(db_column='Nbr_Jours_Dus', blank=True, null=True)  # Field name made lowercase.
    est_bloquer = models.BooleanField(db_column='Est_Bloquer', blank=True, null=True)  # Field name made lowercase.
    user_id = models.CharField(db_column='User_ID', max_length=15, blank=True, null=True)  # Field name made lowercase.
    date_modification = models.DateTimeField(db_column='Date_Modification', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tab_Reliquat_Conge_Annuel'
        unique_together = (('matricule', 'exercice'),)


class TabRubriquesEvalutionPerformance(models.Model):
    code_performance_agent = models.OneToOneField(TabPerformanceAgent, models.DO_NOTHING, db_column='Code_Performance_Agent', primary_key=True)  # Field name made lowercase. The composite primary key (Code_Performance_Agent, Code_Rubrique_Performance) found, that is not supported. The first column is selected.
    code_rubrique_performance = models.ForeignKey('TabRubriquesPerformance', models.DO_NOTHING, db_column='Code_Rubrique_Performance')  # Field name made lowercase.
    taux_evaluation_performance = models.FloatField(db_column='Taux_Evaluation_Performance', blank=True, null=True)  # Field name made lowercase.
    est_bloquer = models.BooleanField(db_column='Est_Bloquer', blank=True, null=True)  # Field name made lowercase.
    user_id = models.CharField(db_column='User_ID', max_length=15, blank=True, null=True)  # Field name made lowercase.
    date_modification = models.DateTimeField(db_column='Date_Modification', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tab_Rubriques_Evalution_Performance'
        unique_together = (('code_performance_agent', 'code_rubrique_performance'),)


class TabRubriquesImpacteesParEvenementRh(models.Model):
    code_evenement = models.ForeignKey(TabEvenementRh, models.DO_NOTHING, db_column='Code_Evenement')  # Field name made lowercase.
    code_rubrique = models.OneToOneField(TabPlanRubriques, models.DO_NOTHING, db_column='Code_Rubrique', primary_key=True)  # Field name made lowercase. The composite primary key (Code_Rubrique, Code_Evenement) found, that is not supported. The first column is selected.
    type_regularisation = models.SmallIntegerField(db_column='Type_Regularisation', blank=True, null=True)  # Field name made lowercase.
    est_bloquer = models.BooleanField(db_column='Est_Bloquer', blank=True, null=True)  # Field name made lowercase.
    user_id = models.CharField(db_column='User_ID', max_length=15, blank=True, null=True)  # Field name made lowercase.
    date_modification = models.DateTimeField(db_column='Date_Modification', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tab_Rubriques_Impactees_Par_Evenement_RH'
        unique_together = (('code_rubrique', 'code_evenement'),)


class TabRubriquesPerformance(models.Model):
    code_rubrique_performance = models.CharField(db_column='Code_Rubrique_Performance', primary_key=True, max_length=15)  # Field name made lowercase.
    libelle_rubrique_performance = models.CharField(db_column='Libelle_Rubrique_Performance', max_length=50, blank=True, null=True)  # Field name made lowercase.
    type_performance = models.SmallIntegerField(db_column='Type_Performance', blank=True, null=True)  # Field name made lowercase.
    taux_evaluation_maximale = models.FloatField(db_column='Taux_Evaluation_Maximale', blank=True, null=True)  # Field name made lowercase.
    est_bloquer = models.BooleanField(db_column='Est_Bloquer', blank=True, null=True)  # Field name made lowercase.
    user_id = models.CharField(db_column='User_ID', max_length=15, blank=True, null=True)  # Field name made lowercase.
    date_modification = models.DateTimeField(db_column='Date_Modification', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tab_Rubriques_Performance'


class TabSite(models.Model):
    code_site = models.CharField(db_column='Code_site', primary_key=True, max_length=10)  # Field name made lowercase.
    code_filiale = models.ForeignKey(TabFiliale, models.DO_NOTHING, db_column='Code_Filiale')  # Field name made lowercase.
    code_region = models.CharField(db_column='Code_Region', max_length=1, blank=True, null=True)  # Field name made lowercase.
    libelle_site = models.CharField(db_column='Libelle_Site', max_length=150, blank=True, null=True)  # Field name made lowercase.
    code_agence = models.ForeignKey(TabAgence, models.DO_NOTHING, db_column='Code_Agence', blank=True, null=True)  # Field name made lowercase.
    type_site = models.SmallIntegerField(db_column='Type_Site', blank=True, null=True)  # Field name made lowercase.
    code_division = models.ForeignKey(TabDivision, models.DO_NOTHING, db_column='Code_Division', blank=True, null=True)  # Field name made lowercase.
    code_commune_site = models.CharField(db_column='Code_Commune_Site', max_length=10, blank=True, null=True)  # Field name made lowercase.
    jour_cloture_mouv_rh_paie = models.CharField(db_column='Jour_Cloture_Mouv_RH_Paie', max_length=2, blank=True, null=True)  # Field name made lowercase.
    date_ouverture_site = models.DateField(db_column='Date_Ouverture_Site', blank=True, null=True)  # Field name made lowercase.
    date_cloture_site = models.DateField(db_column='Date_Cloture_Site', blank=True, null=True)  # Field name made lowercase.
    est_bloquer = models.BooleanField(db_column='Est_Bloquer', blank=True, null=True)  # Field name made lowercase.
    user_id = models.CharField(db_column='User_ID', max_length=15, blank=True, null=True)  # Field name made lowercase.
    date_modification = models.DateTimeField(db_column='Date_Modification', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tab_Site'


class TabSituationNt(models.Model):
    code_situation_nt = models.CharField(db_column='Code_Situation_NT', primary_key=True, max_length=2)  # Field name made lowercase.
    libelle_situation_nt = models.CharField(db_column='Libelle_Situation_NT', max_length=50, blank=True, null=True)  # Field name made lowercase.
    est_bloquer = models.BooleanField(db_column='Est_Bloquer', blank=True, null=True)  # Field name made lowercase.
    user_id = models.CharField(db_column='User_ID', max_length=15, blank=True, null=True)  # Field name made lowercase.
    date_modification = models.DateTimeField(db_column='Date_Modification', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tab_Situation_NT'


class TabSortieAtelierproduction(models.Model):
    id_sortie_atelier = models.AutoField(db_column='Id_Sortie_Atelier', primary_key=True)  # Field name made lowercase.
    code_structure = models.CharField(db_column='Code_Structure', max_length=15)  # Field name made lowercase.
    code_produit = models.CharField(db_column='Code_Produit', max_length=4)  # Field name made lowercase.
    code_unite_mesure = models.ForeignKey('TabUniteDeMesure', models.DO_NOTHING, db_column='Code_Unite_Mesure', blank=True, null=True)  # Field name made lowercase.
    code_site = models.ForeignKey(TabNt, models.DO_NOTHING, db_column='Code_site', to_field='NT')  # Field name made lowercase.
    nt = models.ForeignKey(TabNt, models.DO_NOTHING, db_column='NT', to_field='NT', related_name='tabsortieatelierproduction_nt_set', blank=True, null=True)  # Field name made lowercase.
    site_emetteur = models.CharField(db_column='Site_Emetteur', max_length=10, blank=True, null=True)  # Field name made lowercase.
    code_structure_destination = models.CharField(db_column='Code_Structure_Destination', max_length=15, blank=True, null=True)  # Field name made lowercase.
    code_client = models.ForeignKey(TabClient, models.DO_NOTHING, db_column='Code_Client', blank=True, null=True)  # Field name made lowercase.
    quantite = models.FloatField(db_column='Quantite', blank=True, null=True)  # Field name made lowercase.
    mmaa = models.DateField(db_column='Mmaa')  # Field name made lowercase.
    est_cloturer = models.BooleanField(db_column='Est_Cloturer', blank=True, null=True)  # Field name made lowercase.
    user_id = models.CharField(db_column='User_ID', max_length=15, blank=True, null=True)  # Field name made lowercase.
    date_modification = models.DateTimeField(db_column='Date_Modification', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tab_Sortie_AtelierProduction'


class TabSortieMagasinVesrsNt(models.Model):
    code_site = models.OneToOneField(TabNt, models.DO_NOTHING, db_column='Code_site', primary_key=True)  # Field name made lowercase. The composite primary key (Code_site, NT, Code_Charge, Mmaa) found, that is not supported. The first column is selected.
    nt = models.ForeignKey(TabNt, models.DO_NOTHING, db_column='NT', to_field='NT', related_name='tabsortiemagasinvesrsnt_nt_set')  # Field name made lowercase.
    code_charge = models.ForeignKey(TabCharge, models.DO_NOTHING, db_column='Code_Charge')  # Field name made lowercase.
    code_type_charge = models.ForeignKey('TabTypeCharge', models.DO_NOTHING, db_column='Code_Type_Charge', blank=True, null=True)  # Field name made lowercase.
    code_unite_mesure = models.CharField(db_column='Code_Unite_Mesure', max_length=4, blank=True, null=True)  # Field name made lowercase.
    mmaa = models.DateField(db_column='Mmaa')  # Field name made lowercase.
    quantite = models.FloatField(db_column='Quantite', blank=True, null=True)  # Field name made lowercase.
    valeur = models.DecimalField(db_column='Valeur', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    est_cloturer = models.BooleanField(db_column='Est_Cloturer', blank=True, null=True)  # Field name made lowercase.
    user_id = models.CharField(db_column='User_ID', max_length=15, blank=True, null=True)  # Field name made lowercase.
    date_modification = models.DateTimeField(db_column='Date_Modification', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tab_Sortie_Magasin_Vesrs_NT'
        unique_together = (('code_site', 'nt', 'code_charge', 'mmaa'),)


class TabSpecialite(models.Model):
    code_specialite = models.CharField(db_column='Code_Specialite', primary_key=True, max_length=10)  # Field name made lowercase.
    code_domaine = models.ForeignKey(TabDomaine, models.DO_NOTHING, db_column='Code_Domaine', blank=True, null=True)  # Field name made lowercase.
    libelle_specialite = models.CharField(db_column='Libelle_Specialite', max_length=50, blank=True, null=True)  # Field name made lowercase.
    acronyme = models.CharField(db_column='Acronyme', max_length=20, blank=True, null=True)  # Field name made lowercase.
    niveau_etudes_minim = models.ForeignKey(TabNiveauEtudes, models.DO_NOTHING, db_column='Niveau_Etudes_Minim', blank=True, null=True)  # Field name made lowercase.
    niveau_etude_max = models.ForeignKey(TabNiveauEtudes, models.DO_NOTHING, db_column='Niveau_Etude_Max', related_name='tabspecialite_niveau_etude_max_set', blank=True, null=True)  # Field name made lowercase.
    est_bloquer = models.BooleanField(db_column='Est_Bloquer', blank=True, null=True)  # Field name made lowercase.
    user_id = models.CharField(db_column='User_ID', max_length=15, blank=True, null=True)  # Field name made lowercase.
    date_modification = models.DateTimeField(db_column='Date_Modification', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tab_Specialite'


class TabSpecialiteAgent(models.Model):
    id_specialite_agent = models.AutoField(db_column='ID_Specialite_Agent', primary_key=True)  # Field name made lowercase.
    matricule = models.ForeignKey(TabAgent, models.DO_NOTHING, db_column='Matricule', blank=True, null=True)  # Field name made lowercase.
    code_specialite = models.ForeignKey(TabSpecialite, models.DO_NOTHING, db_column='Code_Specialite')  # Field name made lowercase.
    code_diplome = models.ForeignKey(TabDiplome, models.DO_NOTHING, db_column='Code_diplome', blank=True, null=True)  # Field name made lowercase.
    est_principal = models.BooleanField(db_column='Est_Principal', blank=True, null=True)  # Field name made lowercase.
    date_diplome = models.DateField(db_column='Date_Diplome', blank=True, null=True)  # Field name made lowercase.
    etablissement = models.CharField(db_column='Etablissement', max_length=50, blank=True, null=True)  # Field name made lowercase.
    est_bloquer = models.BooleanField(db_column='Est_Bloquer', blank=True, null=True)  # Field name made lowercase.
    user_id = models.CharField(db_column='User_ID', max_length=15, blank=True, null=True)  # Field name made lowercase.
    date_modification = models.DateTimeField(db_column='Date_Modification', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tab_Specialite_Agent'
        unique_together = (('matricule', 'code_specialite', 'code_diplome'),)


class TabSpecialitePosteTravail(models.Model):
    code_specialite_poste_travail = models.CharField(db_column='Code_Specialite_Poste_Travail', primary_key=True, max_length=30)  # Field name made lowercase.
    code_specialite = models.ForeignKey(TabSpecialite, models.DO_NOTHING, db_column='Code_Specialite', blank=True, null=True)  # Field name made lowercase.
    code_poste_travail = models.ForeignKey(TabPosteTravail, models.DO_NOTHING, db_column='Code_Poste_Travail', blank=True, null=True)  # Field name made lowercase.
    code_diplome = models.ForeignKey(TabDiplome, models.DO_NOTHING, db_column='Code_diplome', blank=True, null=True)  # Field name made lowercase.
    est_bloquer = models.BooleanField(db_column='Est_Bloquer', blank=True, null=True)  # Field name made lowercase.
    user_id = models.CharField(db_column='User_ID', max_length=15, blank=True, null=True)  # Field name made lowercase.
    date_modification = models.DateTimeField(db_column='Date_Modification', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tab_Specialite_Poste_Travail'


class TabSpecialitesCompetences(models.Model):
    code_specialite = models.OneToOneField(TabSpecialite, models.DO_NOTHING, db_column='Code_Specialite', primary_key=True)  # Field name made lowercase. The composite primary key (Code_Specialite, Code_Competence) found, that is not supported. The first column is selected.
    code_competence = models.ForeignKey(TabCompetences, models.DO_NOTHING, db_column='Code_Competence')  # Field name made lowercase.
    est_bloquer = models.BooleanField(db_column='Est_Bloquer', blank=True, null=True)  # Field name made lowercase.
    user_id = models.CharField(db_column='User_ID', max_length=15, blank=True, null=True)  # Field name made lowercase.
    date_modification = models.DateTimeField(db_column='Date_Modification', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tab_Specialites_Competences'
        unique_together = (('code_specialite', 'code_competence'),)


class TabStatutHoraire(models.Model):
    code_statut_horaire = models.CharField(db_column='Code_Statut_Horaire', primary_key=True, max_length=5)  # Field name made lowercase.
    libelle_statut_horaire = models.CharField(db_column='Libelle_Statut_Horaire', max_length=20, blank=True, null=True)  # Field name made lowercase.
    taux_statut_horaire = models.FloatField(db_column='Taux_Statut_Horaire', blank=True, null=True)  # Field name made lowercase.
    est_bloquer = models.BooleanField(db_column='Est_Bloquer', blank=True, null=True)  # Field name made lowercase.
    user_id = models.CharField(db_column='User_ID', max_length=15, blank=True, null=True)  # Field name made lowercase.
    date_modification = models.DateTimeField(db_column='Date_Modification', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tab_Statut_Horaire'


class TabStructureMateriaux(models.Model):
    code_site = models.OneToOneField(TabSite, models.DO_NOTHING, db_column='Code_site', primary_key=True)  # Field name made lowercase. The composite primary key (Code_site, Code_Structure, Code_Charge) found, that is not supported. The first column is selected.
    code_structure = models.ForeignKey('TabStructures', models.DO_NOTHING, db_column='Code_Structure')  # Field name made lowercase.
    code_charge = models.ForeignKey(TabCharge, models.DO_NOTHING, db_column='Code_Charge')  # Field name made lowercase.
    est_bloquer = models.BooleanField(db_column='Est_Bloquer', blank=True, null=True)  # Field name made lowercase.
    user_id = models.CharField(db_column='User_ID', max_length=15, blank=True, null=True)  # Field name made lowercase.
    date_modification = models.DateTimeField(db_column='Date_Modification', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tab_Structure_Materiaux'
        unique_together = (('code_site', 'code_structure', 'code_charge'),)


class TabStructures(models.Model):
    code_structure = models.CharField(db_column='Code_Structure', primary_key=True, max_length=15)  # Field name made lowercase.
    code_site = models.ForeignKey(TabSite, models.DO_NOTHING, db_column='Code_Site')  # Field name made lowercase.
    libelle_structure = models.CharField(db_column='Libelle_Structure', max_length=255, blank=True, null=True)  # Field name made lowercase.
    nbr_agent_prevue = models.IntegerField(db_column='Nbr_Agent_Prevue', blank=True, null=True)  # Field name made lowercase.
    acronyme = models.CharField(db_column='Acronyme', max_length=20, blank=True, null=True)  # Field name made lowercase.
    code_parent = models.ForeignKey('self', models.DO_NOTHING, db_column='Code_Parent', blank=True, null=True)  # Field name made lowercase.
    niveau_hierarchique = models.SmallIntegerField(db_column='Niveau_Hierarchique', blank=True, null=True)  # Field name made lowercase.
    code_famille_structure = models.ForeignKey(TabFamilleStructures, models.DO_NOTHING, db_column='Code_Famille_Structure', blank=True, null=True)  # Field name made lowercase.
    opt_affichage = models.CharField(db_column='Opt_Affichage', max_length=150, blank=True, null=True)  # Field name made lowercase.
    est_structure_chantier = models.BooleanField(db_column='Est_Structure_Chantier', blank=True, null=True)  # Field name made lowercase.
    est_atelier_production = models.BooleanField(db_column='Est_Atelier_Production', blank=True, null=True)  # Field name made lowercase.
    avec_site_recepteur = models.BooleanField(db_column='Avec_Site_Recepteur', blank=True, null=True)  # Field name made lowercase.
    est_bloquer = models.BooleanField(db_column='Est_Bloquer', blank=True, null=True)  # Field name made lowercase.
    user_id = models.CharField(db_column='User_ID', max_length=15, blank=True, null=True)  # Field name made lowercase.
    date_modification = models.DateTimeField(db_column='Date_Modification', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tab_Structures'


class TabTachesGeneriques(models.Model):
    code_taches_generique = models.CharField(db_column='Code_Taches_Generique', primary_key=True, max_length=10)  # Field name made lowercase.
    code_famille_poste_travail = models.ForeignKey(TabFamillePosteTravail, models.DO_NOTHING, db_column='Code_Famille_Poste_Travail')  # Field name made lowercase.
    tache = models.CharField(db_column='Tache', max_length=250)  # Field name made lowercase.
    est_bloquer = models.BooleanField(db_column='Est_Bloquer', blank=True, null=True)  # Field name made lowercase.
    user_id = models.CharField(db_column='User_ID', max_length=15, blank=True, null=True)  # Field name made lowercase.
    date_modification = models.DateTimeField(db_column='Date_Modification', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tab_Taches_Generiques'


class TabTachesPersonnalisees(models.Model):
    matricule = models.OneToOneField(TabAgent, models.DO_NOTHING, db_column='Matricule', primary_key=True)  # Field name made lowercase. The composite primary key (Matricule, Code_Taches_Generique) found, that is not supported. The first column is selected.
    code_taches_generique = models.ForeignKey(TabTachesGeneriques, models.DO_NOTHING, db_column='Code_Taches_Generique')  # Field name made lowercase.
    est_bloquer = models.BooleanField(db_column='Est_Bloquer', blank=True, null=True)  # Field name made lowercase.
    user_id = models.CharField(db_column='User_ID', max_length=15, blank=True, null=True)  # Field name made lowercase.
    date_modification = models.DateTimeField(db_column='Date_Modification', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tab_Taches_Personnalisees'
        unique_together = (('matricule', 'code_taches_generique'),)


class TabTachesPosteTravail(models.Model):
    code_taches_generique = models.ForeignKey(TabTachesGeneriques, models.DO_NOTHING, db_column='Code_Taches_Generique')  # Field name made lowercase.
    code_poste_travail = models.OneToOneField(TabPosteTravail, models.DO_NOTHING, db_column='Code_Poste_Travail', primary_key=True)  # Field name made lowercase. The composite primary key (Code_Poste_Travail, Code_Taches_Generique) found, that is not supported. The first column is selected.
    est_bloquer = models.BooleanField(db_column='Est_Bloquer', blank=True, null=True)  # Field name made lowercase.
    user_id = models.CharField(db_column='User_ID', max_length=15, blank=True, null=True)  # Field name made lowercase.
    date_modification = models.DateTimeField(db_column='Date_Modification', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tab_Taches_Poste_Travail'
        unique_together = (('code_poste_travail', 'code_taches_generique'),)


class TabTauxFsTap(models.Model):
    code_filiale = models.OneToOneField(TabFiliale, models.DO_NOTHING, db_column='Code_Filiale', primary_key=True)  # Field name made lowercase. The composite primary key (Code_Filiale, Date_Debut) found, that is not supported. The first column is selected.
    date_debut = models.DateField(db_column='Date_Debut')  # Field name made lowercase.
    date_fin = models.DateField(db_column='Date_Fin', blank=True, null=True)  # Field name made lowercase.
    taux_fs = models.FloatField(db_column='TAUX_FS', blank=True, null=True)  # Field name made lowercase.
    taux_tap = models.FloatField(db_column='Taux_TAP', blank=True, null=True)  # Field name made lowercase.
    est_cloturer = models.BooleanField(db_column='Est_Cloturer', blank=True, null=True)  # Field name made lowercase.
    user_id = models.CharField(db_column='User_ID', max_length=15, blank=True, null=True)  # Field name made lowercase.
    date_modification = models.DateTimeField(db_column='Date_Modification', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tab_Taux_FS_TAP'
        unique_together = (('code_filiale', 'date_debut'),)


class TabTypeCharge(models.Model):
    code_type_charge = models.CharField(db_column='Code_Type_Charge', primary_key=True, max_length=4)  # Field name made lowercase.
    type_charge = models.CharField(db_column='Type_Charge', max_length=50, blank=True, null=True)  # Field name made lowercase.
    libelle_type_charge = models.CharField(db_column='Libelle_Type_Charge', max_length=80, blank=True, null=True)  # Field name made lowercase.
    est_bloquer = models.BooleanField(db_column='Est_Bloquer', blank=True, null=True)  # Field name made lowercase.
    user_id = models.CharField(db_column='User_ID', max_length=15, blank=True, null=True)  # Field name made lowercase.
    date_modification = models.DateTimeField(db_column='Date_Modification', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tab_Type_Charge'


class TabTypeContrat(models.Model):
    code_type_contrat = models.CharField(db_column='Code_Type_Contrat', primary_key=True, max_length=5)  # Field name made lowercase.
    libelle_type_contrat = models.CharField(db_column='Libelle_Type_Contrat', max_length=50, blank=True, null=True)  # Field name made lowercase.
    type_personnel = models.SmallIntegerField(db_column='Type_Personnel', blank=True, null=True)  # Field name made lowercase.
    est_temps_plein = models.BooleanField(db_column='Est_Temps_Plein', blank=True, null=True)  # Field name made lowercase.
    est_temps_partiel = models.BooleanField(db_column='Est_Temps_Partiel', blank=True, null=True)  # Field name made lowercase.
    est_bloquer = models.BooleanField(db_column='Est_Bloquer', blank=True, null=True)  # Field name made lowercase.
    user_id = models.CharField(db_column='User_ID', max_length=15, blank=True, null=True)  # Field name made lowercase.
    date_modification = models.DateTimeField(db_column='Date_Modification', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tab_Type_Contrat'


class TabTypeEvenementRh(models.Model):
    code_type_evenement = models.CharField(db_column='Code_Type_Evenement', primary_key=True, max_length=5)  # Field name made lowercase.
    libelle_type_evenement = models.CharField(db_column='Libelle_Type_Evenement', max_length=30, blank=True, null=True)  # Field name made lowercase.
    est_bloquer = models.BooleanField(db_column='Est_Bloquer', blank=True, null=True)  # Field name made lowercase.
    user_id = models.CharField(db_column='User_ID', max_length=15, blank=True, null=True)  # Field name made lowercase.
    date_modification = models.DateTimeField(db_column='Date_Modification', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tab_Type_Evenement_RH'


class TabTypeFormation(models.Model):
    code_type_formation = models.CharField(db_column='Code_Type_Formation', primary_key=True, max_length=5)  # Field name made lowercase.
    libelle_type_formation = models.CharField(db_column='Libelle_Type_Formation', max_length=50, blank=True, null=True)  # Field name made lowercase.
    niveau_diplome_max = models.SmallIntegerField(db_column='Niveau_Diplome_Max', blank=True, null=True)  # Field name made lowercase.
    niveau_diplome_min = models.SmallIntegerField(db_column='Niveau_Diplome_Min', blank=True, null=True)  # Field name made lowercase.
    type_diplome = models.SmallIntegerField(db_column='Type_Diplome', blank=True, null=True)  # Field name made lowercase.
    est_bloquer = models.BooleanField(db_column='Est_Bloquer', blank=True, null=True)  # Field name made lowercase.
    user_id = models.CharField(db_column='User_ID', max_length=15, blank=True, null=True)  # Field name made lowercase.
    date_modification = models.DateTimeField(db_column='Date_Modification', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tab_Type_Formation'


class TabTypeProduction(models.Model):
    code_type_production = models.CharField(db_column='Code_Type_Production', primary_key=True, max_length=2)  # Field name made lowercase.
    libelle_type_production = models.CharField(db_column='Libelle_Type_Production', max_length=50, blank=True, null=True)  # Field name made lowercase.
    est_bloquer = models.BooleanField(db_column='Est_Bloquer', blank=True, null=True)  # Field name made lowercase.
    user_id = models.CharField(db_column='User_ID', max_length=15, blank=True, null=True)  # Field name made lowercase.
    date_modification = models.DateTimeField(db_column='Date_Modification', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tab_Type_Production'


class TabTypeRubriques(models.Model):
    code_type = models.CharField(db_column='Code_Type', primary_key=True, max_length=5)  # Field name made lowercase.
    libelle_type_rubrique = models.CharField(db_column='Libelle_Type_Rubrique', max_length=30, blank=True, null=True)  # Field name made lowercase.
    est_bloquer = models.BooleanField(db_column='Est_Bloquer', blank=True, null=True)  # Field name made lowercase.
    user_id = models.CharField(db_column='User_ID', max_length=15, blank=True, null=True)  # Field name made lowercase.
    date_modification = models.DateTimeField(db_column='Date_Modification', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tab_Type_Rubriques'


class TabUniteDeMesure(models.Model):
    code_unite_mesure = models.CharField(db_column='Code_Unite_Mesure', primary_key=True, max_length=4)  # Field name made lowercase.
    symbole_unite = models.CharField(db_column='Symbole_Unite', max_length=10, blank=True, null=True)  # Field name made lowercase.
    libelle_unite = models.CharField(db_column='Libelle_Unite', max_length=50, blank=True, null=True)  # Field name made lowercase.
    est_bloquer = models.BooleanField(db_column='Est_Bloquer', blank=True, null=True)  # Field name made lowercase.
    user_id = models.CharField(db_column='User_ID', max_length=15, blank=True, null=True)  # Field name made lowercase.
    date_modification = models.DateTimeField(db_column='Date_Modification', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tab_Unite_de_Mesure'


class TabUsers(models.Model):
    user = models.OneToOneField(TabAgent, models.DO_NOTHING, db_column='User_ID', primary_key=True)  # Field name made lowercase.
    user_pseudo = models.CharField(db_column='User_Pseudo', max_length=50)  # Field name made lowercase.
    mot_passe = models.CharField(db_column='Mot_Passe', max_length=100)  # Field name made lowercase.
    est_bloquer = models.BooleanField(db_column='Est_Bloquer', blank=True, null=True)  # Field name made lowercase.
    user_creator = models.ForeignKey('self', models.DO_NOTHING, db_column='User_Creator', blank=True, null=True)  # Field name made lowercase.
    date_modification = models.DateTimeField(db_column='Date_Modification', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tab_Users'


class TabVarPaie(models.Model):
    id_var_paie = models.AutoField(db_column='ID_Var_Paie', primary_key=True)  # Field name made lowercase.
    matricule = models.ForeignKey(TabAgent, models.DO_NOTHING, db_column='Matricule')  # Field name made lowercase.
    code_rubrique = models.ForeignKey(TabPlanRubriques, models.DO_NOTHING, db_column='Code_Rubrique')  # Field name made lowercase.
    mmaad = models.DateField(db_column='Mmaad', blank=True, null=True)  # Field name made lowercase.
    mmaaf = models.DateField(db_column='Mmaaf', blank=True, null=True)  # Field name made lowercase.
    base = models.DecimalField(db_column='Base', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    taux = models.FloatField(db_column='Taux', blank=True, null=True)  # Field name made lowercase.
    montant = models.DecimalField(db_column='Montant', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    observation = models.CharField(db_column='Observation', max_length=100, blank=True, null=True)  # Field name made lowercase.
    est_soumis_absence = models.BooleanField(db_column='Est_Soumis_Absence', blank=True, null=True)  # Field name made lowercase.
    mode_saisie = models.SmallIntegerField(db_column='Mode_Saisie', blank=True, null=True)  # Field name made lowercase.
    est_bloquer = models.BooleanField(db_column='Est_Bloquer', blank=True, null=True)  # Field name made lowercase.
    user_id = models.CharField(db_column='User_ID', max_length=15, blank=True, null=True)  # Field name made lowercase.
    date_modification = models.DateTimeField(db_column='Date_Modification', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tab_Var_Paie'
        unique_together = (('matricule', 'code_rubrique', 'mmaad'),)


class TabVarPaieTmp(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    code_rubrique = models.CharField(db_column='Code_Rubrique', max_length=5, blank=True, null=True)  # Field name made lowercase.
    matricule = models.CharField(db_column='Matricule', max_length=15, blank=True, null=True)  # Field name made lowercase.
    mmaad = models.DateField(db_column='Mmaad', blank=True, null=True)  # Field name made lowercase.
    mmaaf = models.DateField(db_column='Mmaaf', blank=True, null=True)  # Field name made lowercase.
    base = models.DecimalField(db_column='Base', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    taux = models.FloatField(db_column='Taux', blank=True, null=True)  # Field name made lowercase.
    montant = models.DecimalField(db_column='Montant', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    observation = models.CharField(db_column='Observation', max_length=100, blank=True, null=True)  # Field name made lowercase.
    est_soumis_absence = models.BooleanField(db_column='Est_Soumis_Absence', blank=True, null=True)  # Field name made lowercase.
    mode_saisie = models.SmallIntegerField(db_column='Mode_Saisie', blank=True, null=True)  # Field name made lowercase.
    est_bloquer = models.BooleanField(db_column='Est_Bloquer', blank=True, null=True)  # Field name made lowercase.
    user_id = models.CharField(db_column='User_ID', max_length=15, blank=True, null=True)  # Field name made lowercase.
    date_modification = models.DateTimeField(db_column='Date_Modification', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tab_Var_Paie_Tmp'


class TabWilaya(models.Model):
    code_wilaya = models.CharField(db_column='Code_Wilaya', primary_key=True, max_length=10)  # Field name made lowercase.
    libelle_wilaya = models.CharField(db_column='Libelle_Wilaya', max_length=50, blank=True, null=True)  # Field name made lowercase.
    est_bloquer = models.BooleanField(db_column='Est_Bloquer', blank=True, null=True)  # Field name made lowercase.
    user_id = models.CharField(db_column='User_ID', max_length=15, blank=True, null=True)  # Field name made lowercase.
    date_modification = models.DateTimeField(db_column='Date_Modification', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tab_Wilaya'


class TypeAvance(models.Model):
    id_type_avance = models.CharField(db_column='Id_Type_Avance', primary_key=True, max_length=3)  # Field name made lowercase.
    libelle = models.CharField(db_column='Libelle', max_length=50)  # Field name made lowercase.
    taux = models.FloatField(db_column='Taux', blank=True, null=True)  # Field name made lowercase.
    est_bloquer = models.BooleanField(db_column='Est_Bloquer', blank=True, null=True)  # Field name made lowercase.
    user_id = models.CharField(db_column='User_ID', max_length=15, blank=True, null=True)  # Field name made lowercase.
    date_modification = models.DateTimeField(db_column='Date_Modification', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Type_Avance'


class TypeCaution(models.Model):
    id_type_caution = models.CharField(db_column='Id_Type_Caution', primary_key=True, max_length=5)  # Field name made lowercase.
    libelle = models.CharField(max_length=50)
    taux_exact = models.FloatField(db_column='Taux_Exact', blank=True, null=True)  # Field name made lowercase.
    taux_min = models.FloatField(db_column='Taux_Min', blank=True, null=True)  # Field name made lowercase.
    taux_max = models.FloatField(db_column='Taux_Max', blank=True, null=True)  # Field name made lowercase.
    type_avance = models.ForeignKey(TypeAvance, models.DO_NOTHING, db_column='Type_Avance', blank=True, null=True)  # Field name made lowercase.
    est_bloquer = models.BooleanField(db_column='Est_Bloquer', blank=True, null=True)  # Field name made lowercase.
    user_id = models.CharField(db_column='User_ID', max_length=15, blank=True, null=True)  # Field name made lowercase.
    date_modification = models.DateTimeField(db_column='Date_Modification', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Type_Caution'


class User(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'User'


class UserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User, models.DO_NOTHING)
    group = models.ForeignKey(Groups, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'User_groups'
        unique_together = (('user', 'group'),)


class UserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User, models.DO_NOTHING)
    permission = models.ForeignKey(Permission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'User_user_permissions'
        unique_together = (('user', 'permission'),)


class ConsolidateDb(models.Model):
    name = models.CharField(primary_key=True, max_length=50)
    active = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'consolidate_db'


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'
