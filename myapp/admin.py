from django.contrib import admin

from myapp.models import Client, Order, Product


@admin.action(description="Сбросить количество на 0")
def reset_amount(modeladmin, request, sequense):
    sequense = sequense.update(amount=0)


class ProductAdmin(admin.ModelAdmin):
    list_display = ["title", "amount", "price", "added_date"]
    list_filter = ["price", "amount"]
    ordering = ["amount"]
    actions = [reset_amount]


class ClientAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "registration_date"]
    ordering = ["registration_date"]


class OrderAdmin(admin.ModelAdmin):
    list_display = ["get_client_name", "price", "date"]
    list_filter = ["date", "price"]
    ordering = ["date"]


# Register your models here.
admin.site.register(Product, ProductAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(Order, OrderAdmin)
