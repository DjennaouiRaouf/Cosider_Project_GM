import django_filters
from django.db.models import Q

from api_sm.models import *


class ClientsFilter(django_filters.FilterSet):
    class Meta:
        model = Clients
        fields = ['id','type_client','est_client_cosider']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field_instance in self.base_filters.items():
            try:
                model_field = self.Meta.model._meta.get_field(field_name)
                field_instance.label = model_field.verbose_name
            except:
                pass


class SitesFilter(django_filters.FilterSet):
    class Meta:
        model = Sites
        fields = ['id', 'type_site','code_filiale','code_division','code_commune_site','code_region']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field_instance in self.base_filters.items():
            try:
                model_field = self.Meta.model._meta.get_field(field_name)
                field_instance.label = model_field.verbose_name
            except:
                pass


class NTFilter(django_filters.FilterSet):
    nt=django_filters.CharFilter(field_name='nt',label='NT')
    code_site=django_filters.ModelChoiceFilter(field_name="code_site",queryset=Sites.objects.all(),label='Site')
    code_client=django_filters.ModelChoiceFilter(field_name='code_client',queryset=Clients.objects.all(),label='Client')
    situation=django_filters.ModelChoiceFilter(field_name='code_situation_nt',queryset=TabSituationNt.objects.all(),label='Situation')
    class Meta:
        model = NT
        fields=['nt','code_site','code_client',]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field_instance in self.base_filters.items():
            try:
                model_field = self.Meta.model._meta.get_field(field_name)
                field_instance.label = model_field.verbose_name
            except:
                pass


class MarcheFilter(django_filters.FilterSet):
    code_site = django_filters.ModelChoiceFilter(field_name='code_site', label='Code du site',
                                                 queryset=Sites.objects.all(),)
    code_contrat = django_filters.CharFilter(field_name='id', label='Code du contrat')
    date_signature=django_filters.DateFilter(field_name="date_signature",label='Date de signature')
    nt = django_filters.CharFilter(field_name='nt', label='Numero du travail')
    client=django_filters.BooleanFilter(field_name='nt__code_client__est_client_cosider', label='Cosider client')
    has_rg = django_filters.BooleanFilter(field_name='rg', label='Avec retenue de garantie ?',method='filter_has_rg',)
    has_tva = django_filters.BooleanFilter(field_name='tva', label='Avec TVA ?',method='filter_has_tva',)
    has_rabais = django_filters.BooleanFilter(field_name='rabais', label='Avec Rabais ? ',method='filter_has_rabais',)

    def filter_has_rabais(self, queryset, name, value):
        if value is False:
            return queryset.filter(**{f"{name}__exact": 0})  
        elif value is True:
            return queryset.exclude(**{f"{name}__exact": 0})  
        return queryset
    def filter_has_tva(self, queryset, name, value):
        if value is False:
            return queryset.filter(**{f"{name}__exact": 0})  
        elif value is True:
            return queryset.exclude(**{f"{name}__exact": 0})  
        return queryset
    def filter_has_rg(self, queryset, name, value):
        if value is False:
            return queryset.filter(**{f"{name}__exact": 0})  
        elif value is True:
            return queryset.exclude(**{f"{name}__exact": 0})  
        return queryset
    class Meta:
        model = Marche
        fields=['code_contrat','date_signature','code_site','client','nt','tva','rg','rabais','has_rg','has_tva',]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field_instance in self.base_filters.items():
            try:
                model_field = self.Meta.model._meta.get_field(field_name)
                field_instance.label = model_field.verbose_name
            except:
                pass


class DQEFilter(django_filters.FilterSet):
    nt = django_filters.CharFilter(field_name='nt', label='NT')
    code_site = django_filters.ModelChoiceFilter(field_name="code_site", queryset=Sites.objects.all(), label='Site')
    code_tache= django_filters.CharFilter(field_name='code_tache', label='Code Tache')

    class Meta:
        model = DQE
        fields=['code_tache','code_site','nt']


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field_instance in self.base_filters.items():
            try:
                model_field = self.Meta.model._meta.get_field(field_name)
                field_instance.label = model_field.verbose_name
            except:
                pass


class FactureFilter(django_filters.FilterSet):
    code_site=django_filters.CharFilter(field_name='marche__code_site')
    nt = django_filters.CharFilter(field_name='marche__nt')

    numero_facture=django_filters.CharFilter(field_name='numero_facture',label='N° Facture')
    num_situation=django_filters.NumberFilter(field_name='num_situation',label='N° Situation')
    paye=django_filters.BooleanFilter(field_name='paye',label='Est Payée')
    class Meta:
        model = Factures
        fields=['code_site','nt','numero_facture','num_situation','paye',]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field_instance in self.base_filters.items():
            try:
                model_field = self.Meta.model._meta.get_field(field_name)
                field_instance.label = model_field.verbose_name
            except:
                pass


class EncaissementFilter(django_filters.FilterSet):
    class Meta:
        model = Encaissement
        fields=['date_encaissement','mode_paiement','facture','facture__marche']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field_instance in self.base_filters.items():
            try:
                model_field = self.Meta.model._meta.get_field(field_name)
                field_instance.label = model_field.verbose_name
            except:
                pass




class MPFilter(django_filters.FilterSet):
    class Meta:
        model = ModePaiement
        fields=['id',]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field_instance in self.base_filters.items():
            try:
                model_field = self.Meta.model._meta.get_field(field_name)
                field_instance.label = model_field.verbose_name
            except:
                pass


class DetailFactureFilter(django_filters.FilterSet):
    code_tache = django_filters.CharFilter(field_name='detail__dqe__code_tache', lookup_expr='icontains',label="Code Tache")
    libelle_tache = django_filters.CharFilter(field_name='detail__dqe__libelle', lookup_expr='icontains',label="Libelle")

    class Meta:
        model = DetailFacture
        fields = ['facture','code_tache','libelle_tache' ]


class AvanceFilter(django_filters.FilterSet):

    class Meta:
        model = Avance
        fields=['marche__nt','marche__code_site','remboursee']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field_instance in self.base_filters.items():
            try:
                model_field = self.Meta.model._meta.get_field(field_name)
                field_instance.label = model_field.verbose_name
            except:
                pass


class CautionFilter(django_filters.FilterSet):

    class Meta:
        model = Cautions
        fields=['marche',]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field_instance in self.base_filters.items():
            try:
                model_field = self.Meta.model._meta.get_field(field_name)
                field_instance.label = model_field.verbose_name
            except:
                pass


class Ordre_De_ServiceFilter(django_filters.FilterSet):

    class Meta:
        model = Ordre_De_Service
        fields=['marche','date','rep_int']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field_instance in self.base_filters.items():
            try:
                model_field = self.Meta.model._meta.get_field(field_name)
                field_instance.label = model_field.verbose_name
            except:
                pass


class TypeAvanceFilter(django_filters.FilterSet):
    class Meta:
        model = TypeAvance
        fields=['id',]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field_instance in self.base_filters.items():
            try:
                model_field = self.Meta.model._meta.get_field(field_name)
                field_instance.label = model_field.verbose_name
            except:
                pass


class TypeCautionFilter(django_filters.FilterSet):
    class Meta:
        model = TypeCaution
        fields=['id',]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field_instance in self.base_filters.items():
            try:
                model_field = self.Meta.model._meta.get_field(field_name)
                field_instance.label = model_field.verbose_name
            except:
                pass


class AttachementsFilter(django_filters.FilterSet):
    code_tache = django_filters.CharFilter(field_name='code_tache', label="Code Tache")
    code_site = django_filters.CharFilter(field_name='code_site', label="Code Pole")
    mm = django_filters.NumberFilter(field_name='date__month', label='Mois')
    aa = django_filters.NumberFilter(field_name='date__year', label='Année')
    class Meta:
        model = Attachements
        fields=['nt','code_tache','code_site',]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field_instance in self.base_filters.items():
            try:
                model_field = self.Meta.model._meta.get_field(field_name)
                field_instance.label = model_field.verbose_name
            except:
                pass


class WorkStateFilter(django_filters.FilterSet):
    marche = django_filters.CharFilter(field_name='dqe__marche', label="Marche")
    date = django_filters.DateFromToRangeFilter(field_name='date', label='Date')

    class Meta:
        model = Attachements
        fields=['marche','date']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field_instance in self.base_filters.items():
            try:
                model_field = self.Meta.model._meta.get_field(field_name)
                field_instance.label = model_field.verbose_name
            except:
                pass



class ECFilter(django_filters.FilterSet):
    code_contrat = django_filters.CharFilter(field_name='id', label='Code du contrat')
    has_creance = django_filters.BooleanFilter(field_name='mgc', label='Avec Creances ? ', method='filter_has_creance', )
    has_invoice = django_filters.BooleanFilter(field_name='mgf', label='Ayant facturé ? ', method='filter_has_invoice', )
    client = django_filters.ModelChoiceFilter(field_name='nt__code_client',queryset=Clients.objects.all(),label='Client')
    def filter_has_creance(self, queryset, name, value):

        if value is False:
            ids = [obj.id for obj in queryset if (obj.montant_global_c <= 0) ]
            return queryset.filter(id__in=ids)
        elif value is True:
            ids = [obj.id for obj in queryset if (obj.montant_global_c > 0)]
            return queryset.filter(id__in=ids)

        return queryset

    def filter_has_invoice(self, queryset, name, value):

        if value is False:
            ids = [obj.id for obj in queryset if (obj.montant_global_f <= 0)]
            return queryset.filter(id__in=ids)
        elif value is True:
            ids = [obj.id for obj in queryset if (obj.montant_global_f > 0)]
            return queryset.filter(id__in=ids)
        return queryset


    class Meta:
        model = Marche
        fields=['code_contrat','has_creance','client','has_invoice']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field_instance in self.base_filters.items():
            try:
                model_field = self.Meta.model._meta.get_field(field_name)
                field_instance.label = model_field.verbose_name
            except:
                pass