from django.core.management.base import BaseCommand
from myapp.models import Product


class Command(BaseCommand):
    help = "Create product"

    def handle(self, *args, **options):
        product = Product(
            product_title="Lego",
            product_description="Lego lego",
            product_price=30000,
            product_amount=1,
        )
        product.save()
        self.stdout.write(f"{Product}")
