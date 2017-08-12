from django.conf.urls import url
from . import views
from django.contrib.auth.views import *
from study import settings
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [

    url(r'^$', views.firstpage, name='first_page'),
    url(r'^login/$', views.login, name='login'),
    url(r'^register/$', views.register, name='register'),
    url(r'^list/(?P<id>[0-9]+)/$', views.article_list, name='article_list'),
    url(r'^article/(?P<id>[0-9]+)/detail/$',views.article_detail, name='article_detail'),
    url(r'^(?P<id>[0-9]+)article/add/$', views.article_add, name= 'article_add'),
    url(r'^article/(?P<id>[0-9]+)/update/$', views.article_update, name='article_update'),
    url(r'^author/(?P<id>[0-9]+)/update/$', views.author_update, name='author_update'),
    url(r'^author/(?P<id>\d+)/detail/$', views.author_detail, name='author_detail'),
    url(r'^(?P<id>[0-9]+)/mypage/$',views.mypage,name='mypage'),
]