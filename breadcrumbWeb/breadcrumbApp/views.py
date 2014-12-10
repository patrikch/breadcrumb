from rest_framework import authentication, permissions, viewsets, filters

from .models import Project, Wave, Shop
from .serializers import ProjectSerializer, WaveSerializer, ShopSerializer
from .forms import WaveFilter, ShopFilter

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
    filter_backends = (
        filters.DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    )

class ProjectViewSet(DefaultMixin,viewsets.ModelViewSet):

    queryset = Project.objects.order_by("name")
    serializer_class = ProjectSerializer
    search_fields = ('id', )
    ordering_fields = ('name', )

class WaveViewSet(DefaultMixin,viewsets.ModelViewSet):

    queryset = Wave.objects.order_by("name")
    serializer_class = WaveSerializer
    search_fields = ('id', )
    ordering_fields = ('name', )
    filter_class = WaveFilter

class ShopViewSet(DefaultMixin,viewsets.ModelViewSet):

    queryset = Shop.objects.order_by("name")
    serializer_class = ShopSerializer
    search_fields = ('id', )
    ordering_fields = ('name',"district", )
    filter_class = ShopFilter



    


    
