from rest_framework import serializers
from .models import *
class ImageLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageLogin
        fields = '__all__'
