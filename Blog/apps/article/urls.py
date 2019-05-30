from django.conf.urls import url

from . import views
urlpatterns = [
    # url(r'^$', views.article_list,name='article_list'),
    url(r'^article-list/$', views.ArticleListView.as_view(),name='article_list'),
    url(r'^article-detail/(?P<id>\d+)/$', views.ArticleDetailView.as_view(),name='article_detail'),
    url(r'^article-create/$', views.article_create,name='article_create'),
    url(r'^article-delete/(?P<id>\d+)/$', views.article_delete,name='article_delete'),
    url(r'^article-update/(?P<id>\d+)/$', views.article_update,name='article_update'),
]