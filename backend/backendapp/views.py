from django.shortcuts import render
from rest_framework import generics
from .models import AnimalsModel
from .serializers import AnimalsModelSerializer
# Create your views here.
class AnimalView(generics.ListAPIView):
    queryset = AnimalsModel.objects.all()
    serializer_class = AnimalsModelSerializer

