from django.db.models import Sum
from num2words import num2words
from rest_framework import serializers

from api_sm.models import *


def create_dynamic_serializer(model_class):
    class DynamicModelSerializer(serializers.ModelSerializer):

        class Meta:
            model = model_class
            fields = '__all__'

    return DynamicModelSerializer




class UserSerializer(serializers.ModelSerializer):
    def get_fields(self, *args, **kwargs):
        fields = super().get_fields(*args, **kwargs)
        fields.pop('id', None)
        return fields
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name','password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', ''),
            is_active=False

        )
        return user


class ICSerializer(serializers.ModelSerializer):

    class Meta:
        model = Images
        fields = '__all__'

class OptionImpressionSerializer(serializers.ModelSerializer):
    def get_fields(self, *args, **kwargs):
        fields = super().get_fields(*args, **kwargs)
        fields.pop('deleted', None)
        fields.pop('deleted_by_cascade', None)
        return fields

    class Meta:
        model = OptionImpression
        fields = '__all__'

class ClientsSerializer(serializers.ModelSerializer):
    def get_fields(self, *args, **kwargs):
        fields = super().get_fields(*args, **kwargs)
        fields.pop('deleted', None)
        fields.pop('deleted_by_cascade', None)
        return fields



    class Meta:
        model = Clients
        fields = '__all__'



class SiteSerializer(serializers.ModelSerializer):
    def get_fields(self, *args, **kwargs):
        fields = super().get_fields(*args, **kwargs)
        fields.pop('deleted', None)
        fields.pop('deleted_by_cascade', None)
        return fields


    class Meta:
        model = Sites
        fields = '__all__'










class NTSerializer(serializers.ModelSerializer):
    class Meta:
        model=NT
        fields ='__all__'
    def get_fields(self, *args, **kwargs):
        fields = super().get_fields(*args, **kwargs)
        fields.pop('deleted', None)
        fields.pop('deleted_by_cascade', None)
        return fields

    def to_representation(self, instance):
        representation = super().to_representation(instance)



        return representation



class DQESerializer(serializers.ModelSerializer):
    prix_q = serializers.SerializerMethodField(label="Montant")

    def get_prix_q(self, obj):
        return obj.prix_q

    class Meta:
        model=DQE
        fields = [ 'id','code_tache','marche','code_site' ,'nt' ,'libelle','unite','prix_u' ,'quantite','prix_q',
    'aug_dim','est_tache_composite','est_tache_complementaire', ]


    def get_fields(self, *args, **kwargs):
        fields = super().get_fields(*args, **kwargs)
        fields.pop('deleted', None)
        fields.pop('deleted_by_cascade', None)

        return fields





class MarcheSerializer(serializers.ModelSerializer):
    code_site=serializers.PrimaryKeyRelatedField(source="nt_code_site",queryset=Sites.objects.all(),write_only=True,label='Code du site')
    nt=serializers.CharField(source="nt_nt",write_only=True,label='NT')
    montant_ht = serializers.SerializerMethodField()
    montant_ttc = serializers.SerializerMethodField()

    def get_montant_ht(self, obj):
        return obj.ht

    def get_montant_ttc(self, obj):
        return obj.ttc
    
    class Meta:
        model = Marche
        fields = "__all__"



    def create(self, validated_data):
        code_site = validated_data.pop('nt_code_site')
        num_t = validated_data.pop('nt_nt')
        print(code_site,num_t)
        nt_obj = NT.objects.get(
            code_site_id=code_site,
            nt=num_t
        )

        marche = Marche.objects.create(nt=nt_obj, **validated_data)
        return marche

    def get_fields(self, *args, **kwargs):
        fields = super().get_fields(*args, **kwargs)
        fields.pop('deleted', None)
        fields.pop('deleted_by_cascade', None)
        return fields
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['ht'] = instance.ht
        representation['ttc'] = instance.ttc
        representation['code_site'] = instance.nt.code_site.id
        representation['nt'] = instance.nt.nt


        return representation


class EtatCreanceSerializer(serializers.ModelSerializer):
    code_site = serializers.PrimaryKeyRelatedField(source="nt_code_site", queryset=Sites.objects.all(), write_only=True,
                                                   label='Code du site')
    nt = serializers.CharField(source="nt_nt", write_only=True, label='NT')
    gf = serializers.SerializerMethodField(label='Montant Global des factures')
    ge = serializers.SerializerMethodField(label='Montant Global Encaissé')
    cr = serializers.SerializerMethodField(label='Creance')

    def get_gf(self, obj):
        return obj.montant_gf
    def get_ge(self, obj):
        return obj.montant_ge
    def get_cr(self,obj):
        return obj.montant_creance

    def get_fields(self, *args, **kwargs):
        fields = super().get_fields(*args, **kwargs)
        fields.pop('deleted', None)
        fields.pop('deleted_by_cascade', None)
        return fields

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['cr'] = instance.montant_creance
        representation['ge'] = instance.montant_ge
        representation['gf'] = instance.montant_gf
        representation['code_site'] = instance.nt.code_site.id
        representation['nt'] = instance.nt.nt


        return representation

    class Meta:
        model = Marche
        fields = ['id', 'code_site', 'nt', 'gf', 'ge', 'cr']


class FactureSerializer(serializers.ModelSerializer):
    num_situation = serializers.IntegerField(label='Numero de la situation')
    projet=serializers.CharField(source='marche.libelle',read_only=True,label="Projet")
    code_contrat=serializers.CharField(source='marche.id',read_only=True,label="Contrat N°")
    signature=serializers.CharField(source='marche.date_signature',read_only=True,label="Signature")
    montant_marche = serializers.CharField(source='marche.ht', read_only=True, label="Montant du Marche")
    client = serializers.CharField(source='marche.nt.code_client.id', read_only=True, label="Client")
    pole = serializers.CharField(source='marche.nt.code_site.id', read_only=True, label="Pole")
    num_travail=serializers.CharField(source='marche.nt.nt', read_only=True, label="NT")
    lib_nt = serializers.CharField(source='marche.nt.libelle', read_only=True, label="Libelle du travail")

    somme=serializers.SerializerMethodField(label="Arretée la présenta facture à la somme de")

    tva=serializers.CharField(source='marche.tva', read_only=True, label="TVA")
    rabais=serializers.CharField(source='marche.rabais', read_only=True, label="Rabais")
    retenue_garantie = serializers.CharField(source='marche.rg', read_only=True, label="Retenue de Garantie")

    montant_precedent=serializers.SerializerMethodField(label="Montant Precedent")

    montant_cumule=serializers.SerializerMethodField(label="Montant Cumule")



    class Meta:
        model=Factures
        fields="__all__"




    def get_somme(self, obj):
        return num2words(obj.montant_factureTTC, to='currency', lang='fr_DZ').upper()

    def get_montant_precedent(self,obj):
        return obj.montant_precedent

    def get_montant_cumule(self,obj):
        return obj.montant_cumule

    def get_fields(self, *args, **kwargs):
        fields = super().get_fields(*args, **kwargs)
        fields.pop('deleted', None)
        fields.pop('deleted_by_cascade', None)

        return fields


    def to_representation(self, instance):
        representation = super().to_representation(instance)

        return representation



class TimeLineSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeLine
        fields = '__all__'
    def get_fields(self, *args, **kwargs):
        fields = super().get_fields(*args, **kwargs)
        fields.pop('deleted', None)
        fields.pop('deleted_by_cascade', None)

        return fields


class ModePaiementSerializer(serializers.ModelSerializer):
    class Meta:
        model=ModePaiement
        fields='__all__'
    def get_fields(self, *args, **kwargs):
        fields = super().get_fields(*args, **kwargs)
        fields.pop('deleted', None)
        fields.pop('deleted_by_cascade', None)


        return fields


    def to_representation(self, instance):
        representation = super().to_representation(instance)
        return representation



class EncaissementSerializer(serializers.ModelSerializer):

    class Meta:
        model=Encaissement
        fields='__all__'

    def get_fields(self, *args, **kwargs):
        fields = super().get_fields(*args, **kwargs)
        fields.pop('deleted', None)
        fields.pop('deleted_by_cascade', None)


        return fields


    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['montant_creance']=instance.montant_creance
        representation['montant_encaisse'] = instance.montant_encaisse
        representation['agence'] = instance.agence.libelle

        del representation['facture']

        return representation







class DetailFactureSerializer(serializers.ModelSerializer):
    date = serializers.CharField(source='detail.date', read_only=True, label="Date Attachement")
    code_tache = serializers.CharField(source='detail.dqe.code_tache', read_only=True, label="Code Tache")
    libelle_tache = serializers.CharField(source='detail.dqe.libelle', read_only=True, label="Libelle Tache")
    qte_attache = serializers.CharField(source='detail.qte_mois', read_only=True, label="Quantite attachée")
    unite = serializers.CharField(source='detail.dqe.unite.libelle', read_only=True, label="Unite")
    prix_attache = serializers.CharField(source='detail.montant_mois', read_only=True, label="Prix attaché")
    qte_contr = serializers.CharField(source='detail.dqe.quantite', read_only=True, label="Quantite Contrat")
    prix_contr = serializers.CharField(source='detail.dqe.prix_u', read_only=True, label="Prix Contrat")

    class Meta:
            model=DetailFacture
            fields='__all__'

    def get_fields(self, *args, **kwargs):
        fields = super().get_fields(*args, **kwargs)
        fields.pop('id', None)
        fields.pop('deleted', None)
        fields.pop('deleted_by_cascade', None)


        return fields


    def to_representation(self, instance):
        representation = super().to_representation(instance)
        del representation['facture']
        del representation['detail']
        return representation



class AvanceSerializer(serializers.ModelSerializer):
    class Meta:
            model=Avance
            fields='__all__'

    def get_fields(self, *args, **kwargs):
        fields = super().get_fields(*args, **kwargs)
        fields.pop('deleted', None)
        fields.pop('deleted_by_cascade', None)
        return fields
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['type']=instance.type.libelle

        return representation



class TypeAvanceSerializer(serializers.ModelSerializer):
    class Meta:
        model=TypeAvance
        fields='__all__'
    def get_fields(self, *args, **kwargs):
        fields = super().get_fields(*args, **kwargs)
        fields.pop('deleted', None)
        fields.pop('deleted_by_cascade', None)


        return fields


    def to_representation(self, instance):
        representation = super().to_representation(instance)
        return representation






class CautionSerializer(serializers.ModelSerializer):

    class Meta:
            model=Cautions
            fields='__all__'


    def get_fields(self, *args, **kwargs):
        fields = super().get_fields(*args, **kwargs)
        fields.pop('deleted', None)
        fields.pop('deleted_by_cascade', None)
        return fields


    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['avance'] = instance.avance.type.libelle
        representation['type'] = instance.type.libelle
        return representation

class TypeCautionSerializer(serializers.ModelSerializer):
    class Meta:
        model=TypeCaution
        fields='__all__'
    def get_fields(self, *args, **kwargs):
        fields = super().get_fields(*args, **kwargs)
        fields.pop('deleted', None)
        fields.pop('deleted_by_cascade', None)


        return fields


    def to_representation(self, instance):
        representation = super().to_representation(instance)
        return representation


class Ordre_De_ServiceSerializer(serializers.ModelSerializer):

    class Meta:
            model=Ordre_De_Service
            fields='__all__'


    def get_fields(self, *args, **kwargs):
        fields = super().get_fields(*args, **kwargs)
        fields.pop('id', None)
        fields.pop('deleted', None)
        fields.pop('deleted_by_cascade', None)


        return fields


    def to_representation(self, instance):
        representation = super().to_representation(instance)
        del representation['marche']
        return representation





class AttachementsSerializer(serializers.ModelSerializer):
    code_tache = serializers.CharField(source='dqe.code_tache', read_only=True, label="Code Tache")
    libelle_tache = serializers.CharField(source='dqe.libelle', read_only=True, label="Designation")
    unite = serializers.CharField(source='dqe.unite.libelle', read_only=True, label="Unite")
    montant_precedent = serializers.SerializerMethodField()
    montant_cumule = serializers.SerializerMethodField()
    qte_precedente = serializers.SerializerMethodField()
    qte_cumule = serializers.SerializerMethodField()

    def get_montant_precedent(self, obj):
        return 0

    def get_montant_cumule(self, obj):
        return obj.montant_cumule

    def get_qte_precedente(self, obj):
        return obj.qte_precedente

    def get_qte_cumule(self, obj):
        return obj.qte_cumule


    def get_fields(self, *args, **kwargs):
        fields = super().get_fields(*args, **kwargs)
        fields.pop('deleted', None)
        fields.pop('deleted_by_cascade', None)

        return fields


    class Meta:
        model = Attachements
        fields ='__all__'




class RemboursementSerializer(serializers.ModelSerializer):
    montant_creance=serializers.SerializerMethodField()

    def get_montant_creance(self, obj):
        return obj.montant_creance
    class Meta:
        model = Remboursement
        fields = '__all__'

    def get_fields(self, *args, **kwargs):
        fields = super().get_fields(*args, **kwargs)
        fields.pop('deleted', None)
        fields.pop('deleted_by_cascade', None)
        fields.pop('id', None)


        return fields

