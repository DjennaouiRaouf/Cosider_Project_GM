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


class ClientsSerializer(serializers.ModelSerializer):
    def get_fields(self, *args, **kwargs):
        fields = super().get_fields(*args, **kwargs)
       
        fields.pop('est_bloquer', None)
        fields.pop('user_id', None)
        fields.pop('date_modification', None)
        return fields



    class Meta:
        model = Clients
        fields = '__all__'



class SiteSerializer(serializers.ModelSerializer):
    def get_fields(self, *args, **kwargs):
        fields = super().get_fields(*args, **kwargs)
        fields.pop('est_bloquer', None)
        fields.pop('user_id', None)
        fields.pop('date_modification', None)
        fields.pop('jour_cloture_mouv_rh_paie',None)

        return fields


    class Meta:
        model = Sites
        fields = '__all__'










class NTSerializer(serializers.ModelSerializer):
    site=serializers.PrimaryKeyRelatedField(source='code_site',queryset=Sites.objects.all(), label='Pole')
    client=serializers.PrimaryKeyRelatedField(source='code_client',queryset=Clients.objects.all(), label='Client')


    class Meta:
        model=NT
        fields =['site','nt','client','code_situation_nt','libelle','date_ouverture_nt','date_cloture_nt']




    def get_fields(self, *args, **kwargs):
        fields = super().get_fields(*args, **kwargs)
        return fields
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if instance.code_situation_nt:
            representation['code_situation_nt'] = instance.code_situation_nt.libelle
        else:
            representation['code_situation_nt'] = None

        return representation



class DQESerializer(serializers.ModelSerializer):
    prix_q = serializers.SerializerMethodField(label="Montant")
    pole= serializers.PrimaryKeyRelatedField(source='code_site',queryset=Sites.objects.all(), label='Pole')



    def get_prix_q(self, obj):
        return obj.prix_q

    class Meta:
        model=DQE
        fields=['pole','nt','code_tache','libelle','est_tache_composite','est_tache_complementaire','prix_u','quantite','unite','prix_q']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if instance.unite:
            representation['unite'] = instance.unite.libelle
        else:
            representation['unite'] = None

        return representation

    def get_fields(self, *args, **kwargs):
        fields = super().get_fields(*args, **kwargs)
       

        return fields




class MarcheSerializer(serializers.ModelSerializer):
    code_site=serializers.PrimaryKeyRelatedField(queryset=Sites.objects.all().distinct(),label='Site')
    nt=serializers.CharField(label='NT')
    montant_ht = serializers.SerializerMethodField(label='Montant en HT')
    montant_ttc = serializers.SerializerMethodField(label='Montant en TTC')

    def get_montant_ht(self, obj):
        return obj.ht

    def get_montant_ttc(self, obj):
        return obj.ttc

    class Meta:
        model = Marche
        fields = ['id','code_site','nt','libelle','ods_depart','date_signature','delais','delai_paiement_f','revisable','rabais','rg'
            ,'tva','montant_ht','montant_ttc']





    def get_fields(self, *args, **kwargs):
        fields = super().get_fields(*args, **kwargs)
        return fields
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['ht'] = instance.ht
        representation['ttc'] = instance.ttc



        return representation






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
    montant_factureHT=serializers.SerializerMethodField(label="Montant en HT")
    montant_factureTTC=serializers.SerializerMethodField(label="Montant en TTC")
    ava=serializers.SerializerMethodField(label="Montant AV.A Remb")
    avf=serializers.SerializerMethodField(label="Montant AV.F Remb")
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
    def get_montant_factureHT(self,obj):
        return obj.montant_factureHT
    def get_montant_factureTTC(self,obj):
        return obj.montant_factureTTC
    def get_ava(self,obj):
        return obj.montant_ava_remb
    def get_avf(self,obj):
        return obj.montant_avf_remb

    def get_fields(self, *args, **kwargs):
        fields = super().get_fields(*args, **kwargs)
       

        return fields


    def to_representation(self, instance):
        representation = super().to_representation(instance)

        return representation





class ModePaiementSerializer(serializers.ModelSerializer):
    class Meta:
        model=ModePaiement
        fields='__all__'
    def get_fields(self, *args, **kwargs):
        fields = super().get_fields(*args, **kwargs)

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
            fields='__all_'
    def get_fields(self, *args, **kwargs):
        fields = super().get_fields(*args, **kwargs)
        fields.pop('id', None)
       


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
       
        return fields


    def to_representation(self, instance):
        representation = super().to_representation(instance)
        return representation

class TypeCautionSerializer(serializers.ModelSerializer):
    class Meta:
        model=TypeCaution
        fields='__all__'
    def get_fields(self, *args, **kwargs):
        fields = super().get_fields(*args, **kwargs)
       


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
       


        return fields


    def to_representation(self, instance):
        representation = super().to_representation(instance)
        del representation['marche']
        return representation





class AttachementsSerializer(serializers.ModelSerializer):
    libelle = serializers.CharField(read_only=True, label="Designation")
    unite = serializers.CharField(read_only=True, label="Unite")
    montant_precedent = serializers.SerializerMethodField(label="Montant Precedent")
    montant_cumule = serializers.SerializerMethodField(label="Montant Cumule")
    qte_precedente = serializers.SerializerMethodField(label="Qte Precedente")
    qte_cumule = serializers.SerializerMethodField(label="Qte Cumulée")

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
        return fields

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        dqe=DQE.objects.get(nt=instance.nt,code_site=instance.code_site,code_tache=instance.code_tache)
        representation['libelle'] = dqe.libelle
        representation['unite'] = dqe.unite.libelle

        return representation


    class Meta:
        model = Attachements
        fields =['id','code_site','nt','code_tache','libelle','unite','qte_precedente','qte','qte_cumule','montant_precedent','montant','montant_cumule']




class RemboursementSerializer(serializers.ModelSerializer):
    montant_creance=serializers.SerializerMethodField()

    def get_montant_creance(self, obj):
        return obj.montant_creance
    class Meta:
        model = Remboursement
        fields = '__all__'

    def get_fields(self, *args, **kwargs):
        fields = super().get_fields(*args, **kwargs)
       
        fields.pop('id', None)


        return fields




class ECSerializer(serializers.ModelSerializer):
    nt = serializers.PrimaryKeyRelatedField(source="nt.nt",label='NT',read_only=True)
    client = serializers.PrimaryKeyRelatedField(source="nt.code_client",label='Client',read_only=True)

    mgf = serializers.SerializerMethodField(label='M.G.Facturé')
    mgp = serializers.SerializerMethodField(label='M.G.Payé')
    mgc = serializers.SerializerMethodField(label='M.G.Créance')

    def get_mgf(self, obj):
        return obj.montant_global_f

    def get_mgp(self, obj):
        return obj.montant_global_p


    def get_mgc(self, obj):
        return obj.montant_global_c

    class Meta:
        model = Marche
        fields = ['id','nt','client','mgf','mgp','mgc']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['client'] = instance.nt.code_client.libelle


        return representation
