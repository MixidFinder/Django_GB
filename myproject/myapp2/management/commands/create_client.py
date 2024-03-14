from django.core.management.base import BaseCommand
from myapp2.models import Client


class Command(BaseCommand):
    help = 'Create client'

    def handle(self, *args, **options):
        client = Client(name='John', email='John@example.com', phone_number='89999999999', address='Ulica pushkina')
        client.save()
        self.stdout.write(f'{client}')
