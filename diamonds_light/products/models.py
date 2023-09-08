from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=30, verbose_name='Название')
    image = models.ImageField(upload_to='category_images/', verbose_name='Фото')
    is_active = models.BooleanField(default=True, verbose_name='Активная')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=100, unique=True, null=False, verbose_name="Ссылка")

    def get_absolute_url(self):
        return reverse('category', kwargs={"category_id_id": self.pk})

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['id']


class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название')
    slug = models.CharField(max_length=150, db_index=True, unique=True, null=False, verbose_name="Ссылка")
    description = models.TextField(verbose_name='Описание')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    image = models.ImageField(upload_to='products/', verbose_name='Фото')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, verbose_name='Категория')
    stock = models.IntegerField(verbose_name='Количество')
    date_added = models.DateTimeField(auto_now_add=True, verbose_name='Добавлен')
    is_active = models.BooleanField(default=True, verbose_name='В наличии')
    discount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, verbose_name='Скидка')

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['id']
