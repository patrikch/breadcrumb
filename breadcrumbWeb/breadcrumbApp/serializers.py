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
            'waves': reverse('wave-list',request=request) +
            '?project={}'.format(obj.pk),
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
            'shops': reverse('shop-list',request=request) +
            '?wave={}'.format(obj.pk),
        }

class ShopSerializer(serializers.ModelSerializer):
    
    links = serializers.SerializerMethodField()

    class Meta:
        model = Shop
        fields = ("id","name","district","links",)

    def get_links(self,obj):
        request = self.context["request"]
        return {
            "self":reverse("shop-detail",kwargs={"pk":obj.pk},
                           request=request),            
        }
