from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views.generic import ListView
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin
from datetime import datetime
from .models import Post, Category
from .filters import PostFilter
from django.urls import reverse_lazy
from .forms import PostFormNews, PostFormArticle
from .task import text



class postList(ListView):
    model = Post
    template_name = 'news/news.html'
    context_object_name = 'posts'
    ordering = '-createPost'  # Указываем поле для упорядочивания объектов
    paginate_by = 5

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
    template_name = 'news/post.html'
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
    template_name = 'news/news_edit.html'


class ArticleCreate(PermissionRequiredMixin, CreateView):
    permission_required = ('news.add_Post',)
    form_class = PostFormArticle
    # модель товаров
    model = Post
    # и новый шаблон, в котором используется форма.
    template_name = 'news/article_edit.html'


class NewsUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = ('news.change_Post',)
    form_class = PostFormNews
    # модель товаров
    model = Post
    # и новый шаблон, в котором используется форма.
    template_name = 'news/news_edit.html'


class ArticleUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = ('news.change_Post',)
    form_class = PostFormArticle
    # модель товаров
    model = Post
    # и новый шаблон, в котором используется форма.
    template_name = 'news/article_edit.html'


class NewsDelete(PermissionRequiredMixin, DeleteView):
    permission_required = ('news.delete_Post',)
    model = Post
    template_name = 'news/news_delete.html'
    success_url = reverse_lazy('news')


class ArticleDelete(PermissionRequiredMixin, DeleteView):
    permission_required = ('news.delete_Post',)
    model = Post
    template_name = 'news/article_delete.html'
    success_url = reverse_lazy('news')


class CategoryListView(ListView):
    model = Post
    template_name = 'news/category_list.html'
    context_object_name = 'category_news_list'

    def get_queryset(self):
        self.category = get_object_or_404(Category, id=self.kwargs['pk'])
        queryset = Post.objects.filter(categoryes__id=self.category.id).order_by('-createPost')
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_not_subscriber'] = self.request.user not in self.category.subscribers.all()
        context['category'] = self.category
        return context

@login_required
def subscribe(request, pk):
    user = request.user
    category = Category.objects.get(id=pk)
    category.subscribers.add(user)

    message = 'Вы успешно подписались на рассылку новостей категории'
    return render(request, 'news/subscribe.html', {'category': category, 'message': message})


def index(request):
    text.delay()
    return render(request, 'index.html')