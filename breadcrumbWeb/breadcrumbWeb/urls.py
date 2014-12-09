from django.conf.urls import include, url
from rest_framework.authtoken.views import obtain_auth_token
from breadcrumbApp.urls import router
import os

site_media = os.path.join(os.path.dirname(__file__),
    "site_media")


urlpatterns = [    
    #url(r'^api/token/', obtain_auth_token,name="api-token"),
    url(r"^api/",include(router.urls)),
    url(r"^site_media/(?P<path>.*)$","django.views.static.serve",
         {"document_root":site_media}),
]
