from django.conf.urls import patterns, url, include

from django.contrib import admin
admin.autodiscover()
#just test
urlpatterns = patterns('',
     url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
     url(r'^admin/', include(admin.site.urls)),
     url(r'^accounts/', include('registration.backends.default.urls')),
     url(r'^$', include('b2b.urls')),
)
