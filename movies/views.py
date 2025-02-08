from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.core.paginator import Paginator
from django.http import JsonResponse

from .models import Movie
from people.models import MoviePerson

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
            "poster_url": movie.get_poster_url(),
        }
        for movie in movies
    ]
    return JsonResponse({"movies": movie_data}, safe=False)

def movie_ranking_list(request):
    """Returns a single movie per page with pagination and search functionality"""
    search_query = request.GET.get('search', '')  # Get the search query from the request
    page_number = request.GET.get('page', 1)  # Get the page number (default to page 1)
    
    # Fetch all movies and filter by search query (case-insensitive search)
    movies = Movie.objects.all()
    if search_query:
        movies = movies.filter(title__icontains=search_query)  # Search by movie title

    # Order by vote_average in descending order (highest vote first)
    movies = movies.order_by('-vote_average')

    # Set up pagination: show one movie per page
    paginator = Paginator(movies, 2)  # One movie per page

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
            "name": mp.person.name,  # Assuming Person model has a 'name' field
            "role": mp.role,  # The role played by the person (for actors)
            "job": mp.job,  # The job title (for crew)
            "department": mp.department  # The department (for crew)
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
        "people": people_data
    }
    return JsonResponse(movie_data)
