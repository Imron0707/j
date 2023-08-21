from django.urls import path
from .views import postList
from .views import detailpostlist, NewsCreate, ArticleCreate, NewsUpdate, ArticleUpdate, NewsDelete, ArticleDelete, CategoryListView, subscribe


urlpatterns = [
    path('', postList.as_view(), name='news'),
    path('<int:pk>/', detailpostlist.as_view(), name='detailpostlist'),
    path('news_create/', NewsCreate.as_view(), name='news_edit'),
    path('article_create/', ArticleCreate.as_view(), name='article_edit'),
    path('<int:pk>/update/news/', NewsUpdate.as_view(), name='news_update'),
    path('<int:pk>/update/article/', ArticleUpdate.as_view(), name='article_update'),
    path('<int:pk>/delete/news/', NewsDelete.as_view(), name='news_delete'),
    path('<int:pk>/delete/article/', ArticleDelete.as_view(), name='article_delete'),
    path('category/<int:pk>/', CategoryListView.as_view(), name='category_list'),
    path('category/<int:pk>/subscribe', subscribe, name='subscribe')
]