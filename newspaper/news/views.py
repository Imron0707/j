from django.views.generic import ListView
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin
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


class NewsCreate(PermissionRequiredMixin, CreateView):
    permission_required = ('news.add_Post',)
    form_class = PostFormNews
    # модель товаров
    model = Post
    # и новый шаблон, в котором используется форма.
    template_name = 'news_edit.html'


class ArticleCreate(PermissionRequiredMixin, CreateView):
    permission_required = ('news.add_Post',)
    form_class = PostFormArticle
    # модель товаров
    model = Post
    # и новый шаблон, в котором используется форма.
    template_name = 'article_edit.html'


class NewsUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = ('news.change_Post',)
    form_class = PostFormNews
    # модель товаров
    model = Post
    # и новый шаблон, в котором используется форма.
    template_name = 'news_edit.html'


class ArticleUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = ('news.change_Post',)
    form_class = PostFormArticle
    # модель товаров
    model = Post
    # и новый шаблон, в котором используется форма.
    template_name = 'article_edit.html'


class NewsDelete(PermissionRequiredMixin, DeleteView):
    permission_required = ('news.delete_Post',)
    model = Post
    template_name = 'news_delete.html'
    success_url = reverse_lazy('news')


class ArticleDelete(PermissionRequiredMixin, DeleteView):
    permission_required = ('news.delete_Post',)
    model = Post
    template_name = 'article_delete.html'
    success_url = reverse_lazy('news')
