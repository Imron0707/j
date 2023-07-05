from django import template
from ..models import Post


register = template.Library()


@register.filter
def censor_text():
    my_objects = Post.textPost().split()
    sometxt = []  # добавить цензуриемые слова, если строка через split и приведение всех к одному регистру
    for i in range(len(my_objects)):
        for j in range(len(sometxt)):
            if my_objects[j] == sometxt[j]:
                my_objects[j] = my_objects[j][0] + ('*' * (len(my_objects) - 1))
            else:
                continue
    return my_objects
