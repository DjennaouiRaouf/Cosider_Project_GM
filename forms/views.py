from django.db.models import IntegerField
from django.db.models.functions import Cast
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api_sch.Filters import ProdFilter
from api_sch.Serializers import ProductionSerializer
from api_sch.models import TabUniteDeMesure, TabProduction
from api_sm.Filters import *
from api_sm.Serializers import *


# Create your views here.


class UserFieldsApiView(APIView):
    def get(self, request):

        serializer = UserSerializer()
        fields = serializer.get_fields()
        field_info = []
        for field_name, field_instance in fields.items():
            obj = {
                    'name': field_name,
                        'type': str(field_instance.__class__.__name__),
                        "required": field_instance.required,
                        'label': field_instance.label or field_name,
                'required': True,
                }
            field_info.append(obj)
            if (field_name == "password"):
                field_info.append({
                    'name': 'confirme' + field_name,
                    'required':True,
                    'type': str(field_instance.__class__.__name__),
                    'label': 'Confirmer le mot de passe',
                })
        return Response({'fields': field_info},
                        status=status.HTTP_200_OK)

class UserFieldsStateApiView(APIView):
    def get(self, request):
        serializer = UserSerializer()
        fields = serializer.get_fields()
        field_info = []
        for field_name, field_instance in fields.items():
            default_value = None
            field_info.append({
                field_name:default_value ,

            })
            state = {}

            for d in field_info:
                state.update(d)
        return Response({'state': state}, status=status.HTTP_200_OK)




class DQEFieldsFilterApiView(APIView):
    def get(self,request):
        field_info=[]
        for field_name, field_instance in DQEFilter.base_filters.items():
            if(field_name not in ['marche','nt','code_site']):
                obj = {
                            'name': field_name,
                            'type': str(field_instance.__class__.__name__),
                            'label': field_instance.label or field_name,
                }
                field_info.append(obj)

        return Response({'fields': field_info},status=status.HTTP_200_OK)


class DQEFieldsStateApiView(APIView):
    def get(self, request):
        serializer = DQESerializer()
        fields = serializer.get_fields()
        field_info = []
        nt = request.query_params.get('nt', None)
        cs = request.query_params.get('cs', None)
        ct = request.query_params.get('ct', None)

        if nt and cs and ct:
            dqe = DQE.objects.get(nt=nt,code_tache=ct,code_site=cs)
            print(dqe.libelle)
        else:
            dqe = None
        if(dqe == None):

            for field_name, field_instance in fields.items():
                if (not field_name in ['prix_q','id','pole','nt']):
                    default_value = None
                    if str(field_instance.__class__.__name__) == 'PrimaryKeyRelatedField':
                        default_value = []
                    if str(field_instance.__class__.__name__) == 'BooleanField':
                        default_value= False
                    if str(field_instance.__class__.__name__) in ['PositiveSmallIntegerField','DecimalField','PositiveIntegerField',
                                                                  'IntegerField',]:
                        default_value = 0

                    field_info.append({
                        field_name:default_value ,

                    })
                    state = {}

                    for d in field_info:
                        state.update(d)
        else:
            update_dqe=DQESerializer(dqe).data
            for field_name, field_instance in fields.items():
                if(not field_name in ['prix_q','id'] ):
                    if(field_name in ['prix_u','quantite']):
                        default_value = update_dqe[field_name]

                    else:

                        default_value = update_dqe[field_name]
                    field_info.append({
                        field_name:default_value ,

                    })
                    state = {}

                    for d in field_info:
                        state.update(d)

            unite=TabUniteDeMesure.objects.get(libelle=state['unite'])
            state['unite']=[{'value':unite.id,'label':unite.libelle}]

        return Response({'state': state}, status=status.HTTP_200_OK)

class DQEFieldsApiView(APIView):
    def get(self, request):
        flag = request.query_params.get('flag',None)
        if flag=='l' or flag =='f':
            serializer = DQESerializer()
            model_class = serializer.Meta.model
            model_name = model_class.__name__
            fields = serializer.get_fields()

            if(flag=='f'): # react form
                field_info = []
                for field_name, field_instance in fields.items():

                    if (field_name not in ['prix_q','id','pole','nt']):

                        if( field_name in ['prix_u','quantite']):
                            readOnly=False
                        else:
                            readOnly = True
                        obj = {
                            'name': field_name,
                            'type': str(field_instance.__class__.__name__),
                            "required": field_instance.required,
                            'label': field_instance.label or field_name,
                            'readOnly': readOnly
                        }
                        if (str(field_instance.style.get("base_template")).find('textarea') != -1):
                            obj['textarea'] = True

                        if (str(field_instance.__class__.__name__) == "PrimaryKeyRelatedField"):
                            anySerilizer = create_dynamic_serializer(field_instance.queryset.model)
                            serialized_data = anySerilizer(field_instance.queryset, many=True).data
                            filtered_data = []
                            for item in serialized_data:
                                filtered_item = {
                                    'value': item['id'],
                                    'label': item['libelle']
                                }
                                filtered_data.append(filtered_item)

                            obj['queryset'] = filtered_data

                        field_info.append(obj)

            if(flag=='l'): #data grid list (react ag-grid)
                field_info = []
                for field_name, field_instance in fields.items():
                    if(field_name not in ['',]):
                        obj = {
                            'field': field_name,
                            'headerName': field_instance.label or field_name,
                            'info': str(field_instance.__class__.__name__),

                        }
                        if( field_name in ['pole','nt']):
                            obj['hide'] = True
                        if (str(field_instance.__class__.__name__) == "PrimaryKeyRelatedField") and field_name not in ['marche']:
                            obj['related'] = str(field_instance.queryset.model.__name__)
                        if(field_name in ['prix_u','prix_q','quantite']):
                            obj['cellRenderer']='InfoRenderer'

                        field_info.append(obj)


            return Response({'fields':field_info,'models':model_name,'pk':DQE._meta.pk.name},status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        return Response(status=status.HTTP_400_BAD_REQUEST)




class MarcheFieldsFilterApiView(APIView):
    def get(self,request):
        field_info = []

        for field_name, field_instance  in MarcheFilter.base_filters.items():


            obj = {
                'name': field_name,
                'type': str(field_instance.__class__.__name__),
                'label': field_instance.label or field_name,

            }
            if str(field_instance.__class__.__name__) == 'ModelChoiceFilter':
                anySerilizer = create_dynamic_serializer(field_instance.queryset.model)
                serialized_data = anySerilizer(field_instance.queryset, many=True).data
                filtered_data = []
                for item in serialized_data:
                    if(field_name in ['code_site']):
                        filtered_item = {
                            'value': item['id'],
                            'label': item['id']
                        }
                    else:
                        filtered_item = {
                            'value': item['id'],
                            'label': item['libelle'] or item['id']
                        }
                    filtered_data.append(filtered_item)

                obj['queryset'] = filtered_data



            field_info.append(obj)

        return Response({'fields': field_info},status=status.HTTP_200_OK)



class MarcheFieldsStateApiView(APIView):
    def get(self, request):
        serializer = MarcheSerializer()
        fields = serializer.get_fields()
        field_info = []
        marche_pk = request.query_params.get('id', None)
        if marche_pk:
            marche = Marche.objects.get(pk=marche_pk)
        else:
            marche = None
        if(marche == None):

            for field_name, field_instance in fields.items():
                if (field_name not in ['id', 'montant_ht', 'montant_ttc','num_avenant']):
                    default_value = None
                    if (str(field_instance.__class__.__name__) == "PrimaryKeyRelatedField"):
                        default_value =[]

                    if str(field_instance.__class__.__name__) == 'BooleanField':
                        default_value= False
                    if str(field_instance.__class__.__name__) in ['PositiveSmallIntegerField','DecimalField','PositiveIntegerField',
                                                                  'IntegerField','FloatField']:
                        default_value = 0

                    field_info.append({
                        field_name:default_value ,

                    })
                    state = {}

                    for d in field_info:
                        state.update(d)
            return Response({'state': state}, status=status.HTTP_200_OK)

        else:
            update_marche=MarcheSerializer(marche).data
            for field_name, field_instance in fields.items():

                    default_value = update_marche[field_name]
                    field_info.append({
                        field_name:default_value ,

                    })
                    state = {}


                    for d in field_info:
                        state.update(d)

            s=Sites.objects.get(id=state['code_site'])

            state['code_site']=[{'value':s.id,'label':s.libelle}]

        return Response({'state': state}, status=status.HTTP_200_OK)


class MarcheFieldsApiView(APIView):
    def get(self, request):
        flag = request.query_params.get('flag',None)
        if flag=='l' or flag =='f':
            serializer = MarcheSerializer()
            fields = serializer.get_fields()
            model_class = serializer.Meta.model
            model_name = model_class.__name__

            if(flag=='f'): # react form

                field_info = []
                for field_name, field_instance in fields.items():

                    if(field_name not in ['montant_ht','montant_ttc','num_avenant']):

                        if (field_name in ['id','nt','code_site',"libelle"]):
                            readOnly = True
                        else:
                            readOnly = False



                        obj={
                            'name':field_name,
                            'type': str(field_instance.__class__.__name__),
                            "required": field_instance.required,
                            'label': field_instance.label or field_name,
                            'source':field_instance.source,
                            'readOnly': readOnly
                        }

                        if (str(field_instance.style.get("base_template")).find('textarea') != -1):
                            obj['textarea'] = True


                        if (str(field_instance.__class__.__name__) == "PrimaryKeyRelatedField"):
                            anySerilizer = create_dynamic_serializer(field_instance.queryset.model)
                            serialized_data = anySerilizer(field_instance.queryset, many=True).data
                            filtered_data = []
                            for item in serialized_data:
                                if (field_name in ['code_site']):
                                    filtered_item = {
                                        'value': item['id'],
                                        'label': item['id']
                                    }
                                else:
                                    filtered_item = {
                                        'value': item['id'],
                                        'label': item['libelle'] or item['id']
                                    }
                                filtered_data.append(filtered_item)

                            obj['queryset'] = filtered_data

                        field_info.append(obj)

            if(flag=='l'): #data grid list (react ag-grid)
                field_info = []
                for field_name, field_instance in fields.items():

                    obj={
                        'field': field_name,
                        'headerName': field_instance.label or field_name,
                        'info': str(field_instance.__class__.__name__),

                    }


                    if (field_name in ['rg','rabais','tva', 'montant_ttc', 'montant_ht']):
                        obj['cellRenderer'] = 'InfoRenderer'

                    field_info.append(obj)
            return Response({'fields':field_info,'models':model_name,'pk':Marche._meta.pk.name},status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        return Response(status=status.HTTP_400_BAD_REQUEST)



class ECFieldsFilterApiView(APIView):
    def get(self,request):
        field_info = []

        for field_name, field_instance  in ECFilter.base_filters.items():


            obj = {
                'name': field_name,
                'type': str(field_instance.__class__.__name__),
                'label': field_instance.label or field_name,

            }
            if str(field_instance.__class__.__name__) == 'ModelChoiceFilter':
                print(field_instance.queryset.model)
                anySerilizer = create_dynamic_serializer(field_instance.queryset.model)
                serialized_data = anySerilizer(field_instance.queryset, many=True).data
                filtered_data = []
                for item in serialized_data:
                    filtered_item = {
                        'value': item['id'],
                        'label': item['libelle']
                    }
                    filtered_data.append(filtered_item)

                obj['queryset'] = filtered_data



            field_info.append(obj)

        return Response({'fields': field_info},status=status.HTTP_200_OK)




class EtatCreancesfields(APIView):
    def get(self, request):

        serializer = ECSerializer()
        fields = serializer.get_fields()
        model_class = serializer.Meta.model
        model_name = model_class.__name__
        field_info = []
        for field_name, field_instance in fields.items():
            if(field_name in ['id','code_site','nt','client','mgf','mgp','mgc']):
                obj={
                            'field': field_name,
                            'headerName': field_instance.label or field_name,
                            'info': str(field_instance.__class__.__name__),
                }
                if(field_name in ['mgf','mgp','mgc']):
                    obj['cellRenderer'] = 'InfoRenderer'


                field_info.append(obj)
        return Response({'fields':field_info,'models':model_name,'pk':Marche._meta.pk.name},status=status.HTTP_200_OK)



class ClientFieldsFilterApiView(APIView):
    def get(self,request):
        filter_fields = list(ClientsFilter.base_filters.keys())
        serializer = ClientsSerializer()
        fields = serializer.get_fields()
        field_info = []
        for field_name, field_instance in fields.items():
            if field_name in filter_fields:
                field_info.append({
                    'name': field_name,
                    'type': str(field_instance.__class__.__name__),

                    'label': field_instance.label or field_name,
                })

        return Response({'fields': field_info},status=status.HTTP_200_OK)


class ClientFieldsStateApiView(APIView):
    def get(self, request):
        serializer = ClientsSerializer()
        fields = serializer.get_fields()
        field_info = []
        for field_name, field_instance in fields.items():
            default_value = None
            if str(field_instance.__class__.__name__) == 'PrimaryKeyRelatedField':
                default_value= []
            if str(field_instance.__class__.__name__) == 'BooleanField':
                default_value= False
            if str(field_instance.__class__.__name__) in ['PositiveSmallIntegerField','DecimalField','PositiveIntegerField',
                                                          'IntegerField',]:
                default_value = 0

            field_info.append({
                field_name:default_value ,

            })
            state = {}

            for d in field_info:
                state.update(d)
        return Response({'state': state}, status=status.HTTP_200_OK)

class ClientFieldsApiView(APIView):
        def get(self, request):
            flag = request.query_params.get('flag', None)
            if flag == 'l' or flag == 'f':
                serializer = ClientsSerializer()
                fields = serializer.get_fields()
                model_class = serializer.Meta.model
                model_name = model_class.__name__
                if (flag == 'f'):  # react form
                    field_info = []
                    for field_name, field_instance in fields.items():
                        field_info.append({
                            'name': field_name,
                            'type': str(field_instance.__class__.__name__),
                            "required": field_instance.required,
                            'label': field_instance.label or field_name,
                        })
                if (flag == 'l'):  # data grid list (react ag-grid)
                    field_info = []
                    for field_name, field_instance in fields.items():

                        field_info.append({
                            'field': field_name,
                            'headerName': field_instance.label or field_name,
                            'info': str(field_instance.__class__.__name__),
                        })

                return Response({'fields': field_info,'models':model_name,'pk':Clients._meta.pk.name}, status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)

            return Response(status=status.HTTP_400_BAD_REQUEST)



class SiteFieldsStateApiView(APIView):
    def get(self, request):
        serializer = SiteSerializer()
        fields = serializer.get_fields()
        field_info = []
        for field_name, field_instance in fields.items():

            default_value = None
            if str(field_instance.__class__.__name__) == 'ChoiceField':
                default_value= ''
            if str(field_instance.__class__.__name__) == 'PrimaryKeyRelatedField':
                default_value= False
            if str(field_instance.__class__.__name__) == 'BooleanField':
                default_value= False
            if str(field_instance.__class__.__name__) in ['PositiveSmallIntegerField','DecimalField','PositiveIntegerField',
                                                          'IntegerField',]:
                default_value = 0

            field_info.append({
                field_name:default_value ,

            })
            state = {}

            for d in field_info:
                state.update(d)

        state['code_filiale']=TabFiliale.objects.first().id
        return Response({'state': state}, status=status.HTTP_200_OK)



class SiteFieldsFilterApiView(APIView):
    def get(self,request):
        filter_fields = list(SitesFilter.base_filters.keys())
        serializer = SiteSerializer()
        fields = serializer.get_fields()
        field_info = []
        for field_name, field_instance in fields.items():
            if field_name in filter_fields:
                field_info.append({
                    'name': field_name,
                    'type': str(field_instance.__class__.__name__),

                    'label': field_instance.label or field_name,
                })

        return Response({'fields': field_info},status=status.HTTP_200_OK)
class SiteFieldsApiView(APIView):
    def get(self, request):
        flag = request.query_params.get('flag', None)
        if flag == 'l' or flag == 'f':
            serializer = SiteSerializer()
            fields = serializer.get_fields()
            if (flag == 'f'):  # react form
                field_info = []
                obj = {}
                for field_name, field_instance in fields.items():
                    if(field_name not in ['code_filiale']):
                        obj={
                            'name': field_name,
                            'type': str(field_instance.__class__.__name__),
                            "required": field_instance.required,
                            'label': field_instance.label or field_name,
                        }
                        try:

                            if field_instance.choices:
                                obj['choices']= [{'key': key, 'value': value} for key, value in dict(field_instance.choices).items()]
                        except:
                            pass

                        if (str(field_instance.style.get("base_template")).find('textarea') != -1):
                            obj['textarea'] = True
                        if (str(field_instance.__class__.__name__) == "PrimaryKeyRelatedField"):
                            anySerilizer = create_dynamic_serializer(field_instance.queryset.model)
                            serialized_data = anySerilizer(field_instance.queryset, many=True).data
                            filtered_data = []
                            for item in serialized_data:
                                filtered_item = {
                                    'value': item['id'],
                                    'label': item['libelle']
                                }
                                filtered_data.append(filtered_item)

                            obj['queryset'] = filtered_data
                        field_info.append(obj)
            if (flag == 'l'):  # data grid list (react ag-grid)
                field_info = []
                for field_name, field_instance in fields.items():
                    field_info.append({
                        'field': field_name,
                        'headerName': field_instance.label or field_name,
                        'info': str(field_instance.__class__.__name__),
                    })

            return Response({'fields': field_info}, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        return Response(status=status.HTTP_400_BAD_REQUEST)


class NTFieldsFilterApiView(APIView):
    def get(self,request):
        field_info = []
        marche = request.query_params.get('marche', None)
        for field_name, field_instance in NTFilter.base_filters.items():
            if (field_name not in ['']):

                obj = {
                    'name': field_name,
                    'type': str(field_instance.__class__.__name__),
                    'label': field_instance.label or field_name,

                }
                if str(field_instance.__class__.__name__) == 'ModelChoiceFilter':

                    anySerilizer = create_dynamic_serializer(field_instance.queryset.model)
                    serialized_data = anySerilizer(field_instance.queryset,
                                                           many=True).data
                    filtered_data = []
                    for item in serialized_data:
                        filtered_item = {
                                'value': item['id'],
                                'label': item['libelle'] or item['id']
                        }
                        filtered_data.append(filtered_item)

                        obj['queryset'] = filtered_data

                field_info.append(obj)

        return Response({'fields': field_info}, status=status.HTTP_200_OK)


class NTFieldsApiView(APIView):
    def get(self, request):
        flag = request.query_params.get('flag', None)
        if flag == 'l' or flag == 'f':
            serializer = NTSerializer()
            fields = serializer.get_fields()
            model_class = serializer.Meta.model
            model_name = model_class.__name__


            if (flag == 'f'):  # react form
                field_info = []

                for field_name, field_instance in fields.items():
                    if (field_name not in ['']):
                        obj = {
                            'name': field_name,
                            'type': str(field_instance.__class__.__name__),
                            "required": field_instance.required,
                            'label': field_instance.label or field_name,

                        }

                        if( field_name in ['site','nt']):
                            readOnly=True
                        else:
                            readOnly = False

                        if (str(field_instance.style.get("base_template")).find('textarea') != -1):
                            obj['textarea'] = True

                        obj['readOnly']=readOnly
                        if (str(field_instance.__class__.__name__) == "PrimaryKeyRelatedField"):
                            anySerilizer = create_dynamic_serializer(field_instance.queryset.model)
                            serialized_data = anySerilizer(field_instance.queryset, many=True).data
                            filtered_data = []
                            for item in serialized_data:
                                if(field_name in ['site',]):
                                    filtered_item = {
                                        'value': item['id'],
                                        'label': item['id']
                                    }
                                else:
                                    filtered_item = {
                                        'value': item['id'],
                                        'label': item['libelle'] or item['id']
                                    }
                                filtered_data.append(filtered_item)

                            obj['queryset'] = filtered_data

                        field_info.append(obj)


            if (flag == 'l'):  # data grid list (react ag-grid)
                field_info = []
                for field_name, field_instance in fields.items():
                    obj={
                            'field': field_name,
                            'headerName': field_instance.label or field_name,
                            'info': str(field_instance.__class__.__name__),
                    }
                    if(field_name in ['id']):
                        obj['hide']=True
                    field_info.append(obj)

            return Response({'fields': field_info,
            'models': model_name, 'pk': NT._meta.pk.name}, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        return Response(status=status.HTTP_400_BAD_REQUEST)


class NTFieldsStateApiView(APIView):
    def get(self, request):
        serializer = NTSerializer()
        fields = serializer.get_fields()
        field_info = []

        cs = request.query_params.get("code_site", None)
        nt = request.query_params.get("nt", None)


        if cs and nt:
            num_t = NT.objects.get(code_site=Sites.objects.get(id=cs),nt=nt)
        else:
            num_t = None
        if (num_t == None):
            for field_name, field_instance in fields.items():
                default_value = None
                if (field_name not in ['',]):
                    default_value=None
                    if str(field_instance.__class__.__name__) == 'PrimaryKeyRelatedField':
                        default_value = []
                    if str(field_instance.__class__.__name__) == 'BooleanField':
                        default_value= True

                    if str(field_instance.__class__.__name__) in ['PositiveSmallIntegerField','DecimalField','PositiveIntegerField',
                                                                  'IntegerField','FloatField']:
                        default_value = 0

                    field_info.append({
                        field_name:default_value ,

                    })


                    state = {}

                for d in field_info:
                    state.update(d)
            return Response({'state': state}, status=status.HTTP_200_OK)
        else:

            update_nt = NTSerializer(num_t).data

            for field_name, field_instance in fields.items():
                if (not field_name in ['']):
                    default_value = update_nt[field_name]

                    field_info.append({
                        field_name: default_value,

                    })
                    state = {}

                    for d in field_info:
                        state.update(d)

            site = Sites.objects.get(id=state['site'])
            state['site'] = [{'value': site.id, 'label': site.id}]

            situation = TabSituationNt.objects.get(libelle=state['code_situation_nt'])
            state['code_situation_nt'] = [{'value': situation.id, 'label': situation.libelle or situation.id}]
            client = Clients.objects.get(id=state['client'])
            state['client'] = [{'value': client.id, 'label': client.libelle or client.id}]

        return Response({'state': state}, status=status.HTTP_200_OK)


class FactureFieldsApiView(APIView):
    def get(self, request):
        flag = request.query_params.get('flag', None)
        if flag == 'l' or flag == 'f' or flag == 'p':
            serializer = FactureSerializer()
            fields = serializer.get_fields()

            model_class = serializer.Meta.model
            model_name = model_class.__name__
            if (flag == 'f'):  # react form
                field_info = []
                for field_name, field_instance in fields.items():

                    if( field_name in ['numero_facture','du','au','num_situation','penalite'] ):

                        obj = {
                            'name': field_name,
                            'type': str(field_instance.__class__.__name__),
                            "required": field_instance.required,
                            'label': field_instance.label or field_name,

                        }

                        if (field_name == 'numero_facture'):
                            try:
                                num_last_facture = Factures.objects.annotate(
                                    numero_facture_int=Cast('numero_facture', IntegerField())
                                ).all().last().numero_facture
                                obj['count'] = num_last_facture
                            except Exception as e:
                                pass
                        if (field_name == 'num_situation'):
                            try:
                                nt=request.query_params.get('nt', None)
                                cs=request.query_params.get('cs', None)
                                num_last_situation = Factures.objects.filter(marche__nt=nt,marche__code_site=cs,est_bloquer=False).last().num_situation
                                obj['count'] = num_last_situation
                            except Exception as e:
                                pass

                        if (str(field_instance.__class__.__name__) == "PrimaryKeyRelatedField"):
                            anySerilizer = create_dynamic_serializer(field_instance.queryset.model)
                            obj['queryset'] = anySerilizer(field_instance.queryset, many=True).data

                        field_info.append(obj)


            if (flag == 'l'):  # data grid list (react ag-grid)
                field_info = []
                for field_name, field_instance in fields.items():
                    obj={
                        'field': field_name,
                        'headerName': field_instance.label or field_name,
                        'info': str(field_instance.__class__.__name__),

                    }
                    if(field_name in ['client','signature','montant_marche','pole','lib_nt','projet','somme','marche','heure',
                                      'num_travail','code_contrat']):
                        obj['hide']= True


                    if (field_name in ['montant_cumule','montant','montant_precedent','montant_rg','montant_taxe','montant_rb',"montant_factureHT",'montant_factureTTC',
                                       "avf","ava",'ave','penalite','taux_realise']):
                        obj['cellRenderer'] = 'InfoRenderer'
                    field_info.append(obj)



            return Response({'fields': field_info,
            'models': model_name, 'pk': Factures._meta.pk.name}, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        return Response(status=status.HTTP_400_BAD_REQUEST)



class FactureFieldsStateApiView(APIView):
    def get(self, request):
        serializer = FactureSerializer()
        fields = serializer.get_fields()
        field_info = []
        for field_name, field_instance in fields.items():
            default_value = None
            if (field_name in ['numero_facture','du','au','num_situation','penalite']):
                if str(field_instance.__class__.__name__) == 'PrimaryKeyRelatedField':
                    default_value = []
                if str(field_instance.__class__.__name__) == 'BooleanField':
                    default_value= True

                if str(field_instance.__class__.__name__) in ['PositiveSmallIntegerField','DecimalField','PositiveIntegerField',
                                                              'IntegerField',]:
                    default_value = 0

                field_info.append({
                    field_name:default_value ,

                })


                state = {}

            for d in field_info:
                state.update(d)
        return Response({'state': state}, status=status.HTTP_200_OK)


class FactureFieldsFilterApiView(APIView):
    def get(self, request):
        field_info = []
        for field_name, field_instance in FactureFilter.base_filters.items():
            if (field_name not in ['marche']):

                obj = {
                    'name': field_name,
                    'type': str(field_instance.__class__.__name__),
                    'label': field_instance.label or field_name,

                }


                if str(field_instance.__class__.__name__) == 'ModelChoiceFilter':
                    anySerilizer = create_dynamic_serializer(field_instance.queryset.model)
                    serialized_data = anySerilizer(field_instance.queryset, many=True).data
                    filtered_data = []
                    for item in serialized_data:
                        filtered_item = {
                            'value': item['id'],
                             'label': item['libelle']
                        }
                        filtered_data.append(filtered_item)

                    obj['queryset'] = filtered_data

                field_info.append(obj)

        return Response({'fields': field_info}, status=status.HTTP_200_OK)


class EncaissementFieldsApiView(APIView):
    def get(self, request):
        flag = request.query_params.get('flag', None)
        if flag == 'l' or flag == 'f' or flag == 'p':
            serializer = EncaissementSerializer()
            fields = serializer.get_fields()

            model_class = serializer.Meta.model
            model_name = model_class.__name__
            if (flag == 'f'):  # react form
                field_info = []
                for field_name, field_instance in fields.items():
                    if( not field_name in ['montant_creance','facture','id'] ):
                        obj = {
                            'name': field_name,
                            'type': str(field_instance.__class__.__name__),
                            "required": field_instance.required,
                            'label': field_instance.label or field_name,

                        }

                        if (str(field_instance.__class__.__name__) == "PrimaryKeyRelatedField"):
                            anySerilizer = create_dynamic_serializer(field_instance.queryset.model)
                            serialized_data = anySerilizer(field_instance.queryset, many=True).data
                            filtered_data = []
                            for item in serialized_data:
                                filtered_item = {
                                    'value': item['id'],
                                    'label': item['libelle']
                                }
                                filtered_data.append(filtered_item)

                            obj['queryset'] = filtered_data

                        field_info.append(obj)


            if (flag == 'l'):  # data grid list (react ag-grid)
                field_info = []
                for field_name, field_instance in fields.items():
                    if( field_name not in ['']):
                        obj = {
                            'field': field_name,
                            'headerName': field_instance.label or field_name,
                            'info': str(field_instance.__class__.__name__),
                            'cellRenderer': 'InfoRenderer'
                        }
                        if (field_name in ['facture']):
                            obj['rowGroup'] = True

                        if (field_name in ['id']):
                            obj['hide'] = True



                        if (str(field_instance.__class__.__name__) == "PrimaryKeyRelatedField"):
                            obj['related'] = str(field_instance.queryset.model.__name__)

                        field_info.append(obj)

            return Response({'fields': field_info,
            'models': model_name, 'pk': Encaissement._meta.pk.name}, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        return Response(status=status.HTTP_400_BAD_REQUEST)


class EncaissementFieldsStateApiView(APIView):
    def get(self, request):
        serializer = EncaissementSerializer()
        fields = serializer.get_fields()
        field_info = []
        for field_name, field_instance in fields.items():
            default_value = None
            if (field_name not in  ['montant_creance','facture']):
                if str(field_instance.__class__.__name__) == 'PrimaryKeyRelatedField':
                    default_value = []
                if str(field_instance.__class__.__name__) == 'BooleanField':
                    default_value= True

                if str(field_instance.__class__.__name__) in ['PositiveSmallIntegerField','DecimalField','PositiveIntegerField',
                                                              'IntegerField',]:
                    default_value = 0

                field_info.append({
                    field_name:default_value ,

                })


                state = {}

            for d in field_info:
                state.update(d)
        return Response({'state': state}, status=status.HTTP_200_OK)


class EncaissementFieldsFilterApiView(APIView):
    def get(self,request):
        filter_fields = list(EncaissementFilter.base_filters.keys())
        serializer = EncaissementSerializer()
        fields = serializer.get_fields()
        field_info = []
        for field_name, field_instance in fields.items():
            if field_name in filter_fields:
                if( field_name not in ['facture']):

                    obj = {
                        'name': field_name,
                        'type': str(field_instance.__class__.__name__),

                        'label': field_instance.label or field_name,
                    }
                    if (str(field_instance.__class__.__name__) == "PrimaryKeyRelatedField"):
                        anySerilizer = create_dynamic_serializer(field_instance.queryset.model)
                        serialized_data = anySerilizer(field_instance.queryset, many=True).data
                        filtered_data = []
                        for item in serialized_data:
                            filtered_item = {
                                'value': item['id'],
                                'label': item['libelle']
                            }
                            filtered_data.append(filtered_item)

                        obj['queryset'] = filtered_data
                    field_info.append(obj)

        return Response({'fields': field_info},status=status.HTTP_200_OK)



class DetailFactureFieldsApiView(APIView):
    def get(self, request):
        serializer = DetailFactureSerializer()
        fields = serializer.get_fields()

        model_class = serializer.Meta.model
        model_name = model_class.__name__

        field_info = []
        for field_name, field_instance in fields.items():
            if (field_name not in ['facture','detail']):
                obj = {
                    'field': field_name,
                    'headerName': field_instance.label or field_name,
                    'info': str(field_instance.__class__.__name__),
                }
                field_info.append(obj)

        return Response({'fields': field_info,
        'models': model_name, 'pk': DetailFacture._meta.pk.name}, status=status.HTTP_200_OK)


class DetailFactureFieldsFilterApiView(APIView):
    def get(self,request):
        filter_fields = list(DetailFactureFilter.base_filters.keys())

        serializer = DetailFactureSerializer()
        fields = serializer.get_fields()
        field_info = []
        for field_name, field_instance in fields.items():
            if field_name in filter_fields:
                if (field_name not in ['facture','detail']):

                    obj = {
                        'name': field_name,
                        'type': str(field_instance.__class__.__name__),

                        'label': field_instance.label or field_name,
                    }
                    if (str(field_instance.__class__.__name__) == "PrimaryKeyRelatedField"):
                        anySerilizer = create_dynamic_serializer(field_instance.queryset.model)
                        obj['queryset'] = anySerilizer(field_instance.queryset, many=True).data
                    field_info.append(obj)

        return Response({'fields': field_info},status=status.HTTP_200_OK)






class AvanceFieldsFilterApiView(APIView):
    def get(self,request):
        filter_fields = list(AvanceFilter.base_filters.keys())

        serializer = AvanceSerializer()
        fields = serializer.get_fields()
        field_info = []
        for field_name, field_instance in fields.items():
            if field_name in filter_fields:
                if (field_name not in ['marche',]):

                    obj = {
                        'name': field_name,
                        'type': str(field_instance.__class__.__name__),

                        'label': field_instance.label or field_name,
                    }
                    try:
                        if field_instance.choices:

                            obj['choices'] = ['']
                            for choice in field_instance.choices:
                                obj['choices'].append(choice)
                    except:
                        pass
                    if (str(field_instance.__class__.__name__) == "PrimaryKeyRelatedField"):
                        anySerilizer = create_dynamic_serializer(field_instance.queryset.model)
                        obj['queryset'] = anySerilizer(field_instance.queryset, many=True).data
                    field_info.append(obj)

        return Response({'fields': field_info},status=status.HTTP_200_OK)



class AvanceFieldsApiView(APIView):
    def get(self, request):
        flag = request.query_params.get('flag', None)
        if flag == 'l' or flag == 'f' :
            serializer = AvanceSerializer()
            fields = serializer.get_fields()

            model_class = serializer.Meta.model
            model_name = model_class.__name__
            if (flag == 'f'):  # react form
                field_info = []

                for field_name, field_instance in fields.items():

                    if( not field_name in ['taux_avance','taux_remb','heure','marche','id','num_avance','remboursee'] ):
                        obj = {
                            'name': field_name,
                            'type': str(field_instance.__class__.__name__),
                            "required": field_instance.required,
                            'label': field_instance.label or field_name,


                        }

                        if (str(field_instance.__class__.__name__) == "PrimaryKeyRelatedField"):
                            anySerilizer = create_dynamic_serializer(field_instance.queryset.model)
                            serialized_data = anySerilizer(field_instance.queryset, many=True).data
                            filtered_data = []
                            for item in serialized_data:
                                filtered_item = {
                                    'value': item['id'],
                                    'label': item['libelle']
                                }
                                filtered_data.append(filtered_item)

                            obj['queryset'] = filtered_data

                        field_info.append(obj)


            if (flag == 'l'):  # data grid list (react ag-grid)
                field_info = []
                for field_name, field_instance in fields.items():
                    if (field_name not in [""]):
                        obj={
                            'field': field_name,
                            'headerName': field_instance.label or field_name,
                            'info': str(field_instance.__class__.__name__),
                        }
                        if(field_name in ['id','marche']):
                            obj['hide']=True
                        if(field_name in ['taux_avance','taux_remb','montant','debut','fin']):
                            obj['cellRenderer']='InfoRenderer'

                        field_info.append(obj)




            return Response({'fields': field_info,
            'models': model_name, 'pk': Avance._meta.pk.name}, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        return Response(status=status.HTTP_400_BAD_REQUEST)



class AvanceFieldsStateApiView(APIView):
    def get(self, request):
        serializer = AvanceSerializer()
        fields = serializer.get_fields()
        field_info = []
        for field_name, field_instance in fields.items():
            default_value = None
            if (field_name not in  ['heure','marche','id','taux_remb','taux_avance']):
                if str(field_instance.__class__.__name__) == 'PrimaryKeyRelatedField':
                    default_value= []
                if str(field_instance.__class__.__name__) == 'BooleanField':
                    default_value= False

                if str(field_instance.__class__.__name__) in ['PositiveSmallIntegerField','DecimalField','PositiveIntegerField',
                                                              'IntegerField',]:
                    default_value = 0

                field_info.append({
                    field_name:default_value ,

                })


                state = {}

            for d in field_info:
                state.update(d)
        return Response({'state': state}, status=status.HTTP_200_OK)


class CautionFieldsApiView(APIView):
    def get(self, request):
        flag = request.query_params.get('flag', None)
        if flag == 'l' or flag == 'f' :
            serializer = CautionSerializer()
            fields = serializer.get_fields()

            model_class = serializer.Meta.model
            model_name = model_class.__name__

            if (flag == 'f'):  # react form
                marche = Marche.objects.get(nt=request.query_params.get('nt', None),
                                            code_site=request.query_params.get('cs', None))

                field_info = []
                for field_name, field_instance in fields.items():

                    if( not field_name in ['est_recupere','marche','id','taux'] ):
                        obj = {
                            'name': field_name,
                            'type': str(field_instance.__class__.__name__),
                            "required": field_instance.required,
                            'label': field_instance.label or field_name,


                        }


                        if (str(field_instance.__class__.__name__) == "PrimaryKeyRelatedField" ):
                            if (str(field_instance.queryset.model.__name__) == "Avance"):
                                serialized_data = AvanceSerializer(field_instance.queryset.filter(marche=marche),
                                                                   many=True).data

                                filtered_data = []
                                for item in serialized_data:
                                    filtered_item = {
                                        'value': item['id'],
                                        'label': f'{item["type"]} N° {item["num_avance"]} '
                                    }
                                    filtered_data.append(filtered_item)

                                obj['queryset'] = filtered_data



                            else:
                                anySerilizer = create_dynamic_serializer(field_instance.queryset.model)
                                serialized_data = anySerilizer(field_instance.queryset, many=True).data
                                filtered_data = []
                                for item in serialized_data:
                                    filtered_item = {
                                        'value': item['id'],
                                        'label': item['libelle']
                                    }
                                    filtered_data.append(filtered_item)

                                obj['queryset'] = filtered_data

                        field_info.append(obj)


            if (flag == 'l'):  # data grid list (react ag-grid)
                field_info = []
                for field_name, field_instance in fields.items():
                    if (field_name not in ['marche']):
                        obj={
                            'field': field_name,
                            'headerName': field_instance.label or field_name,
                            'info': str(field_instance.__class__.__name__),

                        }
                        if(str(field_instance.__class__.__name__) != 'BooleanField' ):
                            obj['cellRenderer']='InfoRenderer'
                        if(field_name in ['id']):
                            obj['hide']=True
                        field_info.append(obj)



            return Response({'fields': field_info,
            'models': model_name, 'pk': Cautions._meta.pk.name}, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        return Response(status=status.HTTP_400_BAD_REQUEST)





class CautionFieldsStateApiView(APIView):
    def get(self, request):
        serializer = CautionSerializer()
        fields = serializer.get_fields()
        field_info = []
        for field_name, field_instance in fields.items():
            default_value = None
            if (field_name not in  ['id','est_recupere','marche','taux']):
                if str(field_instance.__class__.__name__) == 'PrimaryKeyRelatedField':
                    default_value = []
                if str(field_instance.__class__.__name__) == 'BooleanField':
                    default_value= True

                if str(field_instance.__class__.__name__) in ['PositiveSmallIntegerField','DecimalField','PositiveIntegerField',
                                                              'IntegerField',]:
                    default_value = 0

                field_info.append({
                    field_name:default_value ,

                })


                state = {}

            for d in field_info:
                state.update(d)
        return Response({'state': state}, status=status.HTTP_200_OK)







class FlashFieldsApiView(APIView):
    def get(self, request):
        serializer = ProductionSerializer()
        fields = serializer.get_fields()
        model_class = serializer.Meta.model
        model_name = model_class.__name__

        flag = request.query_params.get('flag',None)
        if flag=='l':

            field_info = []
            obj1 = {
                    "headerName": 'Contractuel',
                    "children": []
                }
            obj2 = {
                    "headerName": 'Supplementaire',
                    "children": []
                }
            obj3 = {
                    "headerName": 'Complementaire',
                    "children": []
                }

            for field_name, field_instance in fields.items():
                if(field_name not in ['nt','code_site','code_groupeactivite',
                    'recepteur','code_produit','type_prestation'
                    ,'code_type_production','code_filiale','code_activite'
                    ,'prevu_realiser','id_production','est_cloturer','user_id','date_modification']):

                    obj={
                                'field': field_name,
                                'headerName': field_instance.label or field_name,
                                'info': str(field_instance.__class__.__name__),
                        }

                    if (field_name == 'code_tache'):
                        obj['checkboxSelection'] = True
                        obj['headerCheckboxSelection'] = True



                    if (str(field_name).startswith('valeur') or str(field_name).startswith('quantite')):
                        obj['cellRenderer'] = 'InfoRenderer'

                    if (field_name  in ['quantite_1', 'valeur_1']):
                        obj1['children'].append(obj)
                    if (field_name  in ['quantite_2', 'valeur_2']):
                        obj2['children'].append(obj)
                    if (field_name  in ['quantite_3', 'valeur_3']):
                        obj3['children'].append(obj)

                    if(field_name not in ['quantite_1', 'valeur_1','quantite_2', 'valeur_2','quantite_3', 'valeur_3']):
                        field_info.append(obj)
            field_info.append(obj1)
            field_info.append(obj2)
            field_info.append(obj3)

            return Response({'fields':field_info,'models':model_name,'pk':Marche._meta.pk.name},status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)







class AttachementsFieldsApiView(APIView):
    def get(self, request):
        flag = request.query_params.get('flag', None)
        if flag == 'l' or flag == 'f':
            serializer = AttachementsSerializer()
            fields = serializer.get_fields()

            model_class = serializer.Meta.model
            model_name = model_class.__name__

            if (flag == 'f'):  # react form
                field_info = []
                for field_name, field_instance in fields.items():

                    if(  field_name in ['qte',"date",] ):
                        obj = {
                            'name': field_name,
                            'type': str(field_instance.__class__.__name__),
                            "required": field_instance.required,
                            'label': field_instance.label or field_name,
                        }
                        if (str(field_instance.__class__.__name__) == "PrimaryKeyRelatedField"):
                            anySerilizer = create_dynamic_serializer(field_instance.queryset.model)
                            obj['queryset'] = anySerilizer(field_instance.queryset, many=True).data

                        field_info.append(obj)
                return Response({'fields': field_info,
                             'models': model_name, }, status=status.HTTP_200_OK)

            if (flag == 'l'):  # data grid list (react ag-grid)
                field_info = []
                field_info2 = []
                obj1 = {
                    "headerName": 'Qauntite',
                    "children": [],
                    'cellRenderer': 'InfoRenderer'

                }
                obj2 = {
                    "headerName": 'Montant',
                    "children": [],
                    'cellRenderer': 'InfoRenderer'
                }
                for field_name, field_instance in fields.items():
                    if(field_name in ['marche']):
                        pass
                    else:
                        obj = {
                            'field': field_name,
                            'headerName': field_instance.label or field_name,
                            'info': str(field_instance.__class__.__name__),

                        }
                        if(field_name =='code_tache'):
                            obj['checkboxSelection']= True
                            obj['headerCheckboxSelection']= True
                        if(field_name in ['qte','montant']):
                            obj['editable']= True
                        if(field_name in ['id','code_site','nt']):
                            obj['hide'] = True
                        if(field_name in ['prix_u']):
                            obj['cellRenderer'] = 'InfoRenderer'
                        if (str(field_instance.__class__.__name__) == "PrimaryKeyRelatedField"):
                            obj['related'] = str(field_instance.queryset.model.__name__)

                        field_info2.append(obj)
                        if (field_name in ['qte_precedente','qte','qte_cumule']):
                            obj['cellRenderer'] = 'InfoRenderer'
                            obj1['children'].append(obj)

                        if (field_name in ['montant_precedent','montant','montant_cumule']):
                            obj['cellRenderer'] = 'InfoRenderer'
                            obj2['children'].append(obj)
                        if (field_name not in ['montant_precedent', 'montant', 'montant_cumule','qte_precedente','qte','qte_cumule']):
                            field_info.append(obj)

                field_info.append(obj1)
                field_info.append(obj2)


            return Response({'fields': field_info,"fields2":field_info2,
            'models': model_name}, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        return Response(status=status.HTTP_400_BAD_REQUEST)






class AttFieldsStateApiView(APIView):
    def get(self, request):
        serializer = AttachementsSerializer()
        fields = serializer.get_fields()
        field_info = []

        idp=request.query_params.get('idp', None)
        production=TabProduction.objects.get(id_production=idp)
        if(production):
            for field_name, field_instance in fields.items():
                if(field_name in ['qte']):
                    default_value=round(production.quantite_1,2)
                    field_info.append({field_name:default_value})
                if (field_name in ['date']):
                    default_value = production.mmaa
                    field_info.append({field_name: default_value})
                if (field_name in ['dqe']):
                    default_value = production.code_tache
                    field_info.append({field_name: default_value})
                state = {}
                for d in field_info:
                    state.update(d)

            return Response({'state': state}, status=status.HTTP_200_OK)

        else:
            for field_name, field_instance in fields.items():
                default_value = None
                if(  field_name in ['qte',"date"] ):

                    if str(field_instance.__class__.__name__) == 'PrimaryKeyRelatedField':
                        default_value = []
                    if str(field_instance.__class__.__name__) == 'BooleanField':
                        default_value= True

                    if str(field_instance.__class__.__name__) in ['PositiveSmallIntegerField','DecimalField','PositiveIntegerField',
                                                                  'IntegerField',]:
                        default_value = 0

                    field_info.append({
                        field_name:default_value ,

                    })


                    state = {}

                for d in field_info:
                    state.update(d)
            return Response({'state': state}, status=status.HTTP_200_OK)




class FlashFieldsFilterApiView(APIView):
    def get(self,request):
        field_info = []
        for field_name, field_instance  in ProdFilter.base_filters.items():
            if(field_name in ['dqe']):

                obj = {
                    'name': field_name,
                    'type': str(field_instance.__class__.__name__),
                    'label': field_instance.label or field_name,

                }
                if str(field_instance.__class__.__name__) == 'ModelChoiceFilter':
                    anySerilizer = create_dynamic_serializer(field_instance.queryset.model)
                    serialized_data = anySerilizer(field_instance.queryset, many=True).data
                    filtered_data = []
                    for item in serialized_data:
                        filtered_item = {
                            'value': item['id'],
                            'label': item['libelle']
                        }
                        filtered_data.append(filtered_item)

                    obj['queryset'] = filtered_data



                field_info.append(obj)

        return Response({'fields': field_info},status=status.HTTP_200_OK)






class AttachementFieldsFilterApiView(APIView):
    def get(self,request):
        field_info = []


        for field_name, field_instance  in AttachementsFilter.base_filters.items():
            if(field_name  in ['code_tache']):

                obj = {
                    'name': field_name,
                    'type': str(field_instance.__class__.__name__),
                    'label': field_instance.label or field_name,

                }

                field_info.append(obj)

        return Response({'fields': field_info},status=status.HTTP_200_OK)









class AvenantFieldsApiView(APIView):
    def get(self, request):
        flag = request.query_params.get('flag',None)
        if flag=='l' or flag =='f':
            serializer = MarcheAvenantSerializer()
            fields = serializer.get_fields()
            model_class = serializer.Meta.model
            model_name = model_class.__name__

            if(flag=='f'): # react form

                field_info = []
                for field_name, field_instance in fields.items():

                    if(field_name not in ['montant_ht','montant_ttc',]):

                        if (field_name in ['id','nt','code_site',"libelle"]):
                            readOnly = True
                        else:
                            readOnly = False



                        obj={
                            'name':field_name,
                            'type': str(field_instance.__class__.__name__),
                            "required": field_instance.required,
                            'label': field_instance.label or field_name,
                            'source':field_instance.source,
                            'readOnly': readOnly
                        }

                        if (str(field_instance.style.get("base_template")).find('textarea') != -1):
                            obj['textarea'] = True


                        if (str(field_instance.__class__.__name__) == "PrimaryKeyRelatedField"):
                            anySerilizer = create_dynamic_serializer(field_instance.queryset.model)
                            serialized_data = anySerilizer(field_instance.queryset, many=True).data
                            filtered_data = []
                            for item in serialized_data:
                                if (field_name in ['code_site']):
                                    filtered_item = {
                                        'value': item['id'],
                                        'label': item['id']
                                    }
                                else:
                                    filtered_item = {
                                        'value': item['id'],
                                        'label': item['libelle'] or item['id']
                                    }
                                filtered_data.append(filtered_item)

                            obj['queryset'] = filtered_data

                        field_info.append(obj)

            if(flag=='l'): #data grid list (react ag-grid)
                field_info = []
                for field_name, field_instance in fields.items():

                    obj={
                        'field': field_name,
                        'headerName': field_instance.label or field_name,
                        'info': str(field_instance.__class__.__name__),
                    }


                    if (field_name in ['rg','rabais','tva', 'montant_ttc', 'montant_ht']):
                        obj['cellRenderer'] = 'InfoRenderer'

                    field_info.append(obj)
            return Response({'fields':field_info,'models':model_name,'pk':Marche._meta.pk.name},status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        return Response(status=status.HTTP_400_BAD_REQUEST)




class AvenantFieldsStateApiView(APIView):
    def get(self, request):
        serializer = MarcheAvenantSerializer()
        fields = serializer.get_fields()
        field_info = []
        id = request.query_params.get('id', None)
        num_av=request.query_params.get('av', None)

        if id and num_av:
            marche = MarcheAvenant.objects.get(id=id,num_avenant=num_av)
        else:
            marche = None
        if(marche == None):

            for field_name, field_instance in fields.items():
                if (field_name not in ['id', 'montant_ht', 'montant_ttc','num_avenant']):
                    default_value = None
                    if (str(field_instance.__class__.__name__) == "PrimaryKeyRelatedField"):
                        default_value =[]

                    if str(field_instance.__class__.__name__) == 'BooleanField':
                        default_value= False
                    if str(field_instance.__class__.__name__) in ['PositiveSmallIntegerField','DecimalField','PositiveIntegerField',
                                                                  'IntegerField','FloatField']:
                        default_value = 0

                    field_info.append({
                        field_name:default_value ,

                    })
                    state = {}

                    for d in field_info:
                        state.update(d)
            return Response({'state': state}, status=status.HTTP_200_OK)

        else:
            update_marche=MarcheSerializer(marche).data
            for field_name, field_instance in fields.items():

                    default_value = update_marche[field_name]
                    field_info.append({
                        field_name:default_value ,

                    })
                    state = {}


                    for d in field_info:
                        state.update(d)

            s=Sites.objects.get(id=state['code_site'])

            state['code_site']=[{'value':s.id,'label':s.libelle}]

        return Response({'state': state}, status=status.HTTP_200_OK)





class DQEAVFieldsApiView(APIView):
    def get(self, request):
        flag = request.query_params.get('flag',None)
        if flag=='l' or flag =='f':
            serializer = DQEAvenantSerializer()
            model_class = serializer.Meta.model
            model_name = model_class.__name__
            fields = serializer.get_fields()

            if(flag=='f'): # react form
                field_info = []
                for field_name, field_instance in fields.items():

                    if (field_name not in ['prix_q','id','pole','nt','num_avenant']):

                        if( field_name in ['prix_u','quantite']):
                            readOnly=False
                        else:
                            readOnly = True
                        obj = {
                            'name': field_name,
                            'type': str(field_instance.__class__.__name__),
                            "required": field_instance.required,
                            'label': field_instance.label or field_name,
                            'readOnly': readOnly
                        }
                        if (str(field_instance.style.get("base_template")).find('textarea') != -1):
                            obj['textarea'] = True

                        if (str(field_instance.__class__.__name__) == "PrimaryKeyRelatedField"):
                            anySerilizer = create_dynamic_serializer(field_instance.queryset.model)
                            serialized_data = anySerilizer(field_instance.queryset, many=True).data
                            filtered_data = []
                            for item in serialized_data:
                                filtered_item = {
                                    'value': item['id'],
                                    'label': item['libelle']
                                }
                                filtered_data.append(filtered_item)

                            obj['queryset'] = filtered_data

                        field_info.append(obj)

            if(flag=='l'): #data grid list (react ag-grid)
                field_info = []
                for field_name, field_instance in fields.items():
                    if(field_name not in ['',]):
                        obj = {
                            'field': field_name,
                            'headerName': field_instance.label or field_name,
                            'info': str(field_instance.__class__.__name__),

                        }
                        if( field_name in ['pole','nt','num_avenant']):
                            obj['hide'] = True
                        if (str(field_instance.__class__.__name__) == "PrimaryKeyRelatedField") and field_name not in ['marche']:
                            obj['related'] = str(field_instance.queryset.model.__name__)
                        if(field_name in ['prix_u','prix_q','quantite']):
                            obj['cellRenderer']='InfoRenderer'

                        field_info.append(obj)


            return Response({'fields':field_info,'models':model_name,'pk':DQE._meta.pk.name},status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        return Response(status=status.HTTP_400_BAD_REQUEST)




class MarcheAVFieldsFilterApiView(APIView):
    def get(self,request):
        field_info = []

        for field_name, field_instance  in MarcheAvenantFilter.base_filters.items():


            obj = {
                'name': field_name,
                'type': str(field_instance.__class__.__name__),
                'label': field_instance.label or field_name,

            }
            if str(field_instance.__class__.__name__) == 'ModelChoiceFilter':
                anySerilizer = create_dynamic_serializer(field_instance.queryset.model)
                serialized_data = anySerilizer(field_instance.queryset, many=True).data
                filtered_data = []
                for item in serialized_data:
                    if(field_name in ['code_site']):
                        filtered_item = {
                            'value': item['id'],
                            'label': item['id']
                        }
                    else:
                        filtered_item = {
                            'value': item['id'],
                            'label': item['libelle'] or item['id']
                        }
                    filtered_data.append(filtered_item)

                obj['queryset'] = filtered_data



            field_info.append(obj)

        return Response({'fields': field_info},status=status.HTTP_200_OK)


class DQEAVFieldsFilterApiView(APIView):
    def get(self,request):
        field_info=[]
        for field_name, field_instance in DQEAvenantFilter.base_filters.items():
            if(field_name not in ['marche','nt','code_site','num_avenant']):
                obj = {
                            'name': field_name,
                            'type': str(field_instance.__class__.__name__),
                            'label': field_instance.label or field_name,
                }
                field_info.append(obj)

        return Response({'fields': field_info},status=status.HTTP_200_OK)






class DetailFieldsApiView(APIView):
    def get(self, request):
        flag = request.query_params.get('flag', None)
        if flag == 'l' :
            serializer = DetailFactureSerializer()
            fields = serializer.get_fields()

            model_class = serializer.Meta.model
            model_name = model_class.__name__

            if (flag == 'l'):  # data grid list (react ag-grid)
                field_info = []
                for field_name, field_instance in fields.items():
                    if (field_name not in ['']):
                        obj={
                            'field': field_name,
                            'headerName': field_instance.label or field_name,
                            'info': str(field_instance.__class__.__name__),

                        }
                        if(field_name in ['unite']):
                            obj['hide']=True
                        if(field_name in ['montant','prix_u','qte'] ):
                            obj['cellRenderer']='InfoRenderer'

                        field_info.append(obj)

            return Response({'fields': field_info,
            'models': model_name}, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        return Response(status=status.HTTP_400_BAD_REQUEST)




class PSFieldsApiView(APIView):
    def get(self, request):
        flag = request.query_params.get('flag', None)
        if flag == 'l' :
            serializer = PSSerializer()
            fields = serializer.get_fields()

            model_class = serializer.Meta.model
            model_name = model_class.__name__

            if (flag == 'l'):  # data grid list (react ag-grid)
                field_info = []
                for field_name, field_instance in fields.items():
                    if (field_name not in ['']):
                        obj={
                            'field': field_name,
                            'headerName': field_instance.label or field_name,
                            'info': str(field_instance.__class__.__name__),

                        }
                        if(field_name in ['code_site','nt','unite']):
                            obj['hide']=True
                        if(field_name in ['qte_prod','ecart','qte_att','ind'] ):
                            obj['cellRenderer']='InfoRenderer'

                        field_info.append(obj)

            return Response({'fields': field_info,
            'models': model_name}, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        return Response(status=status.HTTP_400_BAD_REQUEST)