from django.core.management.base import BaseCommand
from myapp.models import Product


class Command(BaseCommand):
    help = "Create product"

    def handle(self, *args, **options):
        product = Product(
            title="Lego",
            description="Lego lego",
            price=30000,
            amount=1,
        )
        product.save()
        self.stdout.write(f"{Product}")
