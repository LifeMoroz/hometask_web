from django.conf.urls import url

from hometask_web import views

urlpatterns = [
    url(r'^$', views.PCView.as_view(), name='pc-list'),
    url(r'^adapters/$', views.adapters, name='adapter-list'),
    # url(r'^connections', views.index, 'adapter-list'),
    # url(r'^configurations', views.index, 'adapter-list'),
]
