from django.contrib.auth.models import User
from django.db import models
from django.db.models import Sum
from django.urls import reverse


class Author(models.Model):
    author = models.OneToOneField(User, on_delete=models.CASCADE)
    ratingauthor = models.SmallIntegerField(default=0)

    def update_rating(self):
        postRat = self.post_set.aggregate(postRating=Sum('rating'))
        pRat = 0
        pRat += postRat.get('postRating')

        commentRat = self.author.comment_set.aggregate(commentRating=Sum('rating'))
        cRat = 0
        cRat += commentRat.get('commentRating')

        self.ratingauthor = pRat * 3 + cRat
        self.save()


class Category(models.Model):
    name = models.CharField(max_length=64,
                            default='Education',
                            unique=True)


Article = 'Ar'
News = 'Nw'

NEAR = [
    (Article, 'Статья'),
    (News, 'Новость')
]


class Post(models.Model):
    post_type = models.CharField(max_length=2, choices=NEAR, default=News)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    headerPost = models.CharField(max_length=256)  # Заголовок поста
    textPost = models.TextField()  # текст поста
    previewPost = models.CharField(max_length=512, default='')  # Превью поста
    createPost = models.DateTimeField(auto_now_add=True)  # Дата создания
    rating = models.SmallIntegerField(default=0)  # Рейтинг пользователя
    categoryes = models.ManyToManyField(Category, through='PostCategory')  # Поле категории
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    image_url = models.URLField(null=True, blank=True)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

    def get_absolute_url(self):
        return reverse('detailpostlist', args=[str(self.id)])


class Comment(models.Model):
    PostComment = models.ForeignKey(Post, on_delete=models.CASCADE)
    CommentUser = models.ForeignKey(User, on_delete=models.CASCADE)
    textComment = models.TextField()
    commentcreate = models.DateTimeField(auto_now_add=True)
    rating = models.SmallIntegerField(default=0)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()


class PostCategory(models.Model):
    posts = models.ForeignKey(Post, on_delete=models.CASCADE)
    categoryThough = models.ForeignKey(Category, on_delete=models.CASCADE)
