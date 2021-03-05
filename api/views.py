from django.db.models import query
from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView, ListCreateAPIView, RetrieveAPIView

from .models import Genre, Movie
from .serializers import MovieSerializer,GenreSerializer

# Create your views here.
class MovieListView(ListAPIView):
    queryset=Movie.objects.all()
    serializer_class=MovieSerializer

class MovieCreateView(CreateAPIView):
    serializer_class=MovieSerializer
    queryset=Movie.objects.all()

class MovieDetailView(RetrieveAPIView):
    lookup_field='title'
    queryset=Movie.objects.all()
    serializer_class=MovieSerializer

class GenreListCreateView(ListCreateAPIView):
    queryset=Genre.objects.all()
    serializer_class=GenreSerializer