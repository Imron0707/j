from .models import Post
from django import forms
from django.core.exceptions import ValidationError


class PostFormNews(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'headerPost',  # Заголовок поста
            'previewPost',  # превью
            'textPost',  # текст поста
            'image',  # изображения
            'image_url',  # url изображения
        ]


class PostFormArticle(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'headerPost',  # Заголовок поста
            'previewPost',  # превью
            'textPost',  # текст поста
            'image',  # изображения
            'image_url',  # url изображения
        ]
        def clean(self):
            cleaned_data = super().clean()
            headerPost, textPost = cleaned_data.get("headerPost"), cleaned_data.get("textPost")
            if type(headerPost) is not str or len(headerPost) < 10:
                raise ValidationError({
                    "headerPost": "Описание не может быть менее 10 символов и должно быть строкой."
                })
            if textPost == headerPost:
                raise ValidationError(
                    "Заголовок не должно быть идентично тексту поста."
                )
