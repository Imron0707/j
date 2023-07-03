from django.views.generic import ListView
from .models import Post


class postList(ListView):
    model = Post
    template_name = 'default.html'
    context_object_name = 'news_post'
    news_post = Post.objects.all()
