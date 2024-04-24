# Generated by Django 4.2.7 on 2024-04-24 08:26

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    dependencies = [
        ('api_sch', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api_sm', '0007_remove_factures_is_remb'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='nt',
            options={'verbose_name': 'NT', 'verbose_name_plural': 'NT'},
        ),
        migrations.AlterField(
            model_name='historicalmarche',
            name='nt',
            field=models.ForeignKey(blank=True, db_column='nt', db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='api_sm.nt', verbose_name='NT'),
        ),
        migrations.AlterField(
            model_name='marche',
            name='nt',
            field=models.ForeignKey(db_column='nt', on_delete=django.db.models.deletion.DO_NOTHING, to='api_sm.nt', verbose_name='NT'),
        ),
        migrations.AlterField(
            model_name='nt',
            name='nt',
            field=models.CharField(db_column='NT', max_length=20, verbose_name='NT'),
        ),
        migrations.CreateModel(
            name='HistoricalDQE',
            fields=[
                ('deleted', models.DateTimeField(db_index=True, editable=False, null=True)),
                ('deleted_by_cascade', models.BooleanField(default=False, editable=False)),
                ('id', models.CharField(db_column='id', db_index=True, editable=False, max_length=500, verbose_name='id')),
                ('code_tache', models.CharField(db_column='Code_Tache', max_length=30, verbose_name='Code de la tache')),
                ('libelle', models.TextField(db_column='Libelle_Tache', verbose_name='Libelle')),
                ('prix_u', models.DecimalField(decimal_places=2, default=0, max_digits=38, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Prix unitaire')),
                ('est_tache_composite', models.BooleanField(blank=True, db_column='Est_Tache_Composite', default=False, verbose_name='Tache composée')),
                ('est_tache_complementaire', models.BooleanField(blank=True, db_column='Est_Tache_Complementaire', default=False, verbose_name='Tache complementaire')),
                ('quantite', models.DecimalField(decimal_places=2, default=0, max_digits=38, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Quantité')),
                ('aug_dim', models.DecimalField(decimal_places=2, default=0, max_digits=38, verbose_name='Augmentation/Diminution')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('marche', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='api_sm.marche', verbose_name='Code du marché')),
                ('unite', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='api_sch.tabunitedemesure', verbose_name='Unité de mesure')),
            ],
            options={
                'verbose_name': 'historical DQE',
                'verbose_name_plural': 'historical DQE',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]