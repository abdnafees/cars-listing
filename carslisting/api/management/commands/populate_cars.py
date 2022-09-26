import csv
import os

from django.conf import settings
from django.core.management.base import BaseCommand, CommandError

from api.models import Car


file_path = os.path.abspath(os.path.abspath(settings.BASE_DIR) + "/data/cars.csv")


class Command(BaseCommand):
    help = "Adds a list of cars from a csv file"

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **kwargs):
        try:
            with open(file_path) as csv_file:
                csv_reader = csv.DictReader(csv_file)
                objects_list = []
                for row in csv_reader:
                    try:
                        print("here")
                        objects_list.append(
                            Car(
                                name=row["Car"],
                                mpg=row["MPG"],
                                cylinders=row["Cylinders"],
                                displacement=row["Displacement"],
                                horsepower=row["Horsepower"],
                                weight=row["Weight"],
                                acceleration=row["Acceleration"],
                                model=row["Model"],
                                origin=row["Origin"],
                            )
                        )
                    except Car.DoesNotExist:
                        raise CommandError("Car object could not be created.")

                try:
                    Car.objects.bulk_create(objects_list)
                    self.stdout.write(self.style.SUCCESS("Car has been created."))

                except Exception as e:
                    self.stdout.write(
                        self.style.ERROR(f"Car object could not be created {e}")
                    )

        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Could not open file {e}"))
