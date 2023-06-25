# Generated by Django 4.1.7 on 2023-03-09 16:50

import cloudinary.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("storeapp", "0011_alter_product_seller_name_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="timestamp",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.CreateModel(
            name="ImageModel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "image",
                    cloudinary.models.CloudinaryField(
                        max_length=255, verbose_name="image"
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="product_image",
                        to="storeapp.product",
                    ),
                ),
            ],
        ),
    ]
