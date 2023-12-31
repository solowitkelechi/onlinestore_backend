# Generated by Django 4.1.7 on 2023-03-12 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("storeapp", "0012_product_timestamp_imagemodel"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="category",
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name="productdetail",
            name="battery_cell",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name="productdetail",
            name="color",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name="productdetail",
            name="cpu_processor",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name="productdetail",
            name="gender",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name="productdetail",
            name="graphic_card",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name="productdetail",
            name="memory",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="productdetail",
            name="operating_system",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="productdetail",
            name="screen_size",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="productdetail",
            name="size",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="productdetail",
            name="storage_size",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
