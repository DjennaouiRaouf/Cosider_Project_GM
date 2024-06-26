import json
import pandas
import openpyxl
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import check_password
from django.db import IntegrityError
from django.db.models import Count, Sum, Min, Max
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.exceptions import NotFound
from rest_framework.mixins import DestroyModelMixin
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from .Filters import *
from .Serializers import *
from .models import *
from .tools import *
from django.db.models import F, Value, CharField
from django.db.models.functions import Concat, Cast


class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class LoginView(APIView):
    permission_classes = []

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        app_name = 'api_sm'

        if user is not None:
            Token.objects.filter(user=user).delete()
            token, created = Token.objects.get_or_create(user=user)
            app_permissions = self.get_app_permissions(user, app_name)
            response = Response(status=status.HTTP_200_OK)
            role = '|'.join(list(app_permissions))
            response.set_cookie('token', token.key)
            response.set_cookie('role', role)
            return response
        else:
            return Response({'message': 'Informations d’identification non valides'},
                            status=status.HTTP_400_BAD_REQUEST)

    def get_app_permissions(self, user, app_name):
        # Get all permissions for the specified app
        all_permissions = user.get_all_permissions()
        app_permissions = set()

        for permission in all_permissions:
            if permission.split('.')[0] == app_name:
                app_permissions.add(permission)

        return app_permissions


class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        Token.objects.get(user_id=request.user.id).delete()
        response = Response({'message': 'Vous etes déconnecté'}, status=status.HTTP_200_OK)
        response.delete_cookie('token')
        response.delete_cookie('role')
        return response


class WhoamiView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({'whoami': request.user.username}, status=status.HTTP_200_OK)


class AjoutClientApiView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated, AddClientPermission]
    queryset = Clients.objects.all()
    serializer_class = ClientsSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        self.perform_create(serializer)
        custom_response = {
            'status': 'success',
            'message': 'Client ajouté',
            'data': serializer.data,
        }

        return Response(custom_response, status=status.HTTP_201_CREATED)


class GetClientsView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated, ViewClientPermission]
    queryset = Clients.objects.all()
    serializer_class = ClientsSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ClientsFilter


class AjoutSiteApiView(generics.CreateAPIView):
    # permission_classes = [IsAuthenticated,AddSitePermission]

    queryset = Sites.objects.all()
    serializer_class = SiteSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        self.perform_create(serializer)
        custom_response = {
            'status': 'success',
            'message': 'Site ajouté',
            'data': serializer.data,
        }
        return Response(custom_response, status=status.HTTP_201_CREATED)


class AjoutMarcheApiView(generics.CreateAPIView):
    # permission_classes = [IsAuthenticated, AddMarchePermission]

    queryset = Marche.objects.all()
    serializer_class = MarcheSerializer

    def create(self, request, *args, **kwargs):

        serializer = self.get_serializer(data=request.data)
        revisable = False
        try:
            revisable = serializer.initial_data['revisable']
            print(revisable)
        except Exception as e:
            revisable = False

        try:

            Marche(id=serializer.initial_data['id'], code_site=serializer.initial_data['code_site'],
                   nt=serializer.initial_data['nt'],
                   libelle=serializer.initial_data['libelle'], ods_depart=serializer.initial_data['ods_depart'],

                   delai_paiement_f=serializer.initial_data['delai_paiement_f'],
                   rabais=serializer.initial_data['rabais'] or 0, tva=serializer.initial_data['tva'] or 0,
                   rg=serializer.initial_data['rg'],
                   date_signature=serializer.initial_data['date_signature']).save(
                force_insert=True)
            try:
                m = Marche.objects.get(id=serializer.initial_data['id'])

                if (m.num_avenant == 0):
                    MarcheAvenant(id=m.id, code_site=m.code_site, nt=m.nt,
                                  libelle=m.libelle, ods_depart=m.ods_depart,
                                  num_avenant=m.num_avenant,
                                  delai_paiement_f=m.delai_paiement_f,
                                  rabais=m.rabais or 0, tva=m.tva or 0, rg=m.rg,
                                  date_signature=m.date_signature).save(
                        force_insert=True)
            except:
                pass

            return Response('Marché ajouté', status=status.HTTP_200_OK)
        except IntegrityError as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)


class AjoutDQEApiView(generics.CreateAPIView):
    # permission_classes = [IsAuthenticated, AddDQEPermission]
    queryset = DQE.objects.all()
    serializer_class = DQESerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        print(serializer.initial_data)

        try:
            DQE(code_site=serializer.initial_data['pole'], nt=serializer.initial_data['nt'],
                code_tache=serializer.initial_data['code_tache'], prix_u=serializer.initial_data['prix_u'],
                est_tache_composite=serializer.initial_data['est_tache_composite'],
                est_tache_complementaire=serializer.initial_data['est_tache_complementaire'],
                quantite=serializer.initial_data['quantite'],
                unite=TabUniteDeMesure.objects.get(id=serializer.initial_data['unite']),
                libelle=serializer.initial_data['libelle']).save(force_insert=True)
            try:
                m = Marche.objects.get(nt=serializer.initial_data['nt'], code_site=serializer.initial_data['pole'])
                print(m.num_avenant)
                if (m.num_avenant == 0):
                    DQEAvenant(code_site=serializer.initial_data['pole'], num_avenant=m.num_avenant,
                               nt=serializer.initial_data['nt'],
                               code_tache=serializer.initial_data['code_tache'],
                               prix_u=serializer.initial_data['prix_u'],
                               est_tache_composite=serializer.initial_data['est_tache_composite'],
                               est_tache_complementaire=serializer.initial_data['est_tache_complementaire'],
                               quantite=serializer.initial_data['quantite'],
                               unite=TabUniteDeMesure.objects.get(id=serializer.initial_data['unite']), libelle=
                               serializer.initial_data['libelle']).save(force_insert=True)
            except:
                pass

            return Response('Tache ajoutée', status=status.HTTP_200_OK)
        except IntegrityError as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)


class GetSitesView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated, ViewSitePermission]

    queryset = Sites.objects.all()
    serializer_class = SiteSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = SitesFilter


class GetMarcheView(generics.ListAPIView):
    # permission_classes = [permissions.IsAuthenticated, ViewMarchePermission]
    queryset = Marche.objects.all()
    serializer_class = MarcheSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = MarcheFilter


class GetProdParams(APIView):
    def get(self, request):
        id = request.query_params.get('id', None)
        marche = Marche.objects.get(id=id)
        ms = MarcheSerializer(marche, many=False).data
        return Response({'cs': ms['code_site'], 'nt': ms['nt']}, status=status.HTTP_200_OK)


class GetDQEView(generics.ListAPIView):
    # permission_classes = [permissions.IsAuthenticated,ViewDQEPermission]
    queryset = DQE.objects.all()
    serializer_class = DQESerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = DQEFilter

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        mt = 0
        response_data = super().list(request, *args, **kwargs).data
        for q in queryset:
            mt = mt + q.prix_q

        return Response({'dqe': response_data,
                         'extra': {
                             'mt': mt,

                         }}, status=status.HTTP_200_OK)


class ImportDQEAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        dqe_file = request.FILES['file']
        nt = request.data.get('nt')
        cs = request.data.get('cs')
        try:
            m = Marche.objects.get(nt=nt, code_site=cs)
            df = pandas.read_excel(dqe_file, engine='openpyxl')
            for index, row in df.iterrows():
                try:
                    try:
                        if (m.num_avenant == 0):
                            DQE(
                                code_site=cs, nt=nt,
                                code_tache=row['code_tache'], prix_u=row['prix_u'],
                                unite=TabUniteDeMesure.objects.get(libelle=row['unite']),
                                libelle=row['libelle'], quantite=row['quantite'], user_id=request.user.username).save(
                                force_insert=True)

                    except:
                        pass
                except IntegrityError as e:
                    try:
                        if (m.num_avenant == 0):
                            DQE(
                                code_site=cs, nt=nt,
                                code_tache=row['code_tache'], prix_u=row['prix_u'],
                                unite=TabUniteDeMesure.objects.get(libelle=row['unite']),
                                libelle=row['libelle'], quantite=row['quantite'], user_id=request.user.username).save(force_update=True)


                    except:
                        pass

                try:
                    if (m.num_avenant == 0):
                        DQEAvenant(
                            num_avenant=m.num_avenant,
                            code_site=cs, nt=nt,
                            code_tache=row['code_tache'], prix_u=row['prix_u'],
                            unite=TabUniteDeMesure.objects.get(libelle=row['unite']),
                            libelle=row['libelle'], quantite=row['quantite'], user_id=request.user.username
                        ).save(force_insert=True)
                except IntegrityError as e:
                    if (m.num_avenant == 0):
                        DQEAvenant(
                            num_avenant=m.num_avenant,
                            code_site=cs, nt=nt,
                            code_tache=row['code_tache'], prix_u=row['prix_u'],
                            unite=TabUniteDeMesure.objects.get(libelle=row['unite']),
                            libelle=row['libelle'], quantite=row['quantite'], user_id=request.user.username
                        ).save(force_update=True)

            return Response(f'Mise à jour',
                            status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)


class GetNTView(generics.ListAPIView):
    # permission_classes = [IsAuthenticated,ViewNTPermission]
    queryset = NT.objects.all()
    serializer_class = NTSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = NTFilter


class AjoutNTApiView(generics.CreateAPIView):
    # permission_classes = [IsAuthenticated, AddNTPermission]
    queryset = NT.objects.all()
    serializer_class = NTSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        print(serializer.initial_data)

        try:
            NT(code_site=serializer.initial_data['site'], nt=serializer.initial_data['nt'],
               code_client=Clients.objects.get(id=serializer.initial_data['client']),
               code_situation_nt=TabSituationNt.objects.get(id=serializer.initial_data['code_situation_nt']),
               libelle=serializer.initial_data['libelle'],
               date_ouverture_nt=serializer.initial_data['date_ouverture_nt']).save(force_insert=True)
            return Response('NT ajoutée', status=status.HTTP_200_OK)
        except IntegrityError as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)


class GetDQEbyId(generics.ListAPIView):
    queryset = DQE.objects.all()
    serializer_class = DQESerializer
    lookup_field = 'marche'

class GetRemb(generics.ListAPIView):
    queryset = Remboursement.objects.all().order_by('facture')
    serializer_class = FactureSerializer


class GetFacture(generics.ListAPIView):
    queryset = Factures.objects.all().order_by('num_situation')
    serializer_class = FactureSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = FactureFilter

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        rg_total = 0
        mgf = 0
        enc = 0
        mgp=0
        ava_remb_c=0
        avf_remb_c=0
        ave_remb_c=0
        response_data = super().list(request, *args, **kwargs).data
        for q in queryset:
            rg_total += q.montant_rg
            mgf += q.montant_factureTTC
            mgp += q.penalite
            ava_remb_c = (Remboursement.objects.filter(avance__type='A', facture__marche_id=q.marche.id).aggregate(total=Sum('montant'))[
                            'total'] or 0)
            avf_remb_c = (Remboursement.objects.filter(avance__type='F', facture__marche_id=q.marche.id).aggregate(total=Sum('montant'))[
                            'total'] or 0)
            ave_remb_c = (Remboursement.objects.filter(avance__type='E', facture__marche_id=q.marche.id).aggregate(total=Sum('montant'))[
                            'total'] or 0)

            try:
                enc += (Encaissement.objects.filter(facture=q).distinct().aggregate(total=Sum('montant_encaisse'))[
                            'total'] or 0)
            except Encaissement.DoesNotExist:
                pass


        creance = mgf - enc


        m = Marche.objects.get(nt=self.request.query_params.get('marche__nt', None),
                               code_site=self.request.query_params.get('marche__code_site', None))
        n = NT.objects.get(nt=self.request.query_params.get('marche__nt', None),
                           code_site=self.request.query_params.get('marche__code_site', None))


        return Response({'facture': response_data,
                         'extra': {

                             'contrat': m.id,
                             'mht':m.ht,
                             'mttc':m.ttc,
                             'tva':m.tva,
                             'rg':m.rg,
                             'rb':m.rabais,
                             'signature': m.date_signature,
                             'projet': m.libelle,
                             'montant_marche': m.ht,
                             'client': n.code_client,
                             'nt': n.nt,
                             'lib_nt': n.libelle,
                             'pole': n.code_site,
                             'rg_total': rg_total,
                             'rg_total_ttc': round(rg_total + (rg_total * m.tva / 100), 2),
                             'mgenc':enc,
                             'creance': creance,
                             'pen':mgp,
                             'mgf':mgf,
                             'ava':ava_remb_c,
                             'avf':avf_remb_c,
                             'ave':ave_remb_c,

                         }}, status=status.HTTP_200_OK)


class DeletedFacture(generics.ListAPIView):
    queryset = Factures.objects.all()
    serializer_class = FactureSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = FactureFilter


class GetEncaissement(generics.ListAPIView):
    queryset = Encaissement.objects.all()
    serializer_class = EncaissementSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = EncaissementFilter


class GetEncaissementRG(generics.ListAPIView):
    queryset = EncaissementsRg.objects.all().order_by('date_encaissement')
    serializer_class = EncaissementRGSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = EncaissementRGFilter

class getDetFacture(generics.ListAPIView):
    queryset = DetailFacture.objects.all()
    serializer_class = DetailFactureSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = DetailFactureFilter

    def list(self, request, *args, **kwargs):
        # Apply filtering
        queryset = self.filter_queryset(self.get_queryset())

        # Call the parent class's list method to get the default response
        response_data = super().list(request, *args, **kwargs).data

        return Response({'detail': response_data,
                         'extra': {

                             'code_contrat': queryset[0].facture.marche.id,
                             'signature': queryset[0].facture.marche.date_signature,
                             'projet': queryset[0].facture.marche.libelle,
                             'montant_marche': queryset[0].facture.marche.ht,
                             'client': queryset[0].facture.marche.nt.code_client.id,
                             'nt': queryset[0].facture.marche.nt.nt,
                             'lib_nt': queryset[0].facture.marche.nt.libelle,
                             'pole': queryset[0].facture.marche.nt.code_site.id,

                         }}, status=status.HTTP_200_OK)


class GetFactureRG(generics.ListAPIView):
    queryset = DQE.objects.all()
    serializer_class = FactureSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = FactureFilter

    def list(self, request, *args, **kwargs):
        # Apply filtering
        queryset = self.filter_queryset(self.get_queryset())
        queryset = queryset.order_by("num_situation")

        # Call the parent class's list method to get the default response
        response_data = super().list(request, *args, **kwargs).data
        total = queryset.aggregate(montant_rg=models.Sum('montant_rg'))['montant_rg']
        return Response({'factures': FactureSerializer(queryset, many=True).data,
                         'extra': {
                             'total_rg': total,
                             'total_rgl': num2words(total, to='currency', lang='fr_DZ').upper(),
                             'code_contrat': queryset[0].marche.id,
                             'signature': queryset[0].marche.date_signature,
                             'projet': queryset[0].marche.libelle,
                             'montant_marche': queryset[0].marche.ht,
                             'client': queryset[0].marche.nt.code_client.id,
                             'nt': queryset[0].marche.nt.nt,
                             'lib_nt': queryset[0].marche.nt.libelle,
                             'pole': queryset[0].marche.nt.code_site.id,

                         }}, status=status.HTTP_200_OK)


class DelDQEByID(generics.DestroyAPIView):
    # permission_classes = [IsAuthenticated,DeleteDQEPermission]
    queryset = DQE.objects.all()
    serializer_class = DQESerializer

    def delete(self, request, *args, **kwargs):
        pk_list = request.data.get(DQE._meta.pk.name)
        if pk_list:
            queryset = self.filter_queryset(self.get_queryset())
            queryset = queryset.filter(pk__in=pk_list)
            self.perform_destroy(queryset)

        return Response({'Message': pk_list}, status=status.HTTP_200_OK)


class DelATT(generics.DestroyAPIView):
    # permission_classes = [IsAuthenticated]
    queryset = Attachements.objects.all()
    serializer_class = AttachementsSerializer
    def delete(self, request, *args, **kwargs):
        pks = self.request.data.get('id', [])
        print(pks)
        if pks:

            for pk in pks:
                try:
                    Attachements.objects.get(id=pk).delete()
                except Exception as e:
                    continue
        return Response(f'Les Attachements suivants {pks} sont Annulés', status=status.HTTP_200_OK)



class UpdateDQEApiVew(generics.UpdateAPIView):
    queryset = DQE.objects.all()
    serializer_class = DQESerializer

    def get_object(self):
        cs = self.request.data.get('pole')
        nt = self.request.data.get('nt')
        ct = self.request.data.get('code_tache')

        try:
            obj = DQE.objects.get(code_site=cs, nt=nt, code_tache=ct)
        except DQE.DoesNotExist:
            raise NotFound("Object n'éxiste pas")
        self.check_object_permissions(self.request, obj)

        return obj

    def update(self, request, *args, **kwargs):

        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data)
            m = Marche.objects.get(nt=serializer.initial_data['nt'], code_site=serializer.initial_data['pole'])
            if (m.num_avenant == 0):
                DQE(
                    code_site=serializer.initial_data['pole'],
                    code_tache=serializer.initial_data['code_tache'],
                    nt=serializer.initial_data['nt'],
                    libelle=serializer.initial_data['libelle'],
                    est_tache_composite=serializer.initial_data['est_tache_composite'],
                    est_tache_complementaire=serializer.initial_data['est_tache_complementaire'],
                    prix_u=serializer.initial_data['prix_u'],
                    quantite=serializer.initial_data['quantite'],
                    user_id=request.user.username,
                    unite=TabUniteDeMesure.objects.get(id=serializer.initial_data['unite']),
                ).save(force_update=True)

                try:
                    DQEAvenant(
                        num_avenant=m.num_avenant,
                        code_site=serializer.initial_data['pole'],
                        code_tache=serializer.initial_data['code_tache'],
                        nt=serializer.initial_data['nt'],
                        libelle=serializer.initial_data['libelle'],
                        est_tache_composite=serializer.initial_data['est_tache_composite'],
                        est_tache_complementaire=serializer.initial_data['est_tache_complementaire'],
                        prix_u=serializer.initial_data['prix_u'],
                        quantite=serializer.initial_data['quantite'],
                        user_id=request.user.username,
                        unite=TabUniteDeMesure.objects.get(id=serializer.initial_data['unite']),
                    ).save(force_update=True)
                except DQEAvenant.DoesNotExist:
                    pass
        except IntegrityError as e:
            print(e)
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)
        return Response('NT mis à jour avec succès', status=status.HTTP_200_OK)


class UpdateNTApiVew(generics.UpdateAPIView):
    queryset = NT.objects.all()
    serializer_class = NTSerializer
    lookup_url_kwarg = ['code_site', 'nt']

    def get_object(self):
        try:
            cs = self.request.data.get('site')
            nt = self.request.data.get('nt')
            obj = NT.objects.get(code_site=Sites.objects.get(id=cs), nt=nt)
        except NT.DoesNotExist:
            raise NotFound("Object n'éxiste pas")

        self.check_object_permissions(self.request, obj)
        return obj

    def update(self, request, *args, **kwargs):

        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data)

            instance.code_client = serializer.initial_data['client']
            instance.code_situation_nt = TabSituationNt.objects.get(id=serializer.initial_data['code_situation_nt'])
            instance.libelle = serializer.initial_data['libelle']
            instance.date_ouverture_nt = serializer.initial_data['date_ouverture_nt']
            instance.date_cloture_nt = serializer.initial_data['date_cloture_nt']
            instance.save(force_update=True)
        except IntegrityError as e:
            print(e)
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)
        return Response('NT mis à jour avec succès', status=status.HTTP_200_OK)


class AddFactureApiView(generics.CreateAPIView):
    queryset = Factures.objects.all()
    serializer_class = FactureSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        m = Marche.objects.get(nt=self.request.query_params.get('marche__nt', None),
                               code_site=self.request.query_params.get('marche__code_site', None))
        try:
            Factures(
                marche=m,
                du=serializer.initial_data['du'],
                au=serializer.initial_data['au'],
                numero_facture=serializer.initial_data['numero_facture'],
                num_situation=serializer.initial_data['num_situation'],
            ).save(force_insert=True)
            avances=Avance.objects.filter(marche=m,remboursee=False)
            for avance in avances:
                Remboursement(facture=Factures.objects.get(numero_facture=serializer.initial_data['numero_facture']),
                              avance=avance).save(force_insert=True)


            if(serializer.initial_data['penalite']):
                PenaliteRetard(facture=Factures.objects.get(numero_facture=serializer.initial_data['numero_facture']),
                               montant=serializer.initial_data['penalite']).save(force_insert=True)

            return Response('Facture ajoutée', status=status.HTTP_200_OK)

        except IntegrityError as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)


class AddEncaissementRG(generics.CreateAPIView):
    queryset = EncaissementsRg.objects.all()
    serializer_class = EncaissementRGSerializer


    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        print(serializer.initial_data)
        try:
            EncaissementsRg(
                nt=serializer.initial_data['nt'],
                code_site=serializer.initial_data['code_site'],
                date_encaissement=serializer.initial_data['date_encaissement'],
                montant_encaisse=serializer.initial_data['montant_encaisse'],
                numero_piece=serializer.initial_data['numero_piece'],
                mode_paiement= serializer.initial_data['mode_paiement'],
                code_agence= serializer.initial_data['code_agence']
            ).save(force_insert=True)

            return Response('Encaissement de la Retenue de Garantie Effectué', status=status.HTTP_200_OK)

        except IntegrityError as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)



class AddEncaissement(generics.CreateAPIView):
    queryset = Encaissement.objects.all()
    serializer_class = EncaissementSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        try:
            Encaissement(
                date_encaissement=serializer.initial_data['date_encaissement'],
                montant_encaisse=serializer.initial_data['montant_encaisse'],
                numero_piece=serializer.initial_data['numero_piece'],
                facture= Factures.objects.get(numero_facture=serializer.initial_data['facture']),
                mode_paiement= ModePaiement.objects.get(id=serializer.initial_data['mode_paiement']),
                agence= TabAgence.objects.get(id=serializer.initial_data['agence'])
            ).save(force_insert=True)

            return Response('Encaissement Effectué', status=status.HTTP_200_OK)

        except IntegrityError as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)


class UpdateMarcheView(generics.UpdateAPIView):
    queryset = Marche.objects.all()
    serializer_class = MarcheSerializer
    lookup_field = "id"

    def get_object(self):
        id = self.request.data.get('id')
        try:
            obj = Marche.objects.get(id=id)
        except Marche.DoesNotExist:
            raise NotFound("Object n'éxiste pas")

        self.check_object_permissions(self.request, obj)

        return obj

    def update(self, request, *args, **kwargs):

        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data)

            instance.ods_depart = serializer.initial_data['ods_depart']
            instance.delai_paiement_f = serializer.initial_data['delai_paiement_f']
            instance.rabais = serializer.initial_data['rabais']
            instance.tva = serializer.initial_data['tva']
            instance.rg = serializer.initial_data['rg']
            instance.date_signature = serializer.initial_data['date_signature']

            instance.save(force_update=True)
        except IntegrityError as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)

        return Response('Contrat mis à jour avec succès', status=status.HTTP_200_OK)


class LibMP(generics.ListAPIView):
    queryset = ModePaiement.objects.all()
    serializer_class = ModePaiementSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = MPFilter


class getDetailFacture(generics.ListAPIView):
    queryset = DetailFacture.objects.all()
    serializer_class = DetailFactureSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = DetailFactureFilter


class GetAvance(generics.ListAPIView):
    # permission_classes = [IsAuthenticated,ViewAvancePermission]
    queryset = Avance.objects.all()
    serializer_class = AvanceSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = AvanceFilter

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        ava = 0
        avf = 0
        ave = 0
        response_data = super().list(request, *args, **kwargs).data
        for q in queryset:
            if (q.type.id == 'F'):
                avf = avf + q.montant

            if (q.type.id == 'A'):
                ava = ava + q.montant

            if (q.type.id == 'E'):
                ave = ave + q.montant

        return Response({'av': response_data,
                         'extra': {
                             'ava': ava,
                             'avf': avf,
                             'ave':ave,
                         }}, status=status.HTTP_200_OK)


class LibAV(generics.ListAPIView):
    queryset = TypeAvance.objects.all()
    serializer_class = TypeAvanceSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = TypeAvanceFilter


class LibCaut(generics.ListAPIView):
    queryset = TypeCaution.objects.all()
    serializer_class = TypeCautionSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = TypeCautionFilter


class AddAvanceApiView(generics.CreateAPIView):
    # permission_classes = [IsAuthenticated,AddAvancePermission]
    queryset = Avance.objects.all()
    serializer_class = AvanceSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        cs = request.data.get('pole')
        nt = request.data.get('nt')
        m = Marche.objects.get(nt=nt, code_site=cs)

        try:
            Avance(montant=serializer.initial_data['montant'], marche=m,
                   debut=serializer.initial_data['debut'], fin=serializer.initial_data['fin'],
                   type=TypeAvance.objects.get(id=serializer.initial_data['type']),
                   date=serializer.initial_data['date']).save(force_insert=True)
            return Response('Avance ajoutée', status=status.HTTP_200_OK)
        except IntegrityError as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)


class GetCautions(generics.ListAPIView):
    queryset = Cautions.objects.all()
    serializer_class = CautionSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = CautionFilter

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        qr = 0
        qd = 0
        response_data = super().list(request, *args, **kwargs).data
        for q in queryset:
            if (q.est_recupere == True):
                qr = qr + q.montant

            if (q.est_recupere == False):
                qd = qd + q.montant

        return Response({'caut': response_data,
                         'extra': {
                             'qr': qr,
                             'qd': qd,

                         }}, status=status.HTTP_200_OK)


class AddCautions(generics.CreateAPIView):
    queryset = Cautions.objects.all()
    serializer_class = CautionSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        print(serializer.initial_data)
        nt = request.query_params.get('marche__nt', None)
        cs = request.query_params.get('marche__code_site', None)
        marche = Marche.objects.get(nt=nt, code_site=cs)
        print(marche.id)
        avance = None
        try:
            id_avance = serializer.initial_data['avance'] or 0
            avance = Avance.objects.get(id=id_avance)
        except Avance.DoesNotExist:
            avance = None
        try:
            Cautions(
                date_soumission=serializer.initial_data['date_soumission'],
                marche=marche,
                avance=avance,
                type=TypeCaution.objects.get(id=serializer.initial_data['type']),
                agence=TabAgence.objects.get(id=serializer.initial_data['agence']),
                montant=serializer.initial_data['montant']
            ).save(force_insert=True)
            return Response('Caution ajoutée', status=status.HTTP_200_OK)
        except IntegrityError as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)


class AddAttachementApiView(generics.CreateAPIView):
    queryset = Attachements.objects.all()
    serializer_class = AttachementsSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        for i in serializer.initial_data:
            marche = Marche.objects.get(code_site=i['code_site'], nt=i['nt'])
            print(marche.id)
            try:
                if(marche.revisable== True):
                    qte=(i['quantite_1']+i['quantite_2']+i['quantite_3'])*i['coefficient_revison']
                else:
                    qte = i['quantite_1'] + i['quantite_2'] + i['quantite_3']
                val=i['valeur_1']+i['valeur_2']+i['valeur_3']
                Attachements(code_site=i['code_site'], nt=i['nt'],
                             code_tache=i['code_tache'], date=i['mmaa'],
                             qte=qte,montant=val, marche=marche).save(force_insert=True)
            except IntegrityError as e:
                pass
        return Response('Attachement ajouté', status=status.HTTP_200_OK)


class GetAttachements(generics.ListAPIView):
    queryset = Attachements.objects.all()
    serializer_class = AttachementsSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = AttachementsFilter

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        qt = 0
        mt = 0
        mtp=0
        mtc=0
        response_data = super().list(request, *args, **kwargs).data
        m = Marche.objects.get(nt=self.request.query_params.get('nt', None),
                               code_site=self.request.query_params.get('code_site', None))

        s=Attachements.objects.filter(date__year__lte=self.request.query_params.get('aa',None)).filter(
            date__month__lt=self.request.query_params.get('mm',None)
        ).aggregate(total_amount=Sum('montant'))['total_amount']
        if(s is None):
            s=0

        for q in queryset:
            mt = mt + q.montant
            mtp = mtp+q.montant_precedent
            mtc= mtc+q.montant_cumule


        try:
            qt = ((mt + s) / m.ht) * 100
        except Exception as e:
            qt = 0

        txmt= (mt + mt * (m.tva / 100))
        txmtc= (mtc + mtc * (m.tva / 100))
        txmtp= (mtp + mtp * (m.tva / 100))
        nt = NT.objects.get(nt=self.request.query_params.get('nt', None),
                            code_site=self.request.query_params.get('code_site', None))
        return Response({'att': response_data,
                         'extra': {
                             'marche': m.id,
                             'nt': nt.nt,
                             'date': self.request.query_params.get('mm', None) + '/' + self.request.query_params.get(
                                 'aa', None),
                             'site': m.code_site,
                             'objet': m.libelle,
                             'client': nt.code_client,
                             'qt': qt,
                             'mt': mt,
                             'mtc':mtc,
                             'mtp':mtp,

                             'tva':m.tva,
                             'txmt': txmt,
                             'txmtc': txmtc,
                             'txmtp': txmtp,

                         }}, status=status.HTTP_200_OK)


class Poles(APIView):
    # permission_classes = [IsAuthenticated]
    def get(self, request):
        try:
           
            pole = Sites.objects.all().values_list('id', flat=True).distinct()
            return Response({'pole': pole}, status=status.HTTP_200_OK)
        except Marche.DoesNotExist:
            return Response({'message': 'Pas de contrat'}, status=status.HTTP_404_NOT_FOUND)



class NTs(APIView):
    # permission_classes = [IsAuthenticated]
    def get(self, request):
        try:
            cs=request.query_params.get('code_site', None)
            nt = NT.objects.filter(code_site=cs).values_list('nt', flat=True).distinct()
            return Response({'nt':nt}, status=status.HTTP_200_OK)
        except Marche.DoesNotExist:
            return Response({'message': 'Pas de contrat'}, status=status.HTTP_404_NOT_FOUND)



class NumAv(APIView):
    # permission_classes = [IsAuthenticated]
    def get(self, request):
        try:
            cs=request.query_params.get('code_site', None)
            nt = request.query_params.get('nt', None)
            num_av = MarcheAvenant.objects.filter(code_site=cs,nt=nt).values_list('num_avenant', flat=True).distinct()
            num_av = [str(num) for num in num_av]
            return Response({'num_av':num_av}, status=status.HTTP_200_OK)
        except Marche.DoesNotExist:
            return Response({'message': 'Pas de contrat'}, status=status.HTTP_404_NOT_FOUND)


class FlashMonths(APIView):
    # permission_classes = [IsAuthenticated]
    def get(self, request):
        try:
            cs = request.query_params.get('code_site', None)
            nt = request.query_params.get('nt', None)
            result = TabProduction.objects.filter(nt=nt, code_site=cs).aggregate(
                min_date=Min('mmaa'),
                max_date=Max('mmaa')
            )

            min_date = result['min_date']
            max_date = result['max_date']

            return Response({'min_date': min_date, 'max_date': max_date}, status=status.HTTP_200_OK)
        except TabProduction.DoesNotExist:
            return Response({'message': 'Pas de Production'}, status=status.HTTP_404_NOT_FOUND)


class AttMonths(APIView):
    # permission_classes = [IsAuthenticated]
    def get(self, request):
        try:
            cs = request.query_params.get('code_site', None)
            nt = request.query_params.get('nt', None)
            result = Attachements.objects.filter(nt=nt, code_site=cs).aggregate(
                min_date=Min('date'),
                max_date=Max('date')
            )

            min_date = result['min_date']
            max_date = result['max_date']

            return Response({'min_date': min_date, 'max_date': max_date}, status=status.HTTP_200_OK)
        except Attachements.DoesNotExist:
            return Response({'message': 'Pas de Production'}, status=status.HTTP_404_NOT_FOUND)


class CInvoice(APIView):
    # permission_classes = [IsAuthenticated]
    def get(self, request):
        try:
            keys = Factures.objects.filter(marche__id=self.request.query_params.get('marche', None)).values_list(
                'numero_facture', flat=True)
            return Response(keys, status=status.HTTP_200_OK)
        except Marche.DoesNotExist:
            return Response({'message': 'Pas de facture'}, status=status.HTTP_404_NOT_FOUND)


class GetECF(generics.ListAPIView):
    queryset = DQE.objects.all()
    serializer_class = FactureSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = FactureFilter

    def list(self, request, *args, **kwargs):
        # Apply filtering
        queryset = self.filter_queryset(self.get_queryset())
        queryset = queryset.order_by("num_situation")
        # Call the parent class's list method to get the default response
        response_data = super().list(request, *args, **kwargs).data
        avance = Avance.objects.filter(marche_id=self.request.query_params.get('marche', None))

        return Response({'factures': FactureSerializer(queryset, many=True).data,
                         'extra': {
                             'projet': queryset[0].marche.libelle,
                             'valeur': queryset[0].marche.ht,
                             'pole': queryset[0].marche.nt.code_site.id,
                             'tva': queryset[0].marche.tva,
                             'rabais': queryset[0].marche.rabais,
                             'rg': queryset[0].marche.rg,
                             'avance': AvanceSerializer(avance, many=True).data

                         }}, status=status.HTTP_200_OK)


class UpdateCautionApiView(generics.UpdateAPIView):
    queryset = Cautions.objects.all()
    serializer_class = CautionSerializer


    def get_object(self):
        id = self.request.data.get('id')
        print(id)
        try:
            obj = Cautions.objects.get(id=id)
        except Cautions.DoesNotExist:
            raise NotFound("Object n'éxiste pas")

        self.check_object_permissions(self.request, obj)

        return obj

    def update(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            instance.est_recupere=True
            instance.save(force_update=True)
            return Response('Caution Récupérée', status=status.HTTP_200_OK)
        except IntegrityError as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)

class DeleteInvoiceApiView(generics.DestroyAPIView):
    queryset = Factures.objects.all()
    serializer_class = FactureSerializer

    def delete(self, request, *args, **kwargs):
        pks = self.request.data.get('numero_facture', [])
        print(pks)
        if pks:

            for pk in pks:
                try:
                    Factures.objects.get(numero_facture=pk).delete()

                except Exception as e:
                    continue
        return Response('Facture Annulée', status=status.HTTP_200_OK)


class UserProfile(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        uid = request.user.id
        try:
            user = User.objects.get(id=uid)
            return Response({
                "full_name": user.get_full_name(),
                "username": user.username,
                "email": user.email,
                "joined": user.date_joined,
                "login": user.last_login,
                "current_password": '',
                "new_password": '',
                "confirm_new_password": '',

            }, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({"message": "Erreur ... !"}, status=status.HTTP_400_BAD_REQUEST)


class EditUserProfile(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        username = request.data.get('username')
        email = request.data.get('email')
        current_password = request.data.get('current_password')
        new_password = request.data.get('new_password')
        confirm_new_password = request.data.get('confirm_new_password')

        uid = request.user.id
        user = User.objects.get(id=uid)
        try:
            if (username):
                user.username = username

            if (email):
                user.email = email

            if (current_password and new_password and confirm_new_password):
                if (check_password(current_password, user.password)):
                    if (new_password != confirm_new_password):
                        return Response({"message": "Vous n'avez pas confirmé votre mot de passe"},
                                        status=status.HTTP_400_BAD_REQUEST)
                    else:

                        user.set_password(new_password)
                else:
                    return Response({"message": "Mot de pass incorrect"}, status=status.HTTP_400_BAD_REQUEST)

            user.save()
            return Response({"message": "Votre profile est mis à jour"}, status=status.HTTP_200_OK)

        except User.DoesNotExist:
            return Response({"message": "Erreur ... !"}, status=status.HTTP_400_BAD_REQUEST)


class WorkState(generics.ListAPIView):
    # permission_classes = [IsAuthenticated]
    queryset = Attachements.objects.all()
    serializer_class = AttachementsSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = WorkStateFilter

    def list(self, request, *args, **kwargs):
        # Apply filtering
        queryset = self.filter_queryset(self.get_queryset())

        # Call the parent class's list method to get the default response
        response_data = super().list(request, *args, **kwargs).data
        marche = self.request.query_params.get('marche', None)

        qs = queryset.values('date__month', 'date__year').distinct().annotate(
            month_year=Concat(
                Cast('date__month', output_field=CharField()),
                Value('-'),
                Cast('date__year', output_field=CharField()),
                output_field=CharField()
            ),
            count=Count('id'), amount=Sum('qte_cumule')).order_by('date__year', 'date__month').values('month_year',
                                                                                                      'amount')
        sum = DQE.objects.filter(Q(marche=marche)).aggregate(
            models.Sum('quantite'))["quantite__sum"]

        if (response_data):
            return Response({"x": qs.values_list('month_year', flat=True), "y1": qs.values_list('amount', flat=True),
                             "y2": [sum] * len(qs)}, status=status.HTTP_200_OK)
        else:
            return Response({'message': "La rechercher n'a pas pu aboutir à un resultat"},
                            status=status.HTTP_404_NOT_FOUND)


class GetDQEStateView(generics.ListAPIView):
    # permission_classes = [permissions.IsAuthenticated,ViewDQEPermission]
    queryset = DQE.objects.all()
    serializer_class = DQESerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = DQEFilter

    def list(self, request, *args, **kwargs):
        # Apply filtering
        queryset = self.filter_queryset(self.get_queryset())

        # Call the parent class's list method to get the default response
        response_data = super().list(request, *args, **kwargs).data
        X = []
        Y1 = []
        Y2 = []
        for q in queryset:
            try:
                attachement = Attachements.objects.filter(dqe=q).latest('date')
                X.append(attachement.dqe.code_tache)
                Y1.append(attachement.qte_cumule)
                Y2.append(attachement.dqe.quantite)
            except Attachements.DoesNotExist:
                pass

        if (response_data):
            return Response({"x": X, "y1": Y1, "y2": Y2}, status=status.HTTP_200_OK)
        else:
            return Response({'message': "La rechercher n'a pas pu aboutir à un resultat"},
                            status=status.HTTP_404_NOT_FOUND)



class DelEnc(generics.DestroyAPIView):
    # permission_classes = [IsAuthenticated]
    queryset = Encaissement.objects.all()
    serializer_class = EncaissementSerializer

    def delete(self, request, *args, **kwargs):
        pks = self.request.data.get('id', [])
        print(pks)
        if pks:
            for pk in pks:
                try:
                    Encaissement.objects.get(id=pk).delete()
                except Exception as e:
                    continue
            
        return Response('Enaissement Annulé', status=status.HTTP_200_OK)


class DeletedEncaissement(generics.ListAPIView):
    queryset = Encaissement.objects.all()
    serializer_class = EncaissementSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = EncaissementFilter


class Etat_Creances(generics.ListAPIView):
    queryset = Marche.objects.all()
    serializer_class = ECSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ECFilter


class GetRemb(generics.ListAPIView):
    queryset = Remboursement.objects.all()
    serializer_class = RemboursementSerializer


class GetMarcheAvenent(generics.ListAPIView):
    queryset = MarcheAvenant.objects.all()
    serializer_class = MarcheAvenantSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = MarcheAvenantFilter


class AjoutAvenantMarcheApiView(generics.CreateAPIView):
    # permission_classes = [IsAuthenticated, AddMarchePermission]

    queryset = MarcheAvenant.objects.all()
    serializer_class = MarcheAvenantSerializer

    def create(self, request, *args, **kwargs):

        serializer = self.get_serializer(data=request.data)
        revisable = False
        try:
            revisable = serializer.initial_data['revisable']
            print(revisable)
        except Exception as e:
            revisable = False
        print(serializer.initial_data)
        try:
            MarcheAvenant(num_avenant=serializer.initial_data['num_avenant'], id=serializer.initial_data['id'],
                          code_site=serializer.initial_data['code_site'], nt=serializer.initial_data['nt'],
                          libelle=serializer.initial_data['libelle'], ods_depart=serializer.initial_data['ods_depart'],

                          delai_paiement_f=serializer.initial_data['delai_paiement_f'],
                          rabais=serializer.initial_data['rabais'] or 0, tva=serializer.initial_data['tva'] or 0,
                          rg=serializer.initial_data['rg'],
                          date_signature=serializer.initial_data['date_signature']).save(
                force_insert=True)

            m = Marche.objects.get(nt=serializer.initial_data['nt'], code_site=serializer.initial_data['code_site'])
            m.num_avenant = serializer.initial_data['num_avenant']
            m.libelle = serializer.initial_data['libelle']
            m.ods_depart = serializer.initial_data['ods_depart']
            m.delai_paiement_f = serializer.initial_data['delai_paiement_f']
            m.rabais = serializer.initial_data['rabais'] or 0
            m.tva = serializer.initial_data['tva'] or 0
            m.rg = serializer.initial_data['rg'] or 0
            m.date_signature = serializer.initial_data['date_signature']
            m.save(force_update=True)

            return Response('Marché ajouté', status=status.HTTP_200_OK)

        except IntegrityError as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)


class GetDQEAvenent(generics.ListAPIView):
    queryset = DQEAvenant.objects.all()
    serializer_class = DQEAvenantSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = DQEAvenantFilter

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        mt = 0
        response_data = super().list(request, *args, **kwargs).data
        for q in queryset:
            mt = mt + q.prix_q
        return Response({'dqe': response_data,
                         'extra': {
                             'mt': mt,

                         }}, status=status.HTTP_200_OK)


class AjoutDQEAvenantApiView(generics.CreateAPIView):
    # permission_classes = [IsAuthenticated, AddDQEPermission]
    queryset = DQEAvenant.objects.all()
    serializer_class = DQEAvenantSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        print(serializer.initial_data)
        try:
            MarcheAvenant.objects.filter(code_site=serializer.initial_data['pole'], nt=serializer.initial_data['nt'],
                                         num_avenant=serializer.initial_data['num_avenant'])
        except MarcheAvenant.DoesNotExist:
            return Response('Impossible d\' ajouter un avenant', status=status.HTTP_200_OK)

        try:
            try:
                dqe = DQE.objects.get(nt=serializer.initial_data['nt'], code_site=serializer.initial_data['pole'],
                                      code_tache=serializer.initial_data['code_tache'])
                DQEAvenant(code_site=serializer.initial_data['pole'],
                           num_avenant=serializer.initial_data['num_avenant'],
                           nt=serializer.initial_data['nt'],
                           code_tache=serializer.initial_data['code_tache'],
                           prix_u=serializer.initial_data['prix_u'],
                           est_tache_composite=serializer.initial_data['est_tache_composite'],
                           est_tache_complementaire=False, quantite=serializer.initial_data['quantite'],
                           unite=TabUniteDeMesure.objects.get(id=serializer.initial_data['unite']), libelle=
                           serializer.initial_data['libelle']).save(force_insert=True)

                qte = float(dqe.quantite) + float(serializer.initial_data['quantite'])
                if (qte < 0):
                    qte = 0
                dqe.quantite = qte
                dqe.prix_u = float(serializer.initial_data['prix_u'])
                dqe.save(force_update=True)
                return (Response('Tache mise à jour', status=status.HTTP_200_OK))

            except DQE.DoesNotExist:
                DQEAvenant(code_site=serializer.initial_data['pole'],
                           num_avenant=serializer.initial_data['num_avenant'],
                           nt=serializer.initial_data['nt'],
                           code_tache=serializer.initial_data['code_tache'], prix_u=serializer.initial_data['prix_u'],
                           unite=TabUniteDeMesure.objects.get(id=serializer.initial_data['unite']), libelle=
                           serializer.initial_data['libelle']).save(force_insert=True)
                DQE(code_site=serializer.initial_data['pole'], nt=serializer.initial_data['nt'],
                    code_tache=serializer.initial_data['code_tache'], prix_u=serializer.initial_data['prix_u'],
                    quantite=serializer.initial_data['quantite'],
                    unite=TabUniteDeMesure.objects.get(id=serializer.initial_data['unite']),
                    libelle=serializer.initial_data['libelle']).save(force_insert=True)
                return Response('Tache complémentaire ajouté', status=status.HTTP_200_OK)
        except IntegrityError as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)


class ImportDQEAvenantAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        dqe_file = request.FILES['file']
        nt = request.data.get('nt')
        cs = request.data.get('cs')
        num_av = request.data.get('num_av')
        try:
            MarcheAvenant.objects.filter(code_site=cs, nt=nt, num_avenant=num_av)
        except MarcheAvenant.DoesNotExist:
            return Response('Impossible d\' ajouter un avenant', status=status.HTTP_200_OK)

        try:

            df=pandas.read_excel(dqe_file, engine='openpyxl')
           
            for index, row in df.iterrows():
                try:
                    dqe = DQE.objects.get(nt=nt, code_site=cs,
                                          code_tache=row['code_tache'])
                    DQEAvenant(
                        code_site=cs, nt=nt,
                        code_tache=row['code_tache'], prix_u=row['prix_u'],
                        num_avenant=num_av,
                        unite=TabUniteDeMesure.objects.get(libelle=row['unite']),
                        libelle=row['libelle'], quantite=row['quantite'], user_id=request.user.username).save(force_insert=True)

                    qte = float(dqe.quantite) + float(row['quantite'])
                    if (qte < 0):
                        qte = 0
                    dqe.quantite = qte
                    dqe.prix_u = float(row['prix_u'])
                    dqe.save(force_update=True)

                except DQE.DoesNotExist:
                    DQEAvenant(
                        code_site=cs, nt=nt,
                        code_tache=row['code_tache'], prix_u=row['prix_u'],
                        num_avenant=num_av,
                        unite=TabUniteDeMesure.objects.get(libelle=row['unite']),
                        libelle=row['libelle'], quantite=row['quantite'], user_id=request.user.username).save(force_insert=True)

                    DQE(
                        code_site=cs, nt=nt,
                        code_tache=row['code_tache'], prix_u=row['prix_u'],
                        unite=TabUniteDeMesure.objects.get(libelle=row['unite']),
                        libelle=row['libelle'], quantite=row['quantite'], user_id=request.user.username
                    ).save(force_insert=True)

            return Response(f'Creation des Taches de l\'avenant  n° {num_av}',
                                status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)




class UpdateAttachementApiVew(generics.UpdateAPIView):
    queryset = Attachements.objects.all()
    serializer_class = AttachementsSerializer

    def get_object(self):
        id = self.request.data.get('id')

        try:
            obj = Attachements.objects.get(id=id)
        except Attachements.DoesNotExist:
            raise NotFound("Object n'éxiste pas")
        self.check_object_permissions(self.request, obj)

        return obj

    def update(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            instance.montant=request.data['montant']
            instance.qte=request.data['qte']
            instance.save(force_update=True)
            return Response('Attachement mis à jour', status=status.HTTP_200_OK)
        except IntegrityError as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)



class GetPSView(generics.ListAPIView):
    queryset = ProductionStockee.objects.all()
    serializer_class = PSSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = PSFilter

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        mt = 0
        response_data = super().list(request, *args, **kwargs).data
        x=[]
        y1=[]
        y2=[]
        for q in queryset:
            x.append(q.code_tache)
            y1.append(q.qte_prod)
            y2.append(q.qte_att)

        return Response({'prod': response_data,
                         'extra': {
                             'x': x,
                             'y1':y1,
                             'y2':y2,
                         }}, status=status.HTTP_200_OK)








class UserProfile(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        uid=request.user.id
        try:
            user=User.objects.get(id=uid)

            return Response({
                "full_name":user.get_full_name(),
                "username":user.username,
                "email":user.email,
                "joined":user.date_joined.strftime("Le %Y-%m-%d à %H:%M:%S"),
                "login":Token.objects.get(user=user).created.strftime("Le %Y-%m-%d à %H:%M:%S"),
                "current_password":'',
                "new_password": '',
                "confirm_new_password": '',

            }, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({"message":"Erreur ... !"}, status=status.HTTP_400_BAD_REQUEST)

class EditUserProfile(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        username = request.data.get('username')
        email = request.data.get('email')
        current_password = request.data.get('current_password')
        new_password=request.data.get('new_password')
        confirm_new_password=request.data.get('confirm_new_password')

        uid = request.user.id
        user = User.objects.get(id=uid)
        try:
            if(username):
                user.username=username

            if (email):
                user.email = email

            if(current_password and new_password and confirm_new_password):
                if(check_password(current_password,user.password)):
                    if(new_password!=confirm_new_password):
                        return Response({"message": "Vous n'avez pas confirmé votre mot de passe"}, status=status.HTTP_400_BAD_REQUEST)
                    else:

                        user.set_password(new_password)
                else:
                    return Response({"message": "Mot de pass incorrect"}, status=status.HTTP_400_BAD_REQUEST)


            user.save()
            return Response({"message": "Votre profile est mis à jour"}, status=status.HTTP_200_OK)

        except User.DoesNotExist:
            return Response({"message": "Erreur ... !"}, status=status.HTTP_400_BAD_REQUEST)



