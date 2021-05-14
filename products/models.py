from django.db import models

# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=20)
    income=models.IntegerField(default=0)
    marital_status=models.TextField(default=' ')
    employment_status= models.TextField(default=' ')
    graduate=models.BooleanField(default=False)
    dependants=models.IntegerField(default=0)
