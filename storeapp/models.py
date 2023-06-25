from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from django.utils import timezone
from cloudinary.models import CloudinaryField

# Create your models here.

# using User as foreignkey
# models.ForeignKey(settings.AUTH_USER_MODEL,)
# OR from django.contrib.auth import get_user_model
# User = get_user_model()

AbstractUser._meta.get_field("email")._unique = True


class User(AbstractUser):
    bank = models.CharField(max_length=255, null=True)
    account_no = models.CharField(max_length=20, null=True)
    eth_address = models.CharField(max_length=100, default="0x0000", blank=True)
    phone_number = models.CharField(max_length=16, null=True)

    def __str__(self):
        return "%s" % (self.username)


class Product(models.Model):
    seller_name = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="product",
        on_delete=models.CASCADE,
        null=True,
    )
    seller_eth_address = models.CharField(max_length=200, null=True, blank=True)
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=200, null=True)
    brand = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    price = models.FloatField()
    quantity = models.IntegerField(default=0)
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return "%s: %s, %s = %i" % (
            self.seller_name,
            self.name,
            self.brand,
            self.quantity,
        )


class ImageModel(models.Model):
    product = models.ForeignKey(
        Product, related_name="product_image", on_delete=models.CASCADE
    )
    image = CloudinaryField("image")

    @property
    def image_url(self):
        return f"https://res.cloudinary.com/dkv8jgh7c/{self.image}"


class ProductDetail(models.Model):
    product = models.ForeignKey(
        Product, related_name="productdetail", on_delete=models.CASCADE, null=True
    )
    gender = models.CharField(max_length=50, null=True, blank=True)
    size = models.CharField(max_length=100, null=True, blank=True)
    color = models.CharField(max_length=200, null=True, blank=True)
    screen_size = models.CharField(max_length=100, null=True, blank=True)
    memory = models.CharField(max_length=100, null=True, blank=True)
    storage_size = models.CharField(max_length=100, null=True, blank=True)
    operating_system = models.CharField(max_length=100, null=True, blank=True)
    cpu_processor = models.CharField(max_length=200, null=True, blank=True)
    graphic_card = models.CharField(max_length=200, null=True, blank=True)
    battery_cell = models.CharField(max_length=200, null=True, blank=True)


class OrderHistory(models.Model):
    buyer_name = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="orderhistory",
        on_delete=models.CASCADE,
        null=True,
    )
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    order_date = models.DateTimeField(
        auto_now_add=True,
    )
    delivered = models.BooleanField(default=False)
    in_transit = models.BooleanField(default=False)
    address = models.CharField(max_length=300, null=True)


class PasswordRecoveryManager(models.Manager):
    def get_queryset(self):
        return (
            super()
            .get_queryset()
            .filter(
                originated_date__gte=timezone.now() - timezone.timedelta(minutes=10)
            )
        )


class PasswordRecovery(models.Model):
    user = models.ForeignKey(
        User, related_name="password_recovery", on_delete=models.CASCADE
    )
    key = models.CharField(max_length=20, default="", unique=True)
    originated_date = models.DateTimeField(default=timezone.now)
