from django.conf.urls import patterns, include, url
from django.contrib import admin
import account
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mynewinstagram.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^account/', include('account.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
