from productos.models import Product, ProductDetail
from django.http import HttpResponse
from django.core import serializers
from django.views import View
class ProductsList(View):
    model = Product

    def get(self, request, *args, **kwargs):
        products = Product.objects.all()
        print(products)
        serializer = serializers.serialize('json', products)
        return HttpResponse(serializer, content_type='application/json')
    