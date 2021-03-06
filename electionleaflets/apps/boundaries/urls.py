from django.conf.urls import *

from boundaries import views

################################################################################
urlpatterns = patterns('casestudies',
    # url(r'^boundry_json/$', views.boundry_json, name='boundry_json'),
    url(r'^tile/([^/]+)/$', views.tile, name="tile"),#This is just used for the reverse lookup of base name for tile urls
    url(r'^tile/([^/]+)/(\d+)/(\d+)/(\d+).png$', views.tile, name="tile"),
    url(r'^popup/([^/]+)$', views.popup, name="popup"),#This is just used for the reverse lookup of base name for popup urls
    url(r'^popup/([^/]+)/([-+]?[0-9]*\.?[0-9]+)/([-+]?[0-9]*\.?[0-9]+)/(\d+)$', views.popup, name="popup"),
    url(r'^key_image/([^/]+)/([0-9]*)/([0-9]*)/([0-9]*)', views.view_key),
    url(r'^([^/]+)/$', views.view_map, name='view_map'),
)
