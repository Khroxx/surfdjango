from rest_framework import serializers
from .models import Corporation

class CorporationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Corporation
        fields = ['id', 'name', 'address', 'url', 'user']