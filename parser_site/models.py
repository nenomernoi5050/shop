from django.db import models
from django.db.models import ManyToManyField
from django.urls import reverse

from parser_site.utils import transliterate



class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    name_slug = models.CharField(max_length=250)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


class Subcategory(models.Model):
    name = models.CharField(max_length=250, verbose_name='Название')
    name_slug = models.CharField(max_length=250)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    sorted = models.IntegerField(verbose_name='Сортировка', blank=True, null=True)
    view_menu = models.BooleanField(default=True, verbose_name='Показывать в меню')


    class Meta:
        verbose_name = "Подраздел"
        verbose_name_plural = "Подразделы"




    def __str__(self):
        return self.name


class CardProduct(models.Model):
    title = models.CharField(max_length=150, verbose_name="Название")
    price = models.IntegerField(verbose_name="Цена", null=True)
    size = models.CharField(max_length=50, verbose_name="Размеры", null=True, blank=True)
    desc_one = models.TextField(verbose_name="Описание часть 1", null=True, blank=True)
    url = models.URLField(verbose_name='Ссылка на оригинал', unique=True)
    subcategory = ManyToManyField(Subcategory,   null=True, verbose_name="Разделы")
    slug = models.CharField(max_length=150,  verbose_name="slug")


    def get_sub_cat(self):
        list = self.subcategory.all()
        list_str = ''
        for sub_cat in list:
            list_str += '/ \n ' + sub_cat.name
        return list_str.lstrip(', ')

    get_sub_cat.short_description = 'Подкатегории'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = transliterate(self.title)
        super().save(*args,*kwargs)


    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"


    def __str__(self):
        return self.title



    def old_price(self):
        return self.price + 700

    def get_absolute_url(self):
        return reverse("detail", kwargs={"slug": self.slug})

class CardFoto(models.Model):
    product = models.ForeignKey(CardProduct,  verbose_name='Товар', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/', verbose_name='Изображение')
    timestamp = models.DateField(auto_now_add=True)
    sorted = models.IntegerField(null=True, blank=True, default=10)


    class Meta:
        ordering = ['sorted']
        verbose_name = "Изображение"
        verbose_name_plural = "Изображение"


    def __str__(self):
        return self.product.title




