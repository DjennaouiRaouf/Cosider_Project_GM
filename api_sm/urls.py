from django.urls import path
from .views import *

urlpatterns = [

    path('adduser/',CreateUserView.as_view()),
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('whoami/', WhoamiView.as_view()),
    path('adddqe/',AjoutDQEApiView.as_view()),
    path('addclient/',AjoutClientApiView.as_view()),
    path('addmarche/', AjoutMarcheApiView.as_view()),
    path('addsite/',AjoutSiteApiView.as_view()),
    path('addnt/',AjoutNTApiView.as_view()),

    path('getatt/',GetAttachements.as_view()),
    path('workstate/', WorkState.as_view()),
    path('dqestate/',GetDQEStateView.as_view()),
    path('importdqe/',ImportDQEAPIView.as_view()),

    path('getclients/', GetClientsView.as_view()),

    path('getsites/', GetSitesView.as_view()),

    path('getmarche/',GetMarcheView.as_view()),
    path('updatemarche/',UpdateMarcheView.as_view()),

    path('addatt/', AddAttachementApiView.as_view()),

    path('recupcaution/',UpdateCautionApiView.as_view()),

    path('updatent/',UpdateNTApiVew.as_view()),
    path('userprofile/',UserProfile.as_view()),
    path('editusr/',EditUserProfile.as_view()),

    path('importdqeav/',ImportDQEAvenantAPIView.as_view()),

    path('etatcreance/',Etat_Creances.as_view()),

    path('getdqe/', GetDQEView.as_view()),
    path('deldqe/',DelDQEByID.as_view()),

    path('updatedqe/',UpdateDQEApiVew.as_view()),

    path('getnt/',GetNTView.as_view()),
    path('getmdqe/<str:marche>/',GetDQEbyId.as_view()),

    path('delenc/',DelEnc.as_view()),

    path('addfacture/',AddFactureApiView.as_view()),
    path('getfacture/',GetFacture.as_view()),
    path('getfacturerg/',GetFactureRG.as_view()),
    path('ecf/',GetECF.as_view()),

    path('encaisser/',AddEncaissement.as_view()),
    path('encaissements/',GetEncaissement.as_view()),
    path('cinvoice/',CInvoice.as_view()),

    path('getlibmp/',LibMP.as_view()),



    path('delfacture/',DeletedFacture.as_view()),
    path('flashm/',FlashMonths.as_view()),
    path('attm/',AttMonths.as_view()),
    path('detail/',getDetailFacture.as_view()),
    path('det/',getDetFacture.as_view()),
    path('mav/',GetMarcheAvenent.as_view()),

    path('addmav/',AjoutAvenantMarcheApiView.as_view()),
    path('adddqeav/',AjoutDQEAvenantApiView.as_view()),

    path('dqeav/',GetDQEAvenent.as_view()),
    path("getlibav/",LibAV.as_view()),

    path("getlibcaut/", LibCaut.as_view()),

    path('getavance/',GetAvance.as_view()),
    path('addavance/',AddAvanceApiView.as_view()),

    path('contractkeys/', contratKeys.as_view()),


    path('prodparams/',GetProdParams.as_view()),

    path('getcautions/',GetCautions.as_view()),
    path('addcautions/',AddCautions.as_view()),

    path('annulefacture/',DeleteInvoiceApiView.as_view()),
    path('delencaissements/',DeletedEncaissement.as_view()),


    path('delatt/',DelATT.as_view()),

    path('remb/',GetRemb.as_view()),




]