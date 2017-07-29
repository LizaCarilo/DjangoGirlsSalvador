from django.conf.urls import include, url
from.import views
from blog.api import PostResource
from tastypie.api import Api

v1_api = Api(api_name='v1')
v1_api.register(PostResource())

urlpatterns = [
    url(r'^$', views.post_list),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^post/(?P<pk>[0-9]+)/delete/$', views.post_delete, name='post_delete'),
    url(r'^api/', include(v1_api.urls))
]