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
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    date = models.DateField(auto_now_add=True)

    def get_client_name(self):
        return self.client.name
