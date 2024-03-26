from django.db import models


# Create your models here.
class Client(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    phone_number = models.CharField(max_length=11)
    address = models.CharField(max_length=120)
    registration_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Client: {self.name}, email: {self.email}"


class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=120)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    amount = models.IntegerField()
    added_date = models.DateField(auto_now_add=True)
    image = models.ImageField()

    def __str__(self):
        return f"Title: {self.title}, price: {self.price}"


class Order(models.Model):
    order_client = models.ForeignKey(Client, on_delete=models.CASCADE)
    order_products = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    date = models.DateField(auto_now_add=True)
