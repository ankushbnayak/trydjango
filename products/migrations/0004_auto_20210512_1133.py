# Generated by Django 2.1.5 on 2021-05-12 06:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20210512_1053'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='emp_status',
            new_name='employement_status',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='mar_status',
            new_name='marital_status',
        ),
    ]
