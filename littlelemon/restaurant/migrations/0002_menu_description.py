# Generated by Django 5.0 on 2023-12-22 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='description',
            field=models.TextField(default='', max_length=1000),
        ),
    ]
