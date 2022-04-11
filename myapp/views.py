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
    serializer_class = serializers.ProductSerializer
    queryset = models.Product.objects.all()
    # permission_classes = [IsAdminUser]

class ProductView3(generics.ListAPIView):
    serializer_class = serializers.ProductSerializer
    queryset = models.Product.objects.all()
    # permission_classes = [IsAdminUser]

class ProductView4(generics.RetrieveAPIView):
    serializer_class = serializers.ProductSerializer
    queryset = models.Product.objects.all()
    # lookup_field = 'pk'

class ProductView5(generics.DestroyAPIView):
    serializer_class = serializers.ProductSerializer
    queryset = models.Product.objects.all()
    # lookup_field = 'pk'

class ProductView6(generics.UpdateAPIView):
    # http_method_names = ['post']
    serializer_class = serializers.ProductSerializer
    queryset = models.Product.objects.all()
    # lookup_field = 'pk'

class RetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    # http_method_names = ['post']
    serializer_class = serializers.ProductSerializer
    queryset = models.Product.objects.all()
    # lookup_field = 'pk'

class RetrieveDestroyAPIView(generics.RetrieveDestroyAPIView):
    # http_method_names = ['post']
    serializer_class = serializers.ProductSerializer
    queryset = models.Product.objects.all()
    # lookup_field = 'pk'

class RetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    # http_method_names = ['post']
    serializer_class = serializers.ProductSerializer
    queryset = models.Product.objects.all()
    # lookup_field = 'pk'