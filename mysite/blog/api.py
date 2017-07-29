from tastypie.resources import ModelResource
from tastypie.constants import ALL
from blog.models import Post

class PostResource(ModelResource):
    class Meta:
        queryset = Post.objects.all()
        resource_name = "post"
        filtering = {'id':["exact"]}