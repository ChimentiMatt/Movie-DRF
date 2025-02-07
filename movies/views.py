from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Movie

def movie_list(request):
    """Returns a list of 3 movies in JSON format."""
    movies = Movie.objects.all()[:3]
    movie_data = [
        {
            "id": movie.id,
            "title": movie.title,
            "overview": movie.overview,
            "release_date": movie.release_date,
            "runtime": movie.runtime,
            "budget": movie.budget,
            "revenue": movie.revenue,
            "vote_average": movie.vote_average,
            "vote_count": movie.vote_count,
            "poster_url": movie.get_poster_url(),  # Calls model method for full poster URL
        }
        for movie in movies
    ]
    return JsonResponse({"movies": movie_data}, safe=False)


def movie_detail(request, movie_id):
    """Returns details of a single movie by ID in JSON format."""
    movie = get_object_or_404(Movie, id=movie_id)
    movie_data = {
        "id": movie.id,
        "title": movie.title,
        "overview": movie.overview,
        "release_date": movie.release_date,
        "runtime": movie.runtime,
        "budget": movie.budget,
        "revenue": movie.revenue,
        "vote_average": movie.vote_average,
        "vote_count": movie.vote_count,
        "poster_url": movie.get_poster_url(),  # Calls model method for full poster URL
    }
    return JsonResponse(movie_data)
