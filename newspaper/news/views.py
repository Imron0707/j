from django.views.generic import ListView
from django.views.generic import DetailView
from .models import Post

class postList(ListView):
    model = Post
    template_name = 'default.html'
    context_object_name = 'news_post'
    news_post = Post.objects.all()


class detailpostlist(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'
