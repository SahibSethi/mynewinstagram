from django.conf.urls import patterns, include, url
urlpatterns = patterns('',
    url(r'^hello/$', 'account.views.hello', name='hello'),
    url(r'^users/$', 'account.views.getallusers', name='getallusers'),
    url(r'^users/(?P<id>\d+)/$','account.views.newhome', name='home'),
)

