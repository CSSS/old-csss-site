from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.CategoryView.as_view(), name='index'),
    url(r'^(?P<name>\w+)/$', views.PostListView.as_view(), name='posts_in_category'),
    url(r'^(?P<name>\w+)/(?P<pk>[0-9]+)/$', views.PostDetailView.as_view(), name='post'),
]
