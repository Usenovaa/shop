from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryView, ProductImageView, ProductView


router = DefaultRouter()
router.register('categories', CategoryView)
router.register('products', ProductView)

urlpatterns = [
    path('', include(router.urls)),
    path('add-product-image/', ProductImageView.as_view())
]

