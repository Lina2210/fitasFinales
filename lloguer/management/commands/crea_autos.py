import random
from faker import Faker
from lloguer.models import Automobil
from django.core.management.base import BaseCommand, CommandError
from django.utils import timezone

class Command(BaseCommand):
    help = 'Seed database with fake data for Automobil model'

    def handle(self, *args, **kwargs):
        faker = Faker()

        for _ in range(200):
            marca = faker.company()
            model = faker.random_element(elements=('Sedan', 'SUV', 'Truck', 'Coupe'))
            matricula = faker.license_plate()

            automobil = Automobil.objects.create(
                marca=marca,
                model=model,
                matricula=matricula
            )

            self.stdout.write(self.style.SUCCESS(f'Automobil {automobil} creado correctamente'))
