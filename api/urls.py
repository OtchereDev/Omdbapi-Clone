
from django.urls.conf import path

from .views import GenreListCreateView, MovieCreateView, MovieDetailView, MovieListView

app_name='own_api'
urlpatterns = [
    path('all_movies/',MovieListView.as_view()),
    path('add_movie/',MovieCreateView.as_view()),
    path('movie/<str:title>/',MovieDetailView.as_view()),
    path('genre/',GenreListCreateView.as_view()),
]
