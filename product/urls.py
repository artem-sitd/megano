from django.urls import path

from .views import ProductDetailApiView, ProductDetailReview

urlpatterns = [
    path("product/<int:pk>", ProductDetailApiView.as_view()),
    path("product/<int:pk>/reviews", ProductDetailReview.as_view()),
]
