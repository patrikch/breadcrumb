from django.conf.urls import patterns, include, url
from rest_framework.authtoken.views import obtain_auth_token
#from django.contrib import admin

urlpatterns = [    
    url(r'^api/token/', obtain_auth_token,name="api-token"),
]
