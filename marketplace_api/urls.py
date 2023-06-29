"""marketplace_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework_extensions.routers import NestedRouterMixin
from storeapp import views
from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter()
router.register(r"users", views.UserViewSet, "user")
router.register(r"products", views.ProductViewSet, "product")
router.register(r"productdetails", views.ProductDetailViewSet, "productdetail")
router.register(r"orderhistory", views.OrderHistoryViewSet, "orderhistory")


class NestedDefaultRouter(NestedRouterMixin, routers.DefaultRouter):
    pass


router = NestedDefaultRouter()

router.register("productdetails", views.ProductDetailViewSet)
router.register("orderhistory", views.OrderHistoryViewSet)

user_router = router.register("users", views.UserViewSet)
product_router = router.register("products", views.ProductViewSet)


user_router.register(
    "products",
    views.ProductViewSet,
    basename="user-products",
    parents_query_lookups=["user"],
)

user_router.register(
    "orderhistory",
    views.OrderHistoryViewSet,
    basename="user-orderhistory",
    parents_query_lookups=["user"],
)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
    path("userauth/", views.UserAuth.as_view()),
    path("randomproducts/", views.RandomProducts.as_view()),
    path("image/upload/", views.UploadImage.as_view()),
    path("image/<int:pk>/", views.ImageDetail.as_view()),
    path("productdetail/get/<int:pk>/", views.GetProductDetail.as_view()),
    path("orderhistory/get/<int:pk>/", views.GetOrderHistory.as_view()),
    path("productbycategory/<str:pk>/", views.ProductByCategory.as_view()),
    path("checkemail/", views.CheckEmail.as_view()),
    path("sendemail/", views.EmailView.as_view()),
    path(
        "saverecoverykey/", views.SavePasswordRecoveryInfo.as_view({"post": "create"})
    ),
    path('passwordrecovery/', views.PasswordRecoveryView.as_view()),
    path('passwordrecovery/<int:pk>/', views.PasswordRecoveryDetail.as_view()),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
