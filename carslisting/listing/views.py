from django.http import HttpResponse
from django.shortcuts import render

from .models import Car


def index(request):
    title = "Cars listing"
    cars_list = Car.objects.all()
    context = {"title": title, "cars_list": cars_list}
    return render(request, "listing/index.html", context)
