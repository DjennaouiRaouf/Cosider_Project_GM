# Generated by Django 4.2.13 on 2024-05-20 14:19

import django.core.validators
from django.db import migrations, models
import django_currentuser.middleware


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attachements',
            fields=[
                ('id', models.AutoField(db_column='Id_Attachement', primary_key=True, serialize=False)),
                ('code_site', models.CharField(db_column='Code_site', max_length=10, verbose_name='Code du Site')),
                ('nt', models.CharField(db_column='NT', max_length=20, verbose_name='NT')),
                ('code_tache', models.CharField(db_column='Code_Tache', max_length=30, verbose_name='Code Tache')),
                ('qte', models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Quantité Mois')),
                ('prix_u', models.FloatField(default=0, editable=False, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Prix unitaire')),
                ('montant', models.FloatField(default=0, editable=False, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Montant du Mois')),
                ('date', models.DateField(db_column='Mmaa', verbose_name='Date')),
                ('user_id', models.CharField(db_column='User_ID', default=django_currentuser.middleware.get_current_user, editable=False, max_length=15)),
                ('date_modification', models.DateTimeField(auto_now=True, db_column='Date_Modification')),
            ],
            options={
                'verbose_name': 'Attachements',
                'verbose_name_plural': 'Attachements',
                'db_table': 'Attachements',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Avance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_avance', models.PositiveIntegerField(blank=True, default=0, editable=False, verbose_name="Numero d'avance")),
                ('taux_avance', models.FloatField(default=0, editable=False, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name="Taux d'avance")),
                ('montant', models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0)], verbose_name="Montant d'avance")),
                ('debut', models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='Debut')),
                ('fin', models.FloatField(default=80, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='Fin')),
                ('user_id', models.CharField(db_column='User_ID', default=django_currentuser.middleware.get_current_user, editable=False, max_length=15)),
                ('date_modification', models.DateTimeField(auto_now=True, db_column='Date_Modification')),
                ('date', models.DateField(verbose_name="Date d'avance")),
                ('remboursee', models.BooleanField(default=False, verbose_name='Est Remboursée')),
            ],
            options={
                'verbose_name': 'Avance',
                'verbose_name_plural': 'Avances',
                'db_table': 'Avances',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Cautions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_soumission', models.DateField(verbose_name='Date dépot')),
                ('montant', models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Montant')),
                ('est_recupere', models.BooleanField(db_column='Est_Recupere', default=False, verbose_name='Est Recuperée')),
                ('user_id', models.CharField(db_column='User_ID', default=django_currentuser.middleware.get_current_user, editable=False, max_length=15)),
                ('date_modification', models.DateTimeField(auto_now=True, db_column='Date_Modification')),
            ],
            options={
                'verbose_name': 'Caution',
                'verbose_name_plural': 'Caution',
                'db_table': 'Cautions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Clients',
            fields=[
                ('id', models.CharField(db_column='Code_Client', max_length=20, primary_key=True, serialize=False, verbose_name='Code Client')),
                ('type_client', models.SmallIntegerField(blank=True, db_column='Type_Client', null=True, verbose_name='Type Client')),
                ('est_client_cosider', models.BooleanField(blank=True, db_column='Est_Client_Cosider', null=True, verbose_name='Est Client Cosider ?')),
                ('libelle', models.CharField(blank=True, db_column='Libelle_Client', max_length=300, null=True, verbose_name='Libelle')),
                ('nif', models.CharField(blank=True, db_column='NIF', max_length=50, null=True, unique=True, verbose_name='NIF')),
                ('raison_social', models.CharField(blank=True, db_column='Raison_Social', max_length=50, null=True, verbose_name='Raison social')),
                ('num_registre_commerce', models.CharField(blank=True, db_column='Num_Registre_Commerce', max_length=20, null=True, verbose_name='N° Registre Commerce')),
                ('est_bloquer', models.BooleanField(db_column='Est_Bloquer', default=False, editable=False)),
                ('user_id', models.CharField(db_column='User_ID', default=django_currentuser.middleware.get_current_user, editable=False, max_length=15)),
                ('date_modification', models.DateTimeField(auto_now=True, db_column='Date_Modification')),
            ],
            options={
                'verbose_name': 'Clients',
                'verbose_name_plural': 'Clients',
                'db_table': 'Tab_Client',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DetailFacture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(db_column='User_ID', default=django_currentuser.middleware.get_current_user, editable=False, max_length=15)),
                ('date_modification', models.DateTimeField(auto_now=True, db_column='Date_Modification')),
            ],
            options={
                'verbose_name': 'Datails Facture',
                'verbose_name_plural': 'Details Facture',
                'db_table': 'Detail_Facture',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DQE',
            fields=[
                ('code_site', models.CharField(db_column='Code_site', max_length=10, primary_key=True, serialize=False, verbose_name='Code du Site')),
                ('nt', models.CharField(db_column='NT', max_length=20, primary_key=True, verbose_name='NT')),
                ('code_tache', models.CharField(db_column='Code_Tache', max_length=30, primary_key=True, verbose_name='Code Tache')),
                ('libelle', models.TextField(db_column='Libelle_Tache', verbose_name='Libelle')),
                ('prix_u', models.FloatField(db_column='Prix_Unitaire', default=0, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Prix unitaire')),
                ('est_tache_composite', models.BooleanField(blank=True, db_column='Est_Tache_Composite', default=False, verbose_name='Tache composée ?')),
                ('est_tache_complementaire', models.BooleanField(blank=True, db_column='Est_Tache_Complementaire', default=False, verbose_name='Tache complementaire ?')),
                ('quantite', models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Quantité')),
                ('est_bloquer', models.BooleanField(db_column='Est_Bloquer', default=False, editable=False)),
                ('user_id', models.CharField(db_column='User_ID', default=django_currentuser.middleware.get_current_user, editable=False, max_length=15)),
                ('date_modification', models.DateTimeField(auto_now=True, db_column='Date_Modification')),
            ],
            options={
                'verbose_name': 'DQE',
                'verbose_name_plural': 'DQE',
                'db_table': 'Tab_NT_Taches',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DQEAvenant',
            fields=[
                ('code_site', models.CharField(db_column='Code_site', max_length=10, primary_key=True, serialize=False, verbose_name='Code du Site')),
                ('nt', models.CharField(db_column='NT', max_length=20, primary_key=True, verbose_name='NT')),
                ('code_tache', models.CharField(db_column='Code_Tache', max_length=30, primary_key=True, verbose_name='Code Tache')),
                ('num_avenant', models.IntegerField(blank=True, db_column='Num_Avenant', null=True, verbose_name='Avenant N°')),
                ('est_tache_composite', models.BooleanField(blank=True, db_column='Est_Tache_Composite', null=True, verbose_name='Est Composée ?')),
                ('est_tache_complementaire', models.BooleanField(blank=True, db_column='Est_Tache_Complementaire', null=True, verbose_name='Est Complémentaire ?')),
                ('libelle', models.TextField(blank=True, db_column='Libelle_Tache', null=True)),
                ('quantite', models.FloatField(blank=True, db_column='Quantite', null=True)),
                ('prix_u', models.DecimalField(blank=True, db_column='Prix_Unitaire', decimal_places=4, max_digits=19, null=True, verbose_name='Prix Unit')),
                ('est_bloquer', models.BooleanField(blank=True, db_column='Est_Bloquer', null=True)),
                ('user_id', models.CharField(db_column='User_ID', default=django_currentuser.middleware.get_current_user, editable=False, max_length=15)),
                ('date_modification', models.DateTimeField(auto_now=True, db_column='Date_Modification')),
            ],
            options={
                'db_table': 'Tab_NT_Taches_Avenant',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Encaissement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_encaissement', models.DateField(verbose_name="Date d'encaissement")),
                ('montant_encaisse', models.FloatField(blank=True, default=0, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Montant encaissé')),
                ('numero_piece', models.CharField(max_length=300, verbose_name='Numero de piéce')),
                ('user_id', models.CharField(db_column='User_ID', default=django_currentuser.middleware.get_current_user, editable=False, max_length=15)),
                ('date_modification', models.DateTimeField(auto_now=True, db_column='Date_Modification')),
            ],
            options={
                'verbose_name': 'Encaissement',
                'verbose_name_plural': 'Encaissement',
                'db_table': 'Encaissements',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Factures',
            fields=[
                ('numero_facture', models.CharField(db_column='Num_facture', max_length=800, primary_key=True, serialize=False, verbose_name='Numero de facture')),
                ('num_situation', models.IntegerField(db_column='Num_Situation', verbose_name='Numero de situation')),
                ('du', models.DateField(db_column='Date_Debut', verbose_name='Du')),
                ('au', models.DateField(db_column='Date_Fin', verbose_name='Au')),
                ('paye', models.BooleanField(db_column='Paye', default=False, editable=False)),
                ('date', models.DateField(auto_now=True)),
                ('montant', models.FloatField(db_column='Montant_Mois', default=0, editable=False, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Montant du Mois')),
                ('montant_rb', models.FloatField(db_column='Montant_RB', default=0, editable=False, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Montant du rabais')),
                ('montant_rg', models.FloatField(db_column='Montant_RG', default=0, editable=False, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Montant Retenue de garantie')),
                ('user_id', models.CharField(db_column='User_ID', default=django_currentuser.middleware.get_current_user, editable=False, max_length=15)),
                ('date_modification', models.DateTimeField(auto_now=True, db_column='Date_Modification')),
            ],
            options={
                'verbose_name': 'Factures',
                'verbose_name_plural': 'Factures',
                'db_table': 'Factures',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Marche',
            fields=[
                ('id', models.CharField(db_column='Num_Contrat', max_length=500, primary_key=True, serialize=False, verbose_name='Contrat N°')),
                ('num_avenant', models.IntegerField(db_column='Num_Avenant', default=0, editable=False, verbose_name='Avenant N°')),
                ('code_site', models.CharField(db_column='Code_site', max_length=10, verbose_name='Code du Site')),
                ('nt', models.CharField(db_column='NT', max_length=20, verbose_name='NT')),
                ('libelle', models.TextField(verbose_name='Libellé')),
                ('ods_depart', models.DateField(verbose_name='ODS de démarrage')),
                ('delais', models.IntegerField(default=0, null=True, verbose_name='Délai des travaux')),
                ('revisable', models.BooleanField(default=True, verbose_name='Est-il révisable ?')),
                ('delai_paiement_f', models.IntegerField(default=0, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='Délai de paiement')),
                ('rabais', models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='Taux de rabais')),
                ('tva', models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='TVA')),
                ('rg', models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='Taux de retenue de garantie')),
                ('date_signature', models.DateField(verbose_name='Date de signature')),
                ('user_id', models.CharField(db_column='User_ID', default=django_currentuser.middleware.get_current_user, editable=False, max_length=15)),
                ('date_modification', models.DateTimeField(auto_now=True, db_column='Date_Modification')),
            ],
            options={
                'verbose_name': 'Marchés',
                'verbose_name_plural': 'Marchés',
                'db_table': 'Marche',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MarcheAvenant',
            fields=[
                ('id', models.CharField(db_column='Num_Contrat', max_length=500, primary_key=True, serialize=False, verbose_name='Contrat N°')),
                ('num_avenant', models.IntegerField(db_column='Num_Avenant', default=0, editable=False, primary_key=True, verbose_name='Avenant N°')),
                ('code_site', models.CharField(db_column='Code_site', max_length=10, verbose_name='Code du Site')),
                ('nt', models.CharField(db_column='NT', max_length=20, verbose_name='NT')),
                ('libelle', models.TextField(verbose_name='Libellé')),
                ('ods_depart', models.DateField(verbose_name='ODS de démarrage')),
                ('delais', models.IntegerField(default=0, null=True, verbose_name='Délai des travaux')),
                ('revisable', models.BooleanField(default=True, verbose_name='Est-il révisable ?')),
                ('delai_paiement_f', models.IntegerField(default=0, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='Délai de paiement')),
                ('rabais', models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='Taux de rabais')),
                ('tva', models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='TVA')),
                ('rg', models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='Taux de retenue de garantie')),
                ('date_signature', models.DateField(verbose_name='Date de signature')),
                ('user_id', models.CharField(db_column='User_ID', default=django_currentuser.middleware.get_current_user, editable=False, max_length=15)),
                ('date_modification', models.DateTimeField(auto_now=True, db_column='Date_Modification')),
            ],
            options={
                'db_table': 'Marche_Avenant',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ModePaiement',
            fields=[
                ('id', models.AutoField(db_column='Id_Mode', primary_key=True, serialize=False)),
                ('libelle', models.CharField(max_length=500, unique=True)),
                ('user_id', models.CharField(db_column='User_ID', default=django_currentuser.middleware.get_current_user, editable=False, max_length=15)),
                ('date_modification', models.DateTimeField(auto_now=True, db_column='Date_Modification')),
            ],
            options={
                'verbose_name': 'Mode de Paiement',
                'verbose_name_plural': 'Mode de Paiement',
                'db_table': 'Mode_Paiement',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='NT',
            fields=[
                ('code_site', models.CharField(db_column='Code_site', max_length=10, primary_key=True, serialize=False, verbose_name='Code du Site')),
                ('nt', models.CharField(db_column='NT', max_length=20, primary_key=True, verbose_name='NT')),
                ('code_client', models.CharField(db_column='Code_Client', max_length=20, verbose_name='Client')),
                ('libelle', models.TextField(blank=True, db_column='Libelle_NT', null=True, verbose_name='libellé')),
                ('date_ouverture_nt', models.DateField(blank=True, db_column='Date_Ouverture_NT', null=True, verbose_name='Ouverture')),
                ('date_cloture_nt', models.DateField(blank=True, db_column='Date_Cloture_NT', null=True, verbose_name='Cloture')),
                ('est_bloquer', models.BooleanField(db_column='Est_Bloquer', default=False, editable=False)),
                ('user_id', models.CharField(db_column='User_ID', default=django_currentuser.middleware.get_current_user, editable=False, max_length=15)),
                ('date_modification', models.DateTimeField(auto_now=True, db_column='Date_Modification')),
            ],
            options={
                'verbose_name': 'NT',
                'verbose_name_plural': 'NT',
                'db_table': 'Tab_NT',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Remboursement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('montant', models.FloatField(db_column='Montant', default=0, editable=False, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Montant Mois')),
                ('user_id', models.CharField(db_column='User_ID', default=django_currentuser.middleware.get_current_user, editable=False, max_length=15)),
                ('date_modification', models.DateTimeField(auto_now=True, db_column='Date_Modification')),
            ],
            options={
                'verbose_name': 'Remboursement',
                'verbose_name_plural': 'Remboursements',
                'db_table': 'Remboursement',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Sites',
            fields=[
                ('id', models.CharField(db_column='Code_site', max_length=10, primary_key=True, serialize=False, verbose_name='Code Pole')),
                ('code_region', models.CharField(blank=True, choices=[('', ''), ('N', 'Nord'), ('S', 'Sud'), ('W', 'West'), ('E', 'Est'), ('C', 'Centre')], db_column='Code_Region', max_length=1, null=True, verbose_name='Région')),
                ('libelle', models.CharField(blank=True, db_column='Libelle_Site', max_length=150, null=True, verbose_name='Libellé')),
                ('type_site', models.SmallIntegerField(blank=True, db_column='Type_Site', null=True, verbose_name='Type du Site')),
                ('code_commune_site', models.CharField(blank=True, db_column='Code_Commune_Site', max_length=10, null=True, verbose_name='Code Commune')),
                ('jour_cloture_mouv_rh_paie', models.CharField(blank=True, db_column='Jour_Cloture_Mouv_RH_Paie', max_length=2, null=True)),
                ('date_ouverture_site', models.DateField(blank=True, db_column='Date_Ouverture_Site', null=True, verbose_name='Date Ouverture')),
                ('date_cloture_site', models.DateField(blank=True, db_column='Date_Cloture_Site', null=True, verbose_name='Date Cloture')),
                ('est_bloquer', models.BooleanField(db_column='Est_Bloquer', default=False, editable=False)),
                ('user_id', models.CharField(db_column='User_ID', default=django_currentuser.middleware.get_current_user, editable=False, max_length=15)),
                ('date_modification', models.DateTimeField(auto_now=True, db_column='Date_Modification')),
            ],
            options={
                'verbose_name': 'Sites',
                'verbose_name_plural': 'Sites',
                'db_table': 'Tab_Site',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TypeAvance',
            fields=[
                ('id', models.AutoField(db_column='Id_Type_Avance', primary_key=True, serialize=False)),
                ('libelle', models.CharField(db_column='Libelle', max_length=500, unique=True)),
                ('taux_max', models.FloatField(db_column='Taux', default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('user_id', models.CharField(db_column='User_ID', default=django_currentuser.middleware.get_current_user, editable=False, max_length=15)),
                ('date_modification', models.DateTimeField(auto_now=True, db_column='Date_Modification')),
            ],
            options={
                'verbose_name': 'Type Avance',
                'verbose_name_plural': 'Type Avance',
                'db_table': 'TypeAvance',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TypeCaution',
            fields=[
                ('id', models.AutoField(db_column='Id_Type_Caution', primary_key=True, serialize=False)),
                ('libelle', models.CharField(blank=True, max_length=500, null=True)),
                ('taux_exact', models.FloatField(blank=True, db_column='Taux_Exact', null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('taux_min', models.FloatField(blank=True, db_column='Taux_Min', null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('taux_max', models.FloatField(blank=True, db_column='Taux_Max', null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('user_id', models.CharField(db_column='User_ID', default=django_currentuser.middleware.get_current_user, editable=False, max_length=15)),
                ('date_modification', models.DateTimeField(auto_now=True, db_column='Date_Modification')),
            ],
            options={
                'verbose_name': 'Type_Caution',
                'verbose_name_plural': 'Type_Caution',
                'db_table': 'Type_Caution',
                'managed': False,
            },
        ),
    ]
