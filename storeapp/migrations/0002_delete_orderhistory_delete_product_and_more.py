# Generated by Django 4.1.7 on 2023-03-03 17:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("storeapp", "0001_initial"),
    ]

    operations = [
        migrations.DeleteModel(
            name="OrderHistory",
        ),
        migrations.DeleteModel(
            name="Product",
        ),
        migrations.DeleteModel(
            name="ProductDetail",
        ),
    ]