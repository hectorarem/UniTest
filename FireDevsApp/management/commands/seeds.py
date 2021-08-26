import json
from django.core.management import BaseCommand
from FireDevsApp.models import Gender, Country, City, Professor

class Command(BaseCommand):
    def handle(self, *args, **options):
        # sexo
        Gender.objects.create(name="Masculino")
        Gender.objects.create(name="Femenino")
        Professor.objects.create(name="Juan Perez Paz")
        Professor.objects.create(name="Esteban Rguez Fdez")
        Professor.objects.create(name="Jose I. Hdez Ortis")
        Professor.objects.create(name="Martha Sanchez Noboa")
        Professor.objects.create(name="Josefina Martinez Alonso")

        # countries = self.loadCountry()
        countries = self.loadCountry()

        for co in countries:
            country = Country.objects.create(name=co['name'])
            print(country)
            cities = co['cities']
            for ci in cities:
                city = City.objects.create(country=country, name=ci['name'])
                print(city)
        print('Semilla creada con éxito')

    def loadCountry(self):
        with open('FireDevsApp/management/commands/countriescities.json', encoding='utf-8') as json_file:
            return json.load(json_file)

    def loadCountry(self):
        with open('FireDevsApp/management/commands/countriescities.json', encoding='utf-8') as json_file:
            return json.load(json_file)
