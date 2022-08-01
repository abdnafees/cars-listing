import csv

from django.core.management.base import BaseCommand, CommandError

from listing.models import Car


class Command(BaseCommand):
    help = "Adds a list of cars from a csv file"

    def add_arguments(self, parser):
        parser.add_argument("file_path", type=str)

    def handle(self, *args, **kwargs):
        path = kwargs["file_path"]
        with open(path) as file:
            file = list(csv.reader(file, delimiter=";"))
            for row in file[2:]:
                try:
                    car = Car(
                        name=row[0],
                        mpg=row[1],
                        cylinders=row[2],
                        displacement=row[3],
                        horsepower=row[4],
                        weight=row[5],
                        acceleration=row[6],
                        model=row[7],
                        origin=row[8],
                    )
                    self.stdout.write(self.style.SUCCESS("Car has been created"))
                except Car.DoesNotExist:
                    raise CommandError("Car object could not be created.")

                car.save()

        self.stdout.write(
            self.style.SUCCESS("Successfully created cars from cars.csv.")
        )
