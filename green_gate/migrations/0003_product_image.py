# Generated by Django 4.1.7 on 2023-03-27 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('green_gate', '0002_remove_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
