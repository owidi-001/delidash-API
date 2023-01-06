from django.db import models
from user.models import User


# Create your models here.
class Rider(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    brand = models.CharField(max_length=50, null=True, blank=True)
    dob = models.CharField(max_length=10, blank=True, null=True)
    GENDER = (("male", "male"), ("female", "female"))
    gender = models.CharField(max_length=6, choices=GENDER)
    national_id = models.CharField(max_length=8, blank=True, null=True)
    license = models.CharField(max_length=9)
    available = models.BooleanField(default=True)

    def __str__(self) -> str:
        return f"{self.brand}"

    @property
    def is_available(self):
        return self.available
