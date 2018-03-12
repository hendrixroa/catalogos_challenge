from django.urls import path, re_path
from . import views

urlpatterns = [
    path('products', views.ProductApi.as_view()),
    re_path(r'^products/page/(?P<page>[0-9])/$', views.ProductApi.as_view()), 
    re_path(r'^product/(?P<id>[0-9])/$', views.ProductDetailApi.as_view()),
]