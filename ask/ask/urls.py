from django.conf.urls import patterns, url

from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('qa.views',
                       # Examples:
                       # url(r'^$', 'ask.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),

                       url(r'^$', 'index', name='index'),
                       url(r'^page(?P<num>[0-9]+)/$', 'index', name='index'),
                       url(r'^login/$', 'test', name='login'),
                       url(r'^signup/$', 'test', name='signup'),
                       url(r'^question/(?P<id>[0-9]+)/$', 'question', name='question'),
                       url(r'^ask/.*$', 'test', name='ask'),
                       url(r'^popular/$', 'popular_page', name='popular_page'),
                       url(r'^new/$', 'test', name='new'),

                       )
