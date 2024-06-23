from django.urls import path
from .views import *

urlpatterns = [

    path('imglogin/', ImgLogin.as_view()),


]