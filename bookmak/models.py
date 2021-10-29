from django.db import models
from typing import List, Tuple
import product
from django.db import models
from account.models import CustomUser
from product.models import Movi


class Bookmark(models.Model):
    post = models.ForeignKey(Movi, on_delete=models.CASCADE)
    user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name='bookmak'
    )

    class Meta:
        ordering = ('-pk',)

        unique_together: List[Tuple[str, str]] = [
            ('post', 'user'),
        ]

        indexes: List[models.Index] = [
            models.Index(fields=('post', 'user')),
        ]
