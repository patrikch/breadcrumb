import django_filters

from .models import Wave, Shop

class WaveFilter(django_filters.FilterSet):

    class Meta:
        model = Wave
        fields = ("id","name","project",)

class ShopFilter(django_filters.FilterSet):

    class Meta:
        model = Shop
        fields = ("id","shopName","wave",)
