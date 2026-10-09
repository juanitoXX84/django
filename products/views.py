from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer
from .services import DescuentoElectronica, DescuentoRopa, DescuentoDefault

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = []

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category']
    permission_classes = [IsAuthenticated]

class PrecioFinalView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        product = Product.objects.get(pk=pk)

        if product.category.name.lower() == "electronica":
            strategy = DescuentoElectronica()
        elif product.category.name.lower() == "ropa":
            strategy = DescuentoRopa()
        else:
            strategy = DescuentoDefault()

        precio_final = strategy.aplicar_descuento(product.price)
        return Response({
            "producto": product.name,
            "precio_original": product.price,
            "precio_final": precio_final
        })
