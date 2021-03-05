
from django.urls.conf import path

from .views import GenreListCreateView, MovieCreateView, MovieDetailView, MovieListView

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Omdbapi API Clone",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.test@services.com/",
      contact=openapi.Contact(email="contact@movies.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

app_name='own_api'
urlpatterns = [
    path('all_movies/',MovieListView.as_view()),
    path('add_movie/',MovieCreateView.as_view()),
    path('movie/<str:title>/',MovieDetailView.as_view()),
    path('genre/',GenreListCreateView.as_view()),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
