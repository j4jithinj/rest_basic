from django.shortcuts import render
from rest_framework import generics
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from . import serializers
from . import models

class ProductView1(generics.ListCreateAPIView):
    # http_method_names = ['post']
    serializer_class = serializers.ProductSerializer
    queryset = models.Product.objects.all()
    # permission_classes = [IsAdminUser]

    def list(self, request):
        queryset = self.get_queryset()
        serializer = serializers.ProductSerializer(queryset, many=True)
        return Response(serializer.data)

class ProductView2(generics.CreateAPIView):
    # http_method_names = ['post']
    serializer_class = serializers.ProductSerializer
    queryset = models.Product.objects.all()
    # permission_classes = [IsAdminUser]

class ProductView3(generics.ListAPIView):
    # http_method_names = ['post']
    serializer_class = serializers.ProductSerializer
    queryset = models.Product.objects.all()
    # permission_classes = [IsAdminUser]

class ProductView4(generics.RetrieveAPIView):
    # http_method_names = ['post']
    serializer_class = serializers.ProductSerializer
    queryset = models.Product.objects.all()
    # lookup_field = 'pk'
    # permission_classes = [IsAdminUser]

class ProductView5(generics.DestroyAPIView):
    # http_method_names = ['post']
    serializer_class = serializers.ProductSerializer
    queryset = models.Product.objects.all()
    # lookup_field = 'pk'
    # permission_classes = [IsAdminUser]

class ProductView6(generics.UpdateAPIView):
    # http_method_names = ['post']
    serializer_class = serializers.ProductSerializer
    queryset = models.Product.objects.all()
    # lookup_field = 'pk'
    # permission_classes = [IsAdminUser]
