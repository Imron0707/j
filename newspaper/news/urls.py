from django.urls import path
from .views import postList
from .views import detailpostlist, NewsCreate, ArticleCreate, NewsUpdate, ArticleUpdate, NewsDelete, ArticleDelete


urlpatterns = [
    path('', postList.as_view(), name='news'),
    path('<int:pk>/', detailpostlist.as_view(), name='detailpostlist'),
    path('news_create/', NewsCreate.as_view(), name='news_edit'),
    path('article_create/', ArticleCreate.as_view(), name='article_edit'),
    path('<int:pk>/update/', NewsUpdate.as_view(), name='news_update'),
    path('<int:pk>/update/', ArticleUpdate.as_view(), name='article_update'),
    path('<int:pk>/delete/', NewsDelete.as_view(), name='news_delete'),
    path('<int:pk>/delete/', ArticleDelete.as_view(), name='article_delete'),
]