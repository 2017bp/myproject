from django.conf.urls import url
from django.contrib.auth.views import login, logout
from . import views
from django.contrib.auth import views as auth_views

app_name = 'BP'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^submit/$', views.submit, name='submit'),
    url(r'^about/$', views.AboutView, name='about'),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/BP/login'}, name='logout'),

    # url(r'^login/$', auth_views.login, {'template_name': 'BP/login.html'}),
    # (r'^logout/$',auth_views.logout, {'next_page': 'login/'}),
]