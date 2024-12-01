from rest_framework import serializers
from .models import *


class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = SupplierProfile
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"