from django.db import models


class Car(models.Model):
    name = models.CharField(max_length=200)
    mpg = models.FloatField()
    cylinders = models.IntegerField()
    displacement = models.FloatField()
    horsepower = models.FloatField()
    weight = models.FloatField()
    acceleration = models.FloatField()
    model = models.IntegerField()
    origin = models.CharField(max_length=200)
