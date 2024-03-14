from django.db import models


# Create your models here.
class Client(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    phone_number = models.CharField(max_length=11)
    address = models.CharField(max_length=120)
    client_registration_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'Client: {self.name}, email: {self.email}'


class Product(models.Model):
    product_title = models.CharField(max_length=100)
    product_description = models.CharField(max_length=120)
    product_price = models.DecimalField(max_digits=12, decimal_places=2)
    product_amount = models.IntegerField()
    product_added_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'Title: {self.product_title}, price: {self.product_price}'


class Order(models.Model):
    order_client = models.ForeignKey(Client, on_delete=models.CASCADE)
    order_products = models.ForeignKey(Product, on_delete=models.CASCADE)
    order_prise = models.DecimalField(max_digits=12, decimal_places=2)
    order_date = models.DateField(auto_now_add=True)