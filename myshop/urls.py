"""myshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import patterns,include,url
from django.contrib import admin
from news import urls as news_urls, views as newsView
from items import urls as item_urls, views as itemView

urlpatterns = [
    #url(r'^$', 'news.views.home', name="home"), we can also use this function instead of below one
    url(r'^$', newsView.home, name="home"),
    url(r'^admin/', admin.site.urls),
    url(r'^news/', include(news_urls)),
    url(r'^items/', include(item_urls)),
]

#old way to add urls in the url config, depricated in 1.9 and will be removed in 1.10
# urlpatterns += patterns('',
   
# )



