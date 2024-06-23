# Generated by Django 4.2.13 on 2024-06-23 12:01

from django.db import migrations, models
import django_currentuser.middleware


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ImageLogin',
            fields=[
                ('id', models.AutoField(db_column='Id_Img', primary_key=True, serialize=False)),
                ('src', models.ImageField(db_column='Src', upload_to='Img/Login')),
                ('est_bloquer', models.BooleanField(db_column='Est_Bloquer', default=False, editable=False)),
                ('user_id', models.CharField(db_column='User_ID', default=django_currentuser.middleware.get_current_user, editable=False, max_length=15)),
                ('date_modification', models.DateTimeField(auto_now=True, db_column='Date_Modification')),
            ],
            options={
                'verbose_name': 'Login',
                'verbose_name_plural': 'Login',
                'db_table': 'Image_login',
                'managed': False,
            },
        ),
    ]
