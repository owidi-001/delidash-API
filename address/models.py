from django.db import models
from user.models import User

# Create your models here.
class Address(models.Model):
    room = models.CharField(max_length=5, blank=True, null=True)
    floor = models.CharField(max_length=5, blank=True, null=True)
    block = models.CharField(max_length=100, blank=True, null=True)
    placemark=models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        verbose_name_plural = "location"

    def __str__(self):
        return f"""Placemark: {self.placemark}
                Room:{self.room}
                Floor: {self.floor}
                Block: {self.block}
                """


# Links the user to an address
class UserAddress(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)     
    address=models.ForeignKey(Address,on_delete=models.CASCADE)   