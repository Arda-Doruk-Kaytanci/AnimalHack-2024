from django.urls import path
from .views import AnimalView

urlpatterns = [path("animals/"), AnimalView.as_view()]
