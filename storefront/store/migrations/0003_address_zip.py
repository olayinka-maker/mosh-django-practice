# Generated by Django 5.1.2 on 2024-12-09 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_product_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='zip',
            field=models.CharField(default='0000', max_length=20),
        ),
    ]
