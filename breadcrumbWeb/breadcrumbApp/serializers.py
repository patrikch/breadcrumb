from rest_framework import serializers
from .models import Project,Wave

class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = ("id","name",)

class WaveSerializer(serializers.ModelSerializer):

    class Meta:
        model = Wave
        fields = ("id","name",)

class ShopSerializer(serializers.ModelSerializer):

    class Meta:
        model = Shop
        fields = ("id","shopName","district",)
