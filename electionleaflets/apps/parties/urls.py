from django.conf.urls import patterns, include, handler500, url
from django.conf import settings

from parties.views import view_party, view_attacking_party, view_parties

urlpatterns = patterns(
    '',
    url(r'^/$',      view_parties, name='parties'),
    url(r'^/(?P<slug>[\w_\-\.]+)/$',  view_party,name='party'),
    url(r'^/(?P<slug>[\w_\-\.]+)/attacking/$',  view_attacking_party,name='attacking_party'),
)

