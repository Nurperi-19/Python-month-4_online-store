# Generated by Django 4.1.4 on 2022-12-22 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_category_product_categories'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='icon',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]