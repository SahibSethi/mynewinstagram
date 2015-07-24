from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mynewinstagram.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^account/hello/$', 'account.views.hello', name='hello'),
    url(r'^account/users/$', 'account.views.getallusers', name='getallusers'),
    url(r'^admin/', include(admin.site.urls)),
)
