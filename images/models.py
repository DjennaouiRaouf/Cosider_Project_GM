from django.db import models
from django.db.models import Q
from django_currentuser.middleware import get_current_user


# Create your models here.
class GeneralManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(~Q(est_bloquer=True))
    def deleted(self):
        return super().get_queryset().filter(Q(est_bloquer=True))



class DeleteMixin:
    def delete(self, *args, **kwargs):
        self.est_bloquer = True
        self.save()


class ImageLogin(DeleteMixin,models.Model):
    id = models.AutoField(db_column='Id_Img', primary_key=True)
    src = models.ImageField(db_column='Src', upload_to="Img/Login", null=False)
    est_bloquer = models.BooleanField(db_column='Est_Bloquer', editable=False,default=False)
    user_id = models.CharField(db_column='User_ID', max_length=15, editable=False,default=get_current_user)
    date_modification = models.DateTimeField(db_column='Date_Modification', editable=False,auto_now=True)
    objects=GeneralManager()

    class Meta:
        managed = False
        db_table = 'Image_login'
        verbose_name = 'Login'
        verbose_name_plural = 'Login'
