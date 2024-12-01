from rest_framework import generics
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from .serializers import *


class SupplierListView(generics.ListAPIView):
    queryset = SupplierProfile.objects.all()
    serializer_class = SupplierSerializer


class SupplierCreateView(generics.CreateAPIView):
    queryset = SupplierProfile.objects.all()
    serializer_class = SupplierSerializer


class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductCreateView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer



# class GymApiView(generics.ListAPIView):
#     queryset = Gym.objects.all()
#     serializer_class = GymSerializer