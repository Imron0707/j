from django.urls import path
from .views import postList


urlpatterns = [
    path('', postList.as_view()),
]