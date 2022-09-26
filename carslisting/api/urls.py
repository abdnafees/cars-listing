from django.urls import include, path
from rest_framework.routers import SimpleRouter
from api.views import CarCreateView, CarListView

router = SimpleRouter()

urlpatterns = [
    path("", include(router.urls)),
    path("add-car/", CarCreateView.as_view(), name="create-car"),
    path("list-all-car/", CarListView.as_view(), name="list-all-car"),
]
