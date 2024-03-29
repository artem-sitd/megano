from django.urls import path

from .views import (
    BannersApiView,
    CategoryListApi,
    LimitedProductsApiView,
    PopularApiView,
    ProductApiView,
    SalesApiView,
)

urlpatterns = [
    path("categories/", CategoryListApi.as_view()),
    path("catalog/", ProductApiView.as_view()),
    path("products/limited", LimitedProductsApiView.as_view()),
    path("sales", SalesApiView.as_view()),
    path("banners", BannersApiView.as_view()),
    path("products/popular", PopularApiView.as_view()),
]
