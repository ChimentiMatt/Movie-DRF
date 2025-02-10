"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from movies.views import upcoming_movie, movie_detail, movie_ranking_list, in_theatres_movies
from people.views import get_person, get_persons_movies

urlpatterns = [
    path('admin/', admin.site.urls),
    path("upcoming-movies/", upcoming_movie, name="upcoming_movies"),
    path("in-theatres-movies/", in_theatres_movies, name="in_theatres_movies"),

    path("movies/<int:movie_id>/", movie_detail, name="movie_detail"),
    path("movies-ranking-list/", movie_ranking_list, name="movie_ranking_list"),
    path("person/<str:name>/", get_person, name="get_person"),
    path("persons-movies/<str:name>/", get_persons_movies, name="get_person"),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
