from django.conf.urls import url

from . import views
urlpatterns = [
    url(r'^article-list/$', views.article_list,name='article_list'),
    url(r'^article-detail/(?P<id>\d+)/$', views.article_detail,name='article_detail'),
]