from django.http import HttpResponse
from django.core import serializers
from django.core.exceptions import ValidationError
import json
from django.views import View
from productos.models import Product, ProductDetail

class ProductsList(View):
    model = Product

    def get(self, request, *args, **kwargs):
        products = Product.objects.all()
        print(products)
        serializer = serializers.serialize('json', products)
        return HttpResponse(serializer, content_type='application/json')

    def post(self, request, *args, **kwargs): 
        try:   
            data_body = json.loads(request.body.decode('utf8'))
            detail = {}
            for item in data_body.items():
                detail.update({ 'price_offer': item.pop('price_offer') })
            print(data_body.items())
            product = Product(**data_body)
            product.full_clean()
            Product.objects.create(**data_body)
            return HttpResponse(json.dumps({'status': 200, 'message': 'Producto Creado'}), content_type='application/json')
        except ValidationError as e:
            response = HttpResponse(json.dumps(e.message_dict), content_type='application/json') 
            response.status_code = 400
            return response