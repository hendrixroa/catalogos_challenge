from django.db import models

class Products(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    is_variation = models.BooleanField()
    created = models.DateTimeField(auto_now=True)
    modified = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField()
    type = models.CharField(max_length=100)
    brand_id = models.IntegerField()
    code = models.IntegerField()
    family = models.IntegerField()
    is_complement = models.BooleanField()
    is_delete = models.BooleanField()

class ProductsDetail(models.Model):
    is_active = models.BooleanField()
    is_visibility = models.BooleanField()
    price = models.FloatField()
    price_offer = models.FloatField()
    offer_day_from = models.DateTimeField()
    offer_day_to = models.DateTimeField()
    quantity = models.IntegerField()
    sku = models.IntegerField()
    product_id = models.ForeignKey(Products, on_delete=models.CASCADE)