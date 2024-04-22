import django_filters
from django.db.models import Q
from django.db.models.functions import ExtractMonth, ExtractYear

from api_sch.models import *
class ProdFilter(django_filters.FilterSet):
    mm = django_filters.NumberFilter(field_name='mmaa__month', label='Mois')
    aa = django_filters.NumberFilter(field_name='mmaa__year', label='Année')

    class Meta:
        model = TabProduction
        fields = ['code_site','prevu_realiser','nt','code_type_production'] # 01




class UMFilter(django_filters.FilterSet):
    class Meta:
        model = TabUniteDeMesure
        fields=['id',]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field_instance in self.base_filters.items():
            try:
                model_field = self.Meta.model._meta.get_field(field_name)
                field_instance.label = model_field.verbose_name
            except:
                pass