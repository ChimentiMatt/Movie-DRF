from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.utils import timezone
from datetime import timedelta

from .models import Movie
from people.models import MoviePerson

from django.http import JsonResponse
from django.utils import timezone
from datetime import timedelta
from .models import Movie  # Ensure Movie model is imported

def upcoming_movie(request):
    """Returns a list of upcoming movies in JSON format, with an optional query param for limiting results."""
    today = timezone.now().date()
    two_months_from_now = today + timedelta(weeks=8)
    
    movies = Movie.objects.filter(release_date__gte=two_months_from_now).order_by('release_date')

    # Ensure limit is retrieved safely and defaults to None if not provided
    limit = request.GET.get("limit")  # This can be None if not in query parameters

    if limit is not None:  # Check if limit was provided
        try:
            limit = int(limit)  # Convert to integer
            if limit > 0:  # Ensure limit is positive before applying
                movies = movies[:limit]
        except ValueError:
            return JsonResponse({"error": "Invalid limit parameter. It must be a positive integer."}, status=400)

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
            "mpaa_rating": movie.mpaa_rating,
            "poster_url": movie.get_poster_url(),
        }
        for movie in movies
    ]
    
    return JsonResponse({"movies": movie_data}, safe=False)


def in_theatres_movies(request):
    """Returns a list of upcoming movies in json format"""
    today = timezone.now().date()
    two_months_ago = today - timedelta(weeks=8)
    # TODO rename func and endpoint is this is going to be a in theatres movie list. I might want to limit to as it could be up to 25 movies 
    movies = Movie.objects.filter(release_date__gte=two_months_ago, release_date__lte=today)
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
            "mpaa_rating": movie.mpaa_rating,
            "poster_url": movie.get_poster_url(),
        }
        for movie in movies
    ]
    return JsonResponse({"movies": movie_data}, safe=False)


def movie_ranking_list(request):
    """Returns a single movie per page with pagination and search functionality"""
    search_query = request.GET.get('search', '')
    page_number = request.GET.get('page', 1)
    
    movies = Movie.objects.all()
    if search_query:
        movies = movies.filter(title__icontains=search_query)

    movies = movies.order_by('-vote_average')

    # Set up pagination: show one movie per page
    paginator = Paginator(movies, 2)

    try:
        page = paginator.page(page_number)
    except EmptyPage:
        return JsonResponse({"error": "Page not found"}, status=404)

    # Prepare movie data to return
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
            "mpaa_rating": movie.mpaa_rating,
            "poster_url": movie.get_poster_url(),
        }
        for movie in page
    ]

    # Return paginated movie data and metadata
    return JsonResponse({
        "movies": movie_data,
        "page": page.number,
        "total_pages": paginator.num_pages,
        "total_movies": paginator.count
    })

def movie_detail(request, movie_id):
    """Returns details of a single movie by ID in JSON format."""
    movie = get_object_or_404(Movie, id=movie_id)
    movie_people = MoviePerson.objects.filter(movie=movie)

    people_data = [
        {
            "id": mp.person.id,
            "name": mp.person.name,
            "role": mp.role,
            "job": mp.job,
            "department": mp.department
        }
        for mp in movie_people
    ]

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
        "genres": [genre.name for genre in movie.genres.all()],  
        "poster_url": movie.get_poster_url(),
        "mpaa_rating": movie.mpaa_rating,
        "people": people_data
    }
    return JsonResponse(movie_data)
