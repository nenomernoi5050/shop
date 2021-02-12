from django.db import models
from parser_site.models import CardProduct


class PageHit(models.Model):
    count = models.PositiveIntegerField(default=0, verbose_name='Просмотры')
    product = models.ForeignKey(CardProduct, on_delete=models.DO_NOTHING, verbose_name='Товар')

    class Meta:
        verbose_name = 'счётчик'
        verbose_name_plural = 'счётчики'

    def __str__(self):
        return self.product.title
