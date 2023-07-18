from django.urls import path
from .views import postList
from .views import detailpostlist


urlpatterns = [
    path('', postList.as_view(), name='news'),
    path('<int:pk>', detailpostlist.as_view()),
]