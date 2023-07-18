from django_filters import FilterSet
from .models import Post


class PostFilter(FilterSet):
    class Meta:
        model = Post
        fields = {
           # поиск по названию
           'headerPost': ['icontains'],
           # количество товаров должно быть больше или равно
           'categoryes': ['icontains'],
            'textPost':['icontains']
       }
