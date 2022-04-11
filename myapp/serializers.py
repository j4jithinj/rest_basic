from re import I
from rest_framework import serializers 
from . import models

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Product
        fields = '__all__'

class GetProductByIdSerializer(serializers.Serializer):
    id = serializers.CharField()

class PoemSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Poem
        fields = ('title','stanzas')