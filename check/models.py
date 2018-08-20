from django.db import models

# Create your models here.


class Query(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length=200)
    ipaddress = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    mac = models.CharField(max_length=200)

