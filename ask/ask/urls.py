from django.conf.urls import patterns, url

from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('qa.views',
                       # Examples:
                       # url(r'^$', 'ask.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),

                       url(r'^$', 'home', name='home'),
                       url(r'^login/$', 'test', name='login'),
                       url(r'^signup/$', 'test', name='signup'),
                       url(r'^question/(?P<id>[0-9]+)/$', 'question_detail', name='question_detail'),
                       url(r'^ask/.*$', 'test', name='ask'),
                       url(r'^popular/$', 'popular', name='popular'),
                       url(r'^new/$', 'test', name='new'),

                       )
