# Generated by Django 4.2.3 on 2023-08-28 07:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('green_gate', '0017_feedback_sname'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feedback',
            name='sname',
        ),
    ]