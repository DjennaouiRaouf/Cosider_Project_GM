import django_filters
from django.db.models import Q
from django.db.models.functions import ExtractMonth, ExtractYear

from api_sch.models import *
from api_sm.models import Marche


class ProdFilter(django_filters.FilterSet):
    mm = django_filters.NumberFilter(field_name='mmaa__month', label='Mois')
    aa = django_filters.NumberFilter(field_name='mmaa__year', label='Année')
    dqe=django_filters.CharFilter(field_name='code_tache',label='DQE',method='filter_dqe')

    def filter_dqe(self, queryset, name, value):
        nt=self.data.get('nt')
        cs=self.data.get('code_site')

        m=Marche.objects.get(nt__nt=nt,nt__code_site=cs)
        dqe_id=self.data.get('dqe')+'_'+m.id
        if(dqe_id):
            return queryset.filter(code_tache=dqe_id)
        else:
            return queryset


    class Meta:
        model = TabProduction
        fields = ['code_site','prevu_realiser','nt','code_type_production'] # 01

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field_instance in self.base_filters.items():
            try:
                model_field = self.Meta.model._meta.get_field(field_name)
                field_instance.label = model_field.verbose_name
            except:
                pass



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