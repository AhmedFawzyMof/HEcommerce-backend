from django.db import models
from django.contrib.auth.models import User
from .models import *

class Size(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
class Color(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    

class Tags(models.Model):
    name   = models.CharField(max_length=255)
    nameAr = models.CharField(max_length=255)
    slug   = models.SlugField()

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return f'/{self.slug}/'


class Category(models.Model):
    name   = models.CharField(max_length=255)
    nameAr = models.CharField(max_length=255)
    slug   = models.SlugField()

    class Meta:
        ordering = ('name',)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return f'/category/{self.slug}/'

class Product(models.Model):
    sizes         = models.ManyToManyField(Size, related_name='products',blank=True)
    colors        = models.ManyToManyField(Color, related_name='products',blank=True)
    tag           = models.ManyToManyField(Tags,related_name='products')
    category      = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    nameAr        = models.CharField(max_length=255)
    name          = models.CharField(max_length=255)
    slug          = models.SlugField()
    description   = models.TextField(blank=True, null=True)
    descriptionAr = models.TextField(blank=True, null=True)
    price         = models.IntegerField()
    image         = models.ImageField(upload_to='products/', blank=True, null=True)
    date_added    = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-date_added',)
    
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return f'/category/{self.category.slug}/products/{self.slug}/'
    
    def get_image(self):
        if self.image:
            return 'http://127.0.0.1:8000' + self.image.url
        return ''

class Comment(models.Model):
    user    = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product,related_name='comments', on_delete=models.CASCADE)
    titles  = models.TextField()
    rate    = models.CharField(max_length=10)
    react   = models.CharField(max_length=100)
    comment = models.TextField()

    def __str__(self):
        return self.react

    def get_username(self):
        return self.user.username

    def get_email(self):
        return self.user.email

