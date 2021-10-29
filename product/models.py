from django.db import models
from django.contrib.auth import get_user_model
from model_utils import Choices
from model_utils.fields import StatusField
from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from account.models import CustomUser

# from likes.models import Like

User = get_user_model()


# class Product(models.Model):
#     body = models.CharField(max_length=140)
#     likes = GenericRelation(Like)

# def __str__(self):
#     return self.body
#
# @property
# def total_likes(self):
#     return self.like.count()


class CreatedatModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    """Создание абстрактной модели для добавления поля созданием продукта. Нужен для сокращение кода и расширяемости """

    class Meta:
        abstract = True


class Movi(CreatedatModel):
    STATUS = Choices(
        ('Action movie', 'Боевик'),
        ('Detective', 'Детектив'),
        ('comedy', 'комедия'),
        ('fantastic', 'фантастика'),
        ('horror', 'ужас'),
    )
    title = models.CharField(max_length=100)
    producer = models.CharField(max_length=55)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='fin', null=True, blank=True)
    video = models.FileField(upload_to='films', null=True, blank=True)
    data = models.DecimalField(max_digits=4, decimal_places=2)

    genre = StatusField()
    description = models.TextField()

    # products = models.Manager()

    class Meta:
        ordering = ['title', 'price', 'image']

    def __str__(self):
        return self.title


class ProductReview(CreatedatModel):
    product = models.ForeignKey(Movi, on_delete=models.CASCADE, related_name='reviews')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews', null=True)
    text = models.TextField()
    rating = models.PositiveSmallIntegerField(default=1)


class Rating(CreatedatModel):
    post = models.ForeignKey(
        Movi, on_delete=models.CASCADE,
        related_name='rating'
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='rating', null=True
    )
    rating = models.PositiveIntegerField()
