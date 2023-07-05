from django.views.generic import ListView
from django.views.generic import DetailView
from datetime import datetime
from .models import Post

class postList(ListView):
    model = Post
    template_name = 'news.html'
    context_object_name = 'posts'
    ordering = '-createPost'  # Указываем поле для упорядочивания объектов

    def get_queryset(self):
        queryset = super().get_queryset()
        for post in queryset:
            post.textPost = post.textPost[:20] + '...'  # Обрезаем поле textPost
        return queryset



class detailpostlist(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        return context
