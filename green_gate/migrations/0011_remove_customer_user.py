# Generated by Django 4.1.7 on 2023-03-29 14:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('green_gate', '0010_delete_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='user',
        ),
    ]
