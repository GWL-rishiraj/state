from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'yogesh_blog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^myadmin/', include(admin.site.urls)),
    url(r'^', include('blogango.urls')),
    
)
