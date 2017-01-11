from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.all_items,name='all items'),
    url(r'^([0-9]{10})/$', views.item)
]