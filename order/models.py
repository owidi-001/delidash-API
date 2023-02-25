from django.db import models
from django.utils import timezone

from address.models import UserAddress
from product.models import Product
from rider.models import Rider
from user.models import User


# Create your models here.
class Order(models.Model):
    # date and time ordered, dispatched and delivered
    date_ordered=models.DateTimeField(auto_now_add=timezone.now(),auto_created=True)
    date_dispatched=models.DateTimeField(blank=True,null=True)
    date_delivered=models.DateTimeField(blank=True,null=True)
    # Product ordered
    item=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.IntegerField(default=1)
    # TODO! replace status by shorter values
    STATUS = (
        ("Pending", "Pending"), ("Dispatched", "Dispatched"), ("Completed", "Completed"), ("Cancelled", "Cancelled"))
    status = models.CharField(max_length=20, choices=STATUS, default="Pending")
    pickup_address = models.ForeignKey(UserAddress, on_delete=models.CASCADE,related_name="source")
    delivery_address=models.ForeignKey(UserAddress,on_delete=models.CASCADE,related_name="destination")
    customer=models.ForeignKey(User,on_delete=models.CASCADE)
    payment_phone=models.CharField(max_length=10,null=True,blank=True)
    rider=models.ForeignKey(Rider,on_delete=models.CASCADE,blank=True,null=True)
    note=models.TextField(blank=True,null=True)


    @property
    def get_total(self) -> float:
        return self.item.unit_price * self.quantity

    @property
    def date(self):
        return self.date_ordered.strftime("%d %B, %Y")

    class Meta:
        verbose_name_plural = "Orders"

    def __str__(self) -> str:
        return f"{self.item}"