from django.db import models


# Категории
class Category(models.Model):
    title = models.CharField(max_length=256)
    slug = models.SlugField(max_length=64, unique=True)
    output_order = models.PositiveSmallIntegerField(max_length=32767, default=100)
    is_published = models.BooleanField(default=True)


# Топинги
class Topping(models.Model):
    title = models.CharField(max_length=256)
    slug = models.SlugField(max_length=64, unique=True)
    is_published = models.BooleanField(default=True)


# Обёртки
class Wrapper(models.Model):
    title = models.CharField(max_length=256)
    is_published = models.BooleanField(default=True)


# Сорта мороженого
class IceCream(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField()
    is_on_main = models.BooleanField(default=False)
    is_published = models.BooleanField(default=True)
