from rest_framework import serializers
from .models import (
    User,
    Product,
    ProductDetail,
    OrderHistory,
    ImageModel,
    PasswordRecovery,
)
from django.contrib.auth.hashers import make_password


class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductDetail
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    lookup_field = "category"

    class Meta:
        model = Product
        fields = "__all__"


class OrderHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderHistory
        fields = "__all__"


class ImageModelSerializer(serializers.ModelSerializer):
    image_url = serializers.ReadOnlyField()

    class Meta:
        model = ImageModel
        fields = ["product", "image_url", "image"]

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation.pop("image")

        return representation


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageModel
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    orderhistory = OrderHistorySerializer(many=True, read_only=True)
    product = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = "__all__"

    def create(self, validated_data):
        password = validated_data["password"]
        user = User.objects.create_user(
            username=validated_data["username"], email=validated_data["email"]
        )
        user.password = make_password(password)
        user.save()
        return user

    def update(self, instance, validated_data):
        if validated_data.get("eth_address"):
            instance.eth_address = validated_data.get("eth_address")
        if validated_data.get("password"):
            instance.password = make_password(
                validated_data.get("password", instance.password)
            )
        instance.save()
        return instance


class PasswordRecoveryInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PasswordRecovery
        fields = ("id", "key", "user")
