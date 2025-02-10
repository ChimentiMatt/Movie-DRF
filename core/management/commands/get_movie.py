from django.core.management.base import BaseCommand
import requests
import os

class Command(BaseCommand):
    help = "Fetches movie details including rating for a hardcoded title from TMDB API."

    def handle(self, *args, **kwargs):
        # Get TMDB API key from environment variables
        api_key = os.environ.get('TMDB_API_KEY')
        
        if not api_key:
            self.stdout.write(self.style.ERROR("❌ TMDB API key is missing! Set it in your environment variables."))
            return

        # Hardcoded movie title
        movie_title = "Jurassic World Rebirth"

        # Search for the movie to get its ID
        search_url = f"https://api.themoviedb.org/3/search/movie?api_key={api_key}&query={movie_title}"
        response = requests.get(search_url)

        if response.status_code != 200:
            self.stdout.write(self.style.ERROR(f"❌ Failed to fetch movie details: {response.text}"))
            return
        
        data = response.json()
        if not data.get("results"):
            self.stdout.write(self.style.WARNING(f"⚠️ No results found for '{movie_title}'."))
            return

        # Get the first matching movie
        movie = data["results"][0]
        movie_id = movie["id"]

        # Fetch full movie details
        details_url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}"
        details_response = requests.get(details_url)
        
        if details_response.status_code != 200:
            self.stdout.write(self.style.ERROR(f"❌ Failed to fetch movie details: {details_response.text}"))
            return

        movie_details = details_response.json()

        # Fetch movie rating from /release_dates endpoint
        rating_url = f"https://api.themoviedb.org/3/movie/{movie_id}/release_dates?api_key={api_key}"
        rating_response = requests.get(rating_url)

        movie_rating = "Not Rated"  # Default in case rating isn't found

        if rating_response.status_code == 200:
            rating_data = rating_response.json()

            # Find US rating (MPAA certification)
            for country in rating_data.get("results", []):
                if country["iso_3166_1"] == "US":  # Look for US rating
                    for release in country["release_dates"]:
                        if release["certification"]:
                            movie_rating = release["certification"]
                            break
                    break  # Stop after finding US rating

        movie_details['movie_rating'] = movie_rating
        self.stdout.write(f"🎬 Movie Detail: {movie_details}")
            
        # Print movie details including rating
        # self.stdout.write(self.style.SUCCESS(f"🎬 Movie Title: {movie_details['title']}"))
        # self.stdout.write(f"📅 Release Date: {movie_details['release_date']}")
        # self.stdout.write(f"⭐ Rating: {movie_details['vote_average']}")
        # self.stdout.write(f"🔞 Movie Certification: {movie_rating}")
        
        # self.stdout.write(f"📝 Overview: {movie_details['overview']}")
        # self.stdout.write(f"🎥 TMDB URL: https://www.themoviedb.org/movie/{movie_id}")
