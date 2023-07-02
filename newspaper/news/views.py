from django.views.generic import ListView
from .models import Post


class postList(ListView):
    model = Post
    queryset = Post.objects.order_by('-createPost')


