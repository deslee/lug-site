from django.conf.urls import patterns, url

from django.views.generic import TemplateView

from basiccms import views
urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<slug>\w+)/$', views.page, name='page'),
)
