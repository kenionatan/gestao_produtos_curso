from django.urls import path
from .views import product_list, product_new

urlpatterns = [
    path('list/', product_list, name="product_list"),
    path('new/', product_new, name="product_new")
]
