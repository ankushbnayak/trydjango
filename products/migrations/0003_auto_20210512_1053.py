# Generated by Django 2.1.5 on 2021-05-12 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20210512_1026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='age',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='product',
            name='emp_status',
            field=models.TextField(default=' '),
        ),
        migrations.AlterField(
            model_name='product',
            name='mar_status',
            field=models.TextField(default=' '),
        ),
    ]
