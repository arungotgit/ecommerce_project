from django.shortcuts import render

# Create your views here.

def product_list(request):
    return render(request, 'products/product_list.html')


from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('-created_at')
    serializer_class = ProductSerializer