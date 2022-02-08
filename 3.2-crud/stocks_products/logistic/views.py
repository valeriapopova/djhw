from rest_framework import filters
from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet
from .models import Product, Stock
from .serializers import ProductSerializer, StockSerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [SearchFilter]
    search_fields = ['title', 'description']


class CustomSearchFilter(SearchFilter):
    search_param = 'products'


class StockViewSet(ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    filter_backends = [CustomSearchFilter]
    search_fields = ['products__id', 'products__title', 'products__description']


