from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Product, ProductDetail, OrderHistory, ImageModel

# Register your models here.

admin.site.register(User, UserAdmin)
admin.site.register(Product)
admin.site.register(ProductDetail)
admin.site.register(OrderHistory)
admin.site.register(ImageModel)
