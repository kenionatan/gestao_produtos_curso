from django.db import models


class Product(models.Model):
    product_title = models.CharField(max_length=100)
    product_price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.product_title
