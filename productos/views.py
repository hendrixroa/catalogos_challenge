from productos.models import Products, ProductsDetail
from productos.serializers import ProductsSerializers, ProductsDetailSerializers
from rest_framework.views import APIView
from rest_framework.response import Response
class ProductsList(APIView):
    def get(self, request, format=None):
        products = Products.objects.all()
        serializer = ProductsSerializer(products, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        return 1

    def put(self, request, format=None):
        return 2

    def delete(self, request, format=None):
        return 3