from django.conf.urls import patterns, include, url
urlpatterns = patterns('',

    url(r'^hello/$', 'account.views.hello', name='hello'),
    url(r'^sendmessage/$', 'account.views.sendmessage', name='sendmessage'),
    url(r'^country/$', 'account.views.create_update_country', name='country-create'),
    url(r'^country/(?P<id>\d+)/$', 'account.views.create_update_country', name='country-edit'),
    url(r'^users/$', 'account.views.getallusers', name='getallusers'),
    url(r'^users/(?P<id>\d+)/$','account.views.newhome', name='home'),
)

