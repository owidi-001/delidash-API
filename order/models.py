from django.utils import timezone
from django.db import models
from product.models import Product
from address.models import Address
from user.models import User
from rider.models import Rider

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
    delivery_address=models.ForeignKey(Address,on_delete=models.CASCADE)
    customer=models.ForeignKey(User,on_delete=models.CASCADE)
    # payment_phone=models.CharField(max_length=10,null=True,blank=True)
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