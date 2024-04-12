from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAdminUser, AllowAny
from .serilaizers import ProductImageSerilaizer, ProductListSerilaizer, ProductSerilaizer, CategorySerilaizer
from .models import Category, Product, ProductImage
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page


class PermissionMixin:
    def get_permissions(self):
        if self.action in ('retrieve', 'list'):
            permissions = [AllowAny]
        else:
            permissions = [IsAdminUser]
        return [permission() for permission in permissions]


class CategoryView(PermissionMixin, ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerilaizer


class ProductView(PermissionMixin, ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerilaizer

    @method_decorator(cache_page(60*5))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def get_serializer_class(self):
        if self.action == 'list':
            return ProductListSerilaizer
        return self.serializer_class


class ProductImageView(CreateAPIView):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerilaizer
    permission_classes = [IsAdminUser]
