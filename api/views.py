from rest_framework.generics import CreateAPIView, ListAPIView

from api.models import Car
from api.serializers import CarSerializer


class CarCreateView(CreateAPIView):

    queryset = Car.objects.all()
    serializer_class = CarSerializer


class CarListView(ListAPIView):

    queryset = Car.objects.all()
    serializer_class = CarSerializer
