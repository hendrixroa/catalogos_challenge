from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    is_variation = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=False)
    type = models.CharField(max_length=100)
    brand_id = models.IntegerField()
    code = models.IntegerField()
    family = models.IntegerField()
    is_complement = models.BooleanField(default=False)
    is_delete = models.BooleanField(default=False)

class ProductDetail(models.Model):
    is_active = models.BooleanField(default=True)
    is_visibility = models.BooleanField(default=False)
    price = models.FloatField()
    price_offer = models.FloatField()
    offer_day_from = models.DateTimeField()
    offer_day_to = models.DateTimeField()
    quantity = models.IntegerField()
    sku = models.IntegerField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)