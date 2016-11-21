from django.conf.urls import patterns, url

from django.contrib import admin
from django.contrib.auth import views

from qa.forms import LoginForm

admin.autodiscover()

urlpatterns = patterns('qa.views',
                       # Examples:
                       # url(r'^$', 'ask.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),

                       url(r'^$', 'home', name='home'),
                       # url(r'^login/', 'user_login', name='login'),
                       url(r'^login/$', views.login, {'template_name': 'login.html', 'authentication_form': LoginForm}),
                       url(r'^signup/$', 'user_signup', name='user_signup'),
                       # url(r'^logout/', 'user_logout', name='user_logout'),
                       url(r'^logout/$', views.logout, {'next_page': '/login'}),
                       url(r'^question/(?P<id>[0-9]+)/$', 'question_detail', name='question_detail'),
                       url(r'^ask/.*$', 'ask', name='ask'),
                       url(r'^answer/.*$', 'answer', name='answer'),
                       url(r'^popular/$', 'popular', name='popular'),
                       url(r'^new/$', 'home', name='home'),

                       )
