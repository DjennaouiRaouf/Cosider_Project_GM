from django.shortcuts import render

# Create your views here.
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from .models import *
from .Serializers import *
class ImgLogin(generics.ListAPIView):
    queryset = ImageLogin.objects.all()
    serializer_class = ImageLoginSerializer

