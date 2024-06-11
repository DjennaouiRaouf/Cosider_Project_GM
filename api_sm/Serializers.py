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

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if instance.code_filiale:
            representation['code_filiale'] = instance.code_filiale.libelle
        else:
            representation['code_filiale'] = None

        if instance.code_agence:
            representation['code_agence'] = instance.code_agence.libelle
        else:
            representation['code_agence'] = None

        if instance.code_division:
            representation['code_division'] = instance.code_division.libelle
        else:
            representation['code_division'] = None

        return representation

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
        fields.pop('est_bloquer', None)
        fields.pop('user_id', None)
        fields.pop('date_modification', None)
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
        fields.pop('est_bloquer', None)
        fields.pop('user_id', None)
        fields.pop('date_modification', None)

        return fields


class DQEAvenantSerializer(serializers.ModelSerializer):
    prix_q = serializers.SerializerMethodField(label="Montant")
    pole = serializers.PrimaryKeyRelatedField(source='code_site', queryset=Sites.objects.all(), label='Pole')
    def get_prix_q(self, obj):
        return obj.prix_q


    class Meta:
        model = DQEAvenant
        fields = ['pole', 'nt', 'code_tache','num_avenant','libelle', 'est_tache_composite', 'est_tache_complementaire', 'prix_u',
                  'quantite', 'unite', 'prix_q','lib_activite']

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
        fields = ['id','code_site','nt','num_avenant','libelle','ods_depart','date_signature','delais','delai_paiement_f','revisable','rabais','rg'
            ,'tva','montant_ht','montant_ttc']


    def get_fields(self, *args, **kwargs):
        fields = super().get_fields(*args, **kwargs)
        fields.pop('est_bloquer', None)
        fields.pop('user_id', None)
        fields.pop('date_modification', None)
        return fields
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['ht'] = instance.ht
        representation['ttc'] = instance.ttc

        return representation


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
        fields = ['id','code_site','nt','num_avenant','libelle','ods_depart','date_signature','delais','delai_paiement_f','revisable','rabais','rg'
            ,'tva','montant_ht','montant_ttc']


    def get_fields(self, *args, **kwargs):
        fields = super().get_fields(*args, **kwargs)
        fields.pop('est_bloquer', None)
        fields.pop('user_id', None)
        fields.pop('date_modification', None)
        return fields
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['ht'] = instance.ht
        representation['ttc'] = instance.ttc

        return representation






class MarcheAvenantSerializer(serializers.ModelSerializer):
    id=serializers.CharField(label='Contrat N°')
    num_avenant = serializers.CharField(label='Avenant N°')
    code_site=serializers.PrimaryKeyRelatedField(queryset=Sites.objects.all().distinct(),label='Pole')
    nt=serializers.CharField(label='NT')
    montant_ht = serializers.SerializerMethodField(label='Montant en HT')
    montant_ttc = serializers.SerializerMethodField(label='Montant en TTC')

    def get_montant_ht(self, obj):
        return obj.ht

    def get_montant_ttc(self, obj):
        return obj.ttc

    class Meta:
        model = MarcheAvenant
        fields = ['id','num_avenant','code_site','nt','num_avenant','libelle','ods_depart','date_signature','delais','delai_paiement_f','revisable','rabais','rg'
            ,'tva','montant_ht','montant_ttc']


    def get_fields(self, *args, **kwargs):
        fields = super().get_fields(*args, **kwargs)
        fields.pop('est_bloquer', None)
        fields.pop('user_id', None)
        fields.pop('date_modification', None)
        return fields
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        return representation



class FactureSerializer(serializers.ModelSerializer):
    somme=serializers.SerializerMethodField(label="Arretée la présenta facture à la somme de")
    ava=serializers.SerializerMethodField(label="Montant AV.A Remb")
    avf=serializers.SerializerMethodField(label="Montant AV.F Remb")

    ave=serializers.SerializerMethodField(label="Montant AV.E Remb")
    montant_precedent=serializers.SerializerMethodField(label="Montant Precedent")
    montant_cumule=serializers.SerializerMethodField(label="Montant Cumule")

    montant_factureHT = serializers.SerializerMethodField(label="Montant en HT")
    montant_factureTTC = serializers.SerializerMethodField(label="Montant en TTC")
    penalite = serializers.FloatField(label="Penalite",read_only=True)


    class Meta:
        model=Factures
        fields=['marche','numero_facture','num_situation','date','du', 'au','montant_precedent'
            ,'montant','montant_cumule','montant_rb','montant_rg','ava','avf','ave','penalite','montant_factureHT','montant_factureTTC','somme','paye']



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
    def get_ave(self,obj):
        return obj.montant_ave_remb

    def get_fields(self, *args, **kwargs):
        fields = super().get_fields(*args, **kwargs)
        fields.pop('est_bloquer', None)
        fields.pop('user_id', None)
        fields.pop('date_modification', None)
       

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
        fields.pop('est_bloquer', None)
        fields.pop('user_id', None)
        fields.pop('date_modification', None)


        return fields


    def to_representation(self, instance):
        representation = super().to_representation(instance)
        return representation



class EncaissementSerializer(serializers.ModelSerializer):
    class Meta:
        model=Encaissement
        fields=['id','facture','date_encaissement','mode_paiement','agence','numero_piece']


    def get_fields(self, *args, **kwargs):
        fields = super().get_fields(*args, **kwargs)
        fields.pop('est_bloquer', None)
        fields.pop('user_id', None)
        fields.pop('date_modification', None)
        return fields


    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['montant_creance']=instance.montant_creance
        representation['montant_encaisse'] = instance.montant_encaisse
        representation['agence'] = instance.agence.libelle
        representation['facture']=instance.facture.numero_facture
        representation['mode_paiement'] = instance.mode_paiement.libelle
        return representation







class DetailFactureSerializer(serializers.ModelSerializer):
    code_tache=serializers.SerializerMethodField(label='Code Tache')
    libelle=serializers.SerializerMethodField(label='Libelle')
    qte = serializers.SerializerMethodField(label='Quantite')
    montant = serializers.SerializerMethodField(label='Montant')
    date=serializers.SerializerMethodField(label='Date')
    prix_u = serializers.SerializerMethodField(label='Prix Unitaire')
    unite = serializers.SerializerMethodField(label='Unite')
    def get_code_tache(self, obj):
        return obj.detail.code_tache

    def get_libelle(self, obj):
        dqe=DQE.objects.get(code_site=obj.detail.code_site,code_tache=obj.detail.code_tache,nt=obj.detail.nt)
        return dqe.libelle
    def get_qte(self, obj):
        return obj.detail.qte
    def get_montant(self, obj):
        return obj.detail.montant
    def get_date(self, obj):
        return obj.detail.date

    def get_prix_u(self, obj):
        return obj.detail.prix_u

    def get_unite(self,obj):
        dqe = DQE.objects.get(code_site=obj.detail.code_site, code_tache=obj.detail.code_tache, nt=obj.detail.nt)
        return dqe.unite.libelle

    class Meta:
            model=DetailFacture
            fields=['code_tache','libelle','prix_u','qte','montant','date','unite']

    def get_fields(self, *args, **kwargs):
        fields = super().get_fields(*args, **kwargs)
        fields.pop('est_bloquer', None)
        fields.pop('user_id', None)
        fields.pop('date_modification', None)

        return fields


    def to_representation(self, instance):
        representation = super().to_representation(instance)
        return representation



class AvanceSerializer(serializers.ModelSerializer):
    taux_avance=serializers.SerializerMethodField(label='Taux d\'avance')
    taux_remb = serializers.SerializerMethodField(label='Taux de Remboursement')

    def get_taux_avance(self,obj):
        return obj.taux_avance
    def get_taux_remb(self,obj):
        return obj.taux_remb
    class Meta:
            model=Avance
            fields=['id','type','num_avance','montant','taux_avance','debut','fin','taux_remb','date','marche']

    def get_fields(self, *args, **kwargs):
        fields = super().get_fields(*args, **kwargs)
        fields.pop('est_bloquer', None)
        fields.pop('user_id', None)
        fields.pop('date_modification', None)

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
        fields.pop('est_bloquer', None)
        fields.pop('user_id', None)
        fields.pop('date_modification', None)

        return fields


    def to_representation(self, instance):
        representation = super().to_representation(instance)
        return representation






class CautionSerializer(serializers.ModelSerializer):

    class Meta:
            model=Cautions
            fields=['id','type','avance','montant','agence','date_soumission','marche','est_recupere']


    def get_fields(self, *args, **kwargs):
        fields = super().get_fields(*args, **kwargs)
        fields.pop('est_bloquer', None)
        fields.pop('user_id', None)
        fields.pop('date_modification', None)
        return fields


    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['type']=instance.type.libelle
        if (instance.avance):
            representation['avance']=instance.avance.type.libelle
        else:
            representation['avance'] = None
        return representation

class TypeCautionSerializer(serializers.ModelSerializer):
    class Meta:
        model=TypeCaution
        fields='__all__'
    def get_fields(self, *args, **kwargs):
        fields = super().get_fields(*args, **kwargs)

        fields.pop('est_bloquer', None)
        fields.pop('user_id', None)
        fields.pop('date_modification', None)

        return fields


    def to_representation(self, instance):
        representation = super().to_representation(instance)
        return representation




class AttachementsSerializer(serializers.ModelSerializer):
    libelle = serializers.CharField(read_only=True, label="Designation")
    unite = serializers.CharField(read_only=True, label="Unite")
    montant_precedent = serializers.SerializerMethodField(label="Montant Precedent")
    montant_cumule = serializers.SerializerMethodField(label="Montant Cumule")
    qte_precedente = serializers.SerializerMethodField(label="Qte Precedente")
    qte_cumule = serializers.SerializerMethodField(label="Qte Cumulée")

    def get_montant_precedent(self, obj):
        return obj.montant_precedent

    def get_montant_cumule(self, obj):
        return obj.montant_cumule

    def get_qte_precedente(self, obj):
        return obj.qte_precedente

    def get_qte_cumule(self, obj):
        return obj.qte_cumule


    def get_fields(self, *args, **kwargs):
        fields = super().get_fields(*args, **kwargs)
        fields.pop('est_bloquer', None)
        fields.pop('user_id', None)
        fields.pop('date_modification', None)
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
    montant_cumule=serializers.SerializerMethodField()
    rest = serializers.SerializerMethodField()

    def get_montant_cumule(self, obj):
        return obj.montant_cumule

    def get_rest(self, obj):
        return obj.rst_remb

    class Meta:
        model = Remboursement
        fields = '__all__'

    def get_fields(self, *args, **kwargs):
        fields = super().get_fields(*args, **kwargs)
        fields.pop('est_bloquer', None)
        fields.pop('user_id', None)
        fields.pop('date_modification', None)
        fields.pop('id', None)


        return fields




class ECSerializer(serializers.ModelSerializer):
    nt = serializers.SerializerMethodField(label='NT',read_only=True)
    code_site = serializers.SerializerMethodField(label='code_site', read_only=True)

    client = serializers.SerializerMethodField(label='Client',read_only=True)

    mgf = serializers.SerializerMethodField(label='M.G.Facturé')
    mgp = serializers.SerializerMethodField(label='M.G.Payé')
    mgc = serializers.SerializerMethodField(label='M.G.Créance')

    def get_nt(self,obj):
        return obj.nt

    def get_code_site(self, obj):
        return obj.code_site
    def get_client(self, obj):
        n=NT.objects.get(nt=obj.nt,code_site=obj.code_site)
        return n.code_client

    def get_mgf(self, obj):
        return obj.montant_global_f

    def get_mgp(self, obj):
        return obj.montant_global_p


    def get_mgc(self, obj):
        return obj.montant_global_c

    class Meta:
        model = Marche
        fields = ['id','nt','code_site','client','mgf','mgp','mgc']

    def to_representation(self, instance):
        representation = super().to_representation(instance)


        return representation




class PSSerializer(serializers.ModelSerializer):
    libelle=serializers.SerializerMethodField(label='Libelle')
    unite=serializers.SerializerMethodField(label='Unite')


    def get_libelle(self,obj):
        try:
            dqe=DQE.objects.get(code_site=obj.code_site,nt=obj.nt,code_tache=obj.code_tache)
            if(dqe):
                return dqe.libelle
            else:
                return None
        except DQE.DoesNotExist:
            return None

    def get_unite(self,obj):
        try:
            dqe=DQE.objects.get(code_site=obj.code_site,nt=obj.nt,code_tache=obj.code_tache)
            if(dqe):
                return dqe.unite.libelle
            else:
                return None
        except DQE.DoesNotExist:
            return None
    class Meta:
        model = ProductionStockee
        fields = ['code_site','nt','code_tache','libelle','qte_prod','qte_att','ecart','unite','ind']
    def to_representation(self, instance):
        representation = super().to_representation(instance)


        return representation