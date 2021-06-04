from django.db import models

# Create your models here.
class Product(models.Model):
    married=models.BooleanField(default=False)
    graduate=models.BooleanField(default=False)
    dependants=models.IntegerField(default=0)
    self_employed=models.BooleanField(default=False)
    applicant_income=models.IntegerField(default=0)
    coapplicant_income=models.IntegerField(default=0)
    semi_urban=models.BooleanField(default=False)
    urban=models.BooleanField(default=False)
    Loan_Amount_Term=models.IntegerField(default=0)

class Signup(models.Model):
    name=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
    sex=models.TextField(default=' ')
    DOB= models.DateField(auto_now=True)
    phone_number=models.IntegerField(default=0)
    city=models.CharField(max_length=20)
