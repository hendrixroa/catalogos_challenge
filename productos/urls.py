from django.urls import path
from . import views

urlpatterns = [
    path(r'', views.ProductsList.as_view(), name="rest_index"), 
]