from django.core.management.base import BaseCommand
from django.core.management import call_command
from catalog.models import Category, Product


class Command(BaseCommand):
    help = "Add product to the database"

    def handle(self, *args, **kwargs):
        Product.objects.all().delete()
        Category.objects.all().delete()
        call_command("loaddata", "catalog_fixture.json")
        self.stdout.write(self.style.SUCCESS("Successfully loaded data from fixture"))
