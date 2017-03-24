from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<posting_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^submit/$', views.submit, name='submit'),
]