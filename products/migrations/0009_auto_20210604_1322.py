# Generated by Django 2.1.5 on 2021-06-04 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_auto_20210518_1205'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='income',
            new_name='Loan_Amount_Term',
        ),
        migrations.RemoveField(
            model_name='product',
            name='employment_status',
        ),
        migrations.RemoveField(
            model_name='product',
            name='marital_status',
        ),
        migrations.RemoveField(
            model_name='product',
            name='name',
        ),
        migrations.AddField(
            model_name='product',
            name='applicant_income',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='product',
            name='coapplicant_income',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='product',
            name='married',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='self_employed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='semi_urban',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='urban',
            field=models.BooleanField(default=False),
        ),
    ]
