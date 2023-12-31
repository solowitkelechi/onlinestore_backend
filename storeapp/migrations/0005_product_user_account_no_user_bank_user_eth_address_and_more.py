# Generated by Django 4.1.7 on 2023-03-03 17:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("storeapp", "0004_remove_product_seller_name_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Product",
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
                ("name", models.CharField(max_length=200)),
                ("brand", models.CharField(max_length=100)),
                ("description", models.CharField(max_length=300)),
                ("price", models.FloatField()),
                ("quantity", models.IntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name="user",
            name="account_no",
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name="user",
            name="bank",
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="user",
            name="eth_address",
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.CreateModel(
            name="ProductDetail",
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
                ("gender", models.CharField(max_length=50)),
                ("size", models.CharField(max_length=100)),
                ("color", models.CharField(max_length=200)),
                ("screen_size", models.CharField(max_length=100)),
                ("memory", models.CharField(max_length=100)),
                ("storage_size", models.CharField(max_length=100)),
                ("operating_system", models.CharField(max_length=100)),
                ("cpu_processor", models.CharField(max_length=200)),
                ("graphic_card", models.CharField(max_length=200)),
                ("battery_cell", models.CharField(max_length=200)),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="storeapp.product",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="product",
            name="seller_name",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.CreateModel(
            name="OrderHistory",
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
                ("order_date", models.DateTimeField(auto_now_add=True)),
                ("delivered", models.BooleanField(default=False)),
                ("in_transit", models.BooleanField(default=False)),
                ("address", models.CharField(max_length=300, null=True)),
                (
                    "product",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="storeapp.product",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
