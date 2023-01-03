from django.db import models
from user.models import User

# Create your models here.
class Contact(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    subject = models.CharField(max_length=250)
    message = models.TextField()
    upload = models.FileField(upload_to='contact/%Y/%m/%d/', null=True, blank=True)
