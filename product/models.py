from django.db import models
from slugify import slugify


class Category(models.Model):
    title = models.CharField(max_length=40, unique=True)
    slug = models.SlugField(max_length=40, primary_key=True, blank=True)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save()

class Product(models.Model):
    title = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(max_length=150, primary_key=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='media/', blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save()


class ProductImage(models.Model):
    image = models.ImageField(upload_to='media/')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    
    def __str__(self):
        return f'{self.image} -> {self.product.slug}'

