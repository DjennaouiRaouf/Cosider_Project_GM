# Generated by Django 4.2.7 on 2024-04-30 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_sm', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='marche',
            name='est_bloquer',
            field=models.BooleanField(db_column='Est_Bloquer', default=False, editable=False),
        ),
    ]
