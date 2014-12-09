from rest_framework import authentication, permissions, viewsets

from .models import Project, Wave, Shop
from .serializers import ProjectSerializer, WaveSerializer, ShopSerializer

class DefaultMixin(object):

    authentication_classes = (
        authentication.BasicAuthentication,
        authentication.TokenAuthentication,        
    )

    permission_classes = (
        #permissions.IsAuthenticated,
        permissions.AllowAny,
    )
    paginate_by = 25
    paginate_by_param = "page_size"
    max_paginate_by = 100

class ProjectViewSet(DefaultMixin,viewsets.ModelViewSet):

    queryset = Project.objects.order_by("name")
    serializer_class = ProjectSerializer

class WaveViewSet(DefaultMixin,viewsets.ModelViewSet):

    queryset = Wave.objects.order_by("name")
    serializer_class = WaveSerializer

class ShopViewSet(DefaultMixin,viewsets.ModelViewSet):

    queryset = Shop.objects.order_by("shopName")
    serializer_class = ShopSerializer



    


    
