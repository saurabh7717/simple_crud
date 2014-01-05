from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'caterer.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^caterer/',include('cmanagement.urls',namespace="cmanagement")),
    url(r'^admin/', include(admin.site.urls)),
)
