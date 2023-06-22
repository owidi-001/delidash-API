from django.db import models
from user.models import User

# Create your models here.
class Address(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    lat= models.FloatField(default=0)
    long= models.FloatField(default=0)
    placemark= models.CharField(max_length=100)
    building= models.CharField(max_length=100)
    floor= models.CharField(max_length=100)
    room = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        verbose_name_plural = "addresses"

    def __str__(self):
        return self.placemark

class UserAddress(models.Model):
    address=models.ForeignKey(Address, on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)