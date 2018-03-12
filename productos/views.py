from django.http import HttpResponse
from django.core import serializers
from django.core.exceptions import ValidationError
from django.core.paginator import Paginator
import json
from django.views import View
from productos.models import Product, ProductDetail

class ProductApi(View):
    model = Product

    def get(self, request, page='', *args, **kwargs):
        products = Product.objects.all()
        if page != '':
            paginator = Paginator(products, 5)
            products = paginator.get_page(int(page))
        serializer = serializers.serialize('json', products)
        return HttpResponse(serializer, content_type='application/json')

    def post(self, request, *args, **kwargs): 
        try:   
            data_body = json.loads(request.body.decode('utf8'))
            detail = {}
            if all (item in data_body for item in ('is_active', 'is_visibility', 'price', 'price_offer', 'offer_day_from', 'offer_day_to', 'quantity', 'sku')):
                detail.update({'is_active': data_body.pop('is_active')})
                detail.update({'is_visibility': data_body.pop('is_visibility')})
                detail.update({'price': data_body.pop('price')})
                detail.update({'price_offer': data_body.pop('price_offer')})
                detail.update({'offer_day_from': data_body.pop('offer_day_from')})
                detail.update({'offer_day_to': data_body.pop('offer_day_to')})
                detail.update({'quantity': data_body.pop('quantity')})
                detail.update({'sku': data_body.pop('sku')})
            else:
                response = HttpResponse(json.dumps({'status': 400, 'message': 'Los campos is_active, is_active, is_visibility, price, price_offer, offer_day_from, offer_day_to, quantity, sku, product_id son requeridos'}), content_type='application/json') 
                response.status_code = 400
                return response
            product = Product(**data_body)
            product_detail = ProductDetail(**detail)
            product.full_clean()
            product_detail.full_clean()
            product_saved = Product.objects.create(**data_body)
            detail_saved = ProductDetail.objects.create(product=product_saved, **detail)
            return HttpResponse(json.dumps({'status': 200, 'message': 'Producto Creado'}), content_type='application/json')
        except ValidationError as e:
            response = HttpResponse(json.dumps(e.message_dict), content_type='application/json') 
            response.status_code = 400
            return response

    def put(self, request, *args, **kwargs):
        data_body = json.loads(request.body.decode('utf8'))
        for product in data_body:
            Product.objects.filter(pk=product['id']).update(**product)
        
class ProductDetailApi(View):
    model = ProductDetail

    def get(self, request, id, *args, **kwargs):
        product = Product.objects.filter(pk=id)
        serializer = serializers.serialize('json', product)
        return HttpResponse(serializer, content_type='application/json')

    def put(self, request, id, *args, **kwargs):
        data_body = json.loads(request.body.decode('utf8'))
        product_updated = Product.objects.filter(pk=id).update(**data_body)
        return HttpResponse(json.dumps({'status': 200, 'message': 'Producto actualizado'}), content_type='application/json')

    def delete(self, request, id, *args, **kwargs):
        product = Product.objects.get(pk=id)
        product.delete()
        return HttpResponse(json.dumps({'status': 200, 'message': 'Producto eliminado'}), content_type='application/json')