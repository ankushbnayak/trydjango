from django.db import models

# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=20)
    income=models.IntegerField(default=0)
    marital_status=models.TextField(default=' ')
    employment_status= models.TextField(default=' ')
    graduate=models.BooleanField(default=False)
    dependants=models.IntegerField(default=0)

class Signup(models.Model):
    name=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
    sex=models.TextField(default=' ')
    DOB= models.DateField(auto_now=True)
    phone_number=models.IntegerField(default=0)
    city=models.CharField(max_length=20)
