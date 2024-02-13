
from django.db import models

# Create your models here.
# models.py

from django.contrib.auth.models import User




class Contact(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=10, blank=True)
    message = models.TextField(max_length=500, blank=True)

    def __str__(self):
        return self.name + ",Phone No:" + self.phone


# Create your models here.
