from rest_framework import serializers
from . import models

class SuperUserSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        user = models.CustomUser.objects.create_superuser(email=validated_data['email'], password=validated_data['password'])
        user.name = validated_data['name']
        user.save()
        return user 

    class Meta:
        model = models.CustomUser
        fields = ['email', 'name', 'password']