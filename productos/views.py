from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def list(self, request):
        productos = Product.objects.all()
        serializer = ProductSerializer(productos, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        producto = self.get_object()
        serializer = ProductSerializer(producto)
        return Response(serializer.data)

    def create(self, request):
        serializer = ProductSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "mensaje": "Producto creado correctamente",
                    "producto": serializer.data
                },
                status=status.HTTP_201_CREATED
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        producto = self.get_object()
        serializer = ProductSerializer(producto, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "mensaje": "Producto actualizado correctamente",
                    "producto": serializer.data
                }
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        producto = self.get_object()
        serializer = ProductSerializer(producto, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "mensaje": "Producto actualizado parcialmente",
                    "producto": serializer.data
                }
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        producto = self.get_object()
        producto.delete()

        return Response(
            {"mensaje": "Producto eliminado correctamente"},
            status=status.HTTP_204_NO_CONTENT
        )