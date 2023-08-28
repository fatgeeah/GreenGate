# Generated by Django 4.2.3 on 2023-08-28 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('green_gate', '0019_delete_feedback'),
    ]

    operations = [
        migrations.CreateModel(
            name='FeedBack',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('feedback', models.TextField()),
            ],
        ),
    ]