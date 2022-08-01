from django.urls import path

from listing import views

app_name = "listing"
urlpatterns = [path("", views.index, name="index")]
