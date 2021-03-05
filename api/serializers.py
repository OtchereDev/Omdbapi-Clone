from rest_framework.serializers import ModelSerializer
from .models import Genre, Movie

class GenreSerializer(ModelSerializer):
    class Meta:
        model=Genre
        fields=['name']


class MovieSerializer(ModelSerializer):
    genre=GenreSerializer()
    class Meta:
        model=Movie
        fields=['title',
                'description',
                'created',
                'rated',
                'duration',
                'genre',
                'actors',
                'country',
                'type',
                'poster',
                'director',
                'language',]




