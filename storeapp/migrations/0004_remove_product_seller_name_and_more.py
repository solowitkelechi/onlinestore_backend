# Generated by Django 4.1.7 on 2023-03-03 17:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        (
            "storeapp",
            "0003_product_user_account_no_user_bank_user_eth_address_and_more",
        ),
    ]

    operations = [
        migrations.RemoveField(
            model_name="product",
            name="seller_name",
        ),
        migrations.RemoveField(
            model_name="productdetail",
            name="product",
        ),
        migrations.RemoveField(
            model_name="user",
            name="account_no",
        ),
        migrations.RemoveField(
            model_name="user",
            name="bank",
        ),
        migrations.RemoveField(
            model_name="user",
            name="eth_address",
        ),
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