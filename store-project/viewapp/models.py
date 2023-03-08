from django.db import models
from django.urls import reverse

class Products(models.Model):
    title = models.CharField(max_length=100, verbose_name='Товар')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')
    price = models.IntegerField(null=True, blank=True, verbose_name='Цена')
    quantity = models.IntegerField(null=True, blank=True,verbose_name='Количество')
    release_date = models.DateField(verbose_name='Дата производства')
    data_upload = models.DateField(auto_now_add=True, db_index=True, verbose_name='Опубликовано')
    data_upgrade = models.DateField(auto_now_add=True, verbose_name='Дата обновления')
    images = models.ImageField(upload_to='img/', default = 'img/None/no-img.jpg', verbose_name='Фото')
    categories = models.ForeignKey('Categories', null=True, on_delete=models.PROTECT, verbose_name='Категория')
    
    def get_absolute_url(self):
        return reverse('post', kwargs={'post_id': self.pk})
    
    def __str__(self):
	    return self.title
        
class Meta:
    verbose_name = 'Продукт'
    verbose_name_plural = 'Продукты'
    ordering = ['id']

class Categories(models.Model):
    title = models.CharField(max_length=30, verbose_name='Категория')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    
    def get_absolute_url(self):
        return reverse('category_detail', kwargs={'cat_id': self.pk})

    def __str__(self):
	    return self.title
    
class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['id']


class Users(models.Model):
    uname = models.CharField(max_length=100, verbose_name='Имя')
    password = models.CharField(max_length=20, verbose_name='Пароль')
    email = models.EmailField()
    address = models.CharField(max_length=128, verbose_name='Адрес')
    def __str__(self):
	    return self.uname


class Orders(models.Model):
    total_price = models.IntegerField(verbose_name='Общая цена')
    order_date = models.DateField(auto_now_add=True)
    users = models.ForeignKey(Users, on_delete=models.CASCADE)


class OrderItems(models.Model):
    quantity = models.IntegerField(verbose_name='Количество')
    price = models.IntegerField(null=True, blank=True, verbose_name='Цена')
    products = models.ForeignKey(Products, on_delete=models.CASCADE)
    orders = models.ForeignKey(Orders, on_delete=models.CASCADE)






