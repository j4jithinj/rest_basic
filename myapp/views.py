from re import M
from django.shortcuts import render
from rest_framework import generics
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from . import serializers
from . import models
from rest_framework import status
from drf_multiple_model.views import ObjectMultipleModelAPIView, FlatMultipleModelAPIView
from generics import permissions

class ProductView1(generics.ListCreateAPIView):
    # http_method_names = ['post']
    serializer_class = serializers.ProductSerializer
    queryset = models.Product.objects.all()
    permission_classes = [permissions.SamplePermissionUser]

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = serializers.ProductSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class ProductView2(generics.CreateAPIView):
    serializer_class = serializers.ProductSerializer
    queryset = models.Product.objects.all()
    # permission_classes = [IsAdminUser]

class CreateAPIView(generics.CreateAPIView):
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

class GenericView(generics.GenericAPIView):
    def get(self, request, *args, **kwargs):
        return Response(data={'details':'Get method called'}, status=status.HTTP_200_OK)
    def post(self, request, *args, **kwargs):
        return Response(data={'details':'POST method called'}, status=status.HTTP_201_CREATED)

class TextAPIView(ObjectMultipleModelAPIView):
    querylist = [
        {'queryset': models.Product.objects.all(), 'serializer_class': serializers.ProductSerializer},
        {'queryset': models.Poem.objects.filter(), 'serializer_class': serializers.PoemSerializer},
    ]

class TextAPIFlatView(FlatMultipleModelAPIView):
    querylist = [
        {'queryset': models.Product.objects.all(), 'serializer_class': serializers.ProductSerializer},
        {'queryset': models.Poem.objects.filter(), 'serializer_class': serializers.PoemSerializer},
    ]