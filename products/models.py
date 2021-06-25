from django.db import models

# Create your models here.
class Product(models.Model):
    married=models.IntegerField(default=0)
    gender=models.IntegerField(default=0)
    graduate=models.IntegerField(default=0)
    dependants=models.IntegerField(default=0)
    self_employed=models.IntegerField(default=0)
    loan_amount=models.IntegerField(default=0)
    applicant_income=models.IntegerField(default=0)
    coapplicant_income=models.IntegerField(default=0)
    semi_urban=models.IntegerField(default=0)
    urban=models.IntegerField(default=0)
    Loan_Amount_Term=models.IntegerField(default=0)

class Signup(models.Model):
    name=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
    sex=models.TextField(default=' ')
    DOB= models.DateField(auto_now=True)
    phone_number=models.IntegerField(default=0)
    city=models.CharField(max_length=20)
