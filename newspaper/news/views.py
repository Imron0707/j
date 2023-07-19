from django.views.generic import ListView
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from datetime import datetime
from .models import Post
from .filters import PostFilter
from django.urls import reverse_lazy
from .forms import PostFormNews, PostFormArticle

class postList(ListView):
    model = Post
    template_name = 'news.html'
    context_object_name = 'posts'
    ordering = '-createPost'  # Указываем поле для упорядочивания объектов
    paginate_by = 7

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        queryset = self.filterset.qs
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if hasattr(self, 'filterset'):
            context['filterset'] = self.filterset
        return context

class detailpostlist(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        return context


class NewsCreate(CreateView):
    form_class = PostFormNews
    # модель товаров
    model = Post
    # и новый шаблон, в котором используется форма.
    template_name = 'news_edit.html'


class ArticleCreate(CreateView):
    form_class = PostFormArticle
    # модель товаров
    model = Post
    # и новый шаблон, в котором используется форма.
    template_name = 'article_edit.html'


class NewsUpdate(UpdateView):
    form_class = PostFormNews
    # модель товаров
    model = Post
    # и новый шаблон, в котором используется форма.
    template_name = 'news_edit.html'



class ArticleUpdate(UpdateView):
    form_class = PostFormArticle
    # модель товаров
    model = Post
    # и новый шаблон, в котором используется форма.
    template_name = 'article_edit.html'


class NewsDelete(DeleteView):
    model = Post
    template_name = 'news_delete.html'
    success_url = reverse_lazy('news')



class ArticleDelete(DeleteView):
    model = Post
    template_name = 'article_delete.html'
    success_url = reverse_lazy('news')
