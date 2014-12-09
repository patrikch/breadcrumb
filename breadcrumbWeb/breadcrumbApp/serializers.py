from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import Project,Wave,Shop

class ProjectSerializer(serializers.ModelSerializer):

    links = serializers.SerializerMethodField()
 
    class Meta:
        model = Project
        fields = ("id","name","links",)
        
    def get_links(self,obj):
        request = self.context["request"]
        return {
            "self":reverse("project-detail",kwargs={"pk":obj.pk},
                           request=request),            
        }

class WaveSerializer(serializers.ModelSerializer):

    links = serializers.SerializerMethodField()

    class Meta:
        model = Wave
        fields = ("id","name","links",)

    def get_links(self,obj):
        request = self.context["request"]
        return {
            "self":reverse("wave-detail",kwargs={"pk":obj.pk},
                           request=request),            
        }

class ShopSerializer(serializers.ModelSerializer):
    
    links = serializers.SerializerMethodField()

    class Meta:
        model = Shop
        fields = ("id","shopName","district","links",)

    def get_links(self,obj):
        request = self.context["request"]
        return {
            "self":reverse("shop-detail",kwargs={"pk":obj.pk},
                           request=request),            
        }
