from datetime import date
from django.db import models
from django.utils import timezone

from vendor.models import Vendor


class Category(models.Model):
    name = models.CharField(max_length=50)
    icon = models.ImageField(upload_to="category//%Y/%m/%d/")
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = 'categories'
        verbose_name_plural = 'categories'
        ordering = ('name','-date_created')


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200)
    unit = models.CharField(max_length=2,
                            choices=(("kg", "kg"), ("g", "g"), ("l", "l"), ("ml", "ml"),
                                     ("in", "in")), default="kg",help_text="Quantity measurement metrics")

    unit_price = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='unit price',help_text="Price per given unit")
    image = models.ImageField(upload_to="product//%Y/%m/%d/")
    description = models.TextField(blank=True, verbose_name="description")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    stock = models.PositiveIntegerField(verbose_name='stock', default=1)
    date_added = models.DateTimeField(auto_now_add=True,blank=True,null=True)

    def __str__(self):
        return f"{self.name}"

    @property
    def is_new(self):
        return (date.today() - self.date_added.date()).days <= 2

    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'products'
        ordering = ('name','-date_added')
