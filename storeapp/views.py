from django.shortcuts import render, get_object_or_404
from .serializers import (
    UserSerializer,
    ProductSerializer,
    ProductDetailSerializer,
    OrderHistorySerializer,
    ImageModelSerializer,
    ImageSerializer,
    PasswordRecoveryInfoSerializer,
)
from .models import (
    User,
    Product,
    ProductDetail,
    OrderHistory,
    ImageModel,
    PasswordRecovery,
)
from rest_framework import viewsets, permissions, status, views, generics
from rest_framework_extensions.mixins import NestedViewSetMixin
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView, RetrieveAPIView
from rest_framework.parsers import MultiPartParser
import json, requests
from django.core.mail import EmailMultiAlternatives, send_mail
from django.core import serializers
from rest_framework_api_key.permissions import HasAPIKey
from django.contrib.auth.hashers import check_password, make_password
from django.http import Http404
from rest_framework.pagination import PageNumberPagination
import random
from django.utils import timezone

# Create your views here.


class UserViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class ProductViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class RandomProducts(views.APIView):
    def get(self, request):
        randomProducts = []
        indexChecklist = []
        products = Product.objects.all()
        i = 0
        while i <= 4:
            while True:
                randomIndex = random.randint(0, len(products) - 1)
                if randomIndex not in indexChecklist:
                    break
            randomProducts.append(products[randomIndex])
            indexChecklist.append(randomIndex)
            i = i + 1
        serializer = ProductSerializer(randomProducts, many=True)
        return Response(serializer.data)


class ProductByCategory(views.APIView, PageNumberPagination):

    page_size = 20

    def get_object(self, pk):
        try:
            return Product.objects.filter(category=pk).order_by("timestamp")
        except Product.DoesNotExist:
            raise HTTP404

    def get(self, request, pk, format=None):
        product = self.get_object(pk)
        results = self.paginate_queryset(product, request, view=self)
        serializer = ProductSerializer(results, many=True)
        return self.get_paginated_response(serializer.data)


class ProductDetailViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    serializer_class = ProductDetailSerializer
    queryset = ProductDetail.objects.all()


class GetProductDetail(views.APIView):
    def get_object(self, pk):
        try:
            return ProductDetail.objects.get(product=pk)
        except ProductDetail.DoesNotExist:
            raise HTTP404

    def get(self, request, pk, format=None):
        detail = self.get_object(pk)
        serializer = ProductDetailSerializer(detail)
        return Response(serializer.data)


class OrderHistoryViewSet(viewsets.ModelViewSet):
    serializer_class = OrderHistorySerializer
    queryset = OrderHistory.objects.all()


class GetOrderHistory(views.APIView):
    def get_object(self, pk):
        try:
            return OrderHistory.objects.get(buyer_name=pk)
        except OrderHistory.DoesNotExist:
            raise HTTP404

    def get(self, request, pk, format=None):
        history = self.get_object(pk)
        serializer = OrderHistorySerializer(history)
        return Response(serializer.data)


class UploadImage(CreateAPIView):
    serializer_class = ImageModelSerializer
    parser_classes = (MultiPartParser,)
    queryset = ImageModel.objects.all()


class ImageDetail(views.APIView):
    def get_object(self, pk):
        try:
            return ImageModel.objects.get(product=pk)
        except ImageModel.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        image = self.get_object(pk)
        serializer = ImageModelSerializer(image)
        return Response(serializer.data)


class UserAuth(views.APIView):
    def post(self, request, *args, **kwargs):
        email = request.data.get("email", None)
        password = request.data.get("password", None)
        try:
            auth_user = User.objects.get(email=email)
        except:
            auth_user = None
        if auth_user is not None:
            auth_pwd = check_password(password, auth_user.password)
            if not auth_pwd:
                print(auth_pwd, password)
                print(make_password(password))
                print(auth_user.password)
                return Response(
                    {"status": "failed", "message": "password authentication failed"}
                )
            else:
                print(auth_pwd, password)
                print(make_password(password))
                print(auth_user.password)
                serializer = UserSerializer(auth_user, many=False)
                return Response({"status": "success", "data": serializer.data})
        else:
            return Response(
                {"status": "failed", "message": "email authentication failed"}
            )


class RegisterView(views.APIView):
    def post(self, request, *args, **kwargs):
        data = request.data.get("data", None)
        response = requests.post(
            "http://localhost:8000/api/user/",
            data=json.dumps(data),
            headers={"Content-Type": "application/json"},
        )
        if response.status_code == 201:
            return Response(response.json())
        else:
            return Response({"status": "failed", "message": response.json()})


class SavePasswordRecoveryInfo(viewsets.ModelViewSet):
    serializer_class = PasswordRecoveryInfoSerializer
    queryset = PasswordRecovery.objects.all()


class PasswordRecoveryView(views.APIView):
    def post(self, request, *args, **kwargs):
        key = request.data.get("key", None)
        try:
            query = PasswordRecovery.objects.filter(
                originated_date__gte=timezone.now() - timezone.timedelta(minutes=5)
            )
            result = query.get(key=key)
        except:
            result = None

        if result is not None:
            print("data is in db")
            serializer = PasswordRecoveryInfoSerializer(result, many=False)
            return Response({"status": "success", "data": serializer.data})
        else:
            print(result)
            return Response({"status": "failed"})


class PasswordRecoveryDetail(views.APIView):
    def get_object(self, pk):
        try:
            return PasswordRecovery.objects.get(pk=pk)
        except PasswordRecovery.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        query = self.get_object(pk)
        serializer = PasswordRecoveryInfoSerializer(query, many=False)
        return Response(serializer.data)

    def delete(self, request, pk, format=None):
        query = self.get_object(pk)
        query.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CheckEmail(views.APIView):
    def post(self, request, *args, **kwargs):
        email = request.data.get("email", None)
        try:
            user = User.objects.get(email=email)
        except:
            user = None

        if user is not None:
            serializer = UserSerializer(user, many=False)
            return Response({"status": "success", "data": serializer.data})
        else:
            return Response({"status": "failed"})


class EmailView(views.APIView):
    def post(self, request, *args, **kwargs):
        subject = request.data.get("subject", None)
        text_content = request.data.get("text_content", None)
        toEmail = request.data.get("email", None)
        html_content = request.data.get("html_content", None)
        from_email = "solomonilo11@live.com"
        msg = EmailMultiAlternatives(
            subject,
            text_content,
            from_email,
            [toEmail],
        )
        msg.attach_alternative(html_content, "text/html")
        response = msg.send()

        if response == 1:
            print(response)
            return Response({"status": True})
        else:
            print(response)
            return Response({"status": False})
