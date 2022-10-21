from django.shortcuts import render
from rest_framework import viewsets, filters
from .models import (
    Category,
    Brand,
    Product,
    Firm,
    Stock,
)
from .serializers import (
    CategorySerializer,
    BrandSerializer,
    ProductSerializer,
    FirmSerializer,
)
from rest_framework.permissions import DjangoModelPermissions
from django_filters.rest_framework import DjangoFilterBackend


class CategoryView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    # permission_classes = [DjangoModelPermissions]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['name']
    search_fields = ['name']


class BrandView(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    permission_classes = [DjangoModelPermissions]


class ProductView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # permission_classes = [DjangoModelPermissions]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['name']
    search_fields = ['name']


class FirmView(viewsets.ModelViewSet):
    queryset = Firm.objects.all()
    serializer_class = FirmSerializer
    # permission_classes = [DjangoModelPermissions]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['name']
    search_fields = ['name']