from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.AnnouncementListView.as_view(), name='index'),
    url(r'^(?P<slug>[-\w]+)/$', views.PostListView.as_view(), name='posts_in_category'),
    url(r'^([-\w]+)/(?P<slug>[-\w]+)/$', views.PostDetailView.as_view(), name='post'),
]
