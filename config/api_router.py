from django.conf import settings
from django.urls.conf import include, path
from rest_framework.routers import DefaultRouter, SimpleRouter

from drf_movies.users.api.views import UserViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)


app_name = "api"
urlpatterns = [path('',include('api.urls')),]

urlpatterns+=router.urls
