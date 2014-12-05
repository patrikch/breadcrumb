from rest_framework import authentication, permissions, viewsets

from .models import Project
from .serializers import ProjectSerializer

class DefaultMixin(object):

    authentication_classes = (
        authentication.BasicAuthentication,
        authentication.TokenAuthentication,        
    )

    permission_classes = (
        permissions.IsAuthenticated,
    )
    paginate_by = 25
    paginate_by_param = "page_size"
    max_paginate_by = 100

class ProjectViewSet(DefaultMixin,viewsets.ModelViewSet):

    queryset = Project.objects.order_by("name")
    serializer_class = ProjectSerializer


    
