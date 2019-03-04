from django.urls import path
from .views import home
from produtos.views import product_list


urlpatterns = [
    path('', home, name="home"),
    path('product/list/', product_list, name="product_list")
]
