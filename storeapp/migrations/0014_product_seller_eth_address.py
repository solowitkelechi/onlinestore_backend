# Generated by Django 4.1.7 on 2023-04-14 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("storeapp", "0013_product_category_alter_productdetail_battery_cell_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="seller_eth_address",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
