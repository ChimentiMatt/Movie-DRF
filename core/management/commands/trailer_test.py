from django.core.management.base import BaseCommand
import requests
import os

class Command(BaseCommand):
    help = "Fetches the trailer URL for a given movie title."

    def handle(self, *args, **kwargs):
        # Hardcoding the movie title
        movie_title = 'Captain America: The First Avenger'  # Change this to any movie title you want to hardcode
        
        # Get TMDb API key from environment variable
        api_key = os.environ.get('TMDB_API_KEY')

        if not api_key:
            self.stdout.write(self.style.ERROR("TMDB_API_KEY is not set in environment variables."))
            return
        
        # TMDb base URL
        base_url = "https://api.themoviedb.org/3"
        
        # Step 1: Search for the movie by title
        search_url = f"{base_url}/search/movie?api_key={api_key}&query={movie_title}&language=en-US"
        search_response = requests.get(search_url)
        
        if search_response.status_code == 200:
            search_data = search_response.json()
            if search_data['results']:
                # Assuming the first result is the correct movie
                movie_id = search_data['results'][0]['id']
                
                # Step 2: Get videos (including trailers) for the movie
                trailer_url = None
                video_url = f"{base_url}/movie/{movie_id}/videos?api_key={api_key}&language=en-US"
                video_response = requests.get(video_url)
                
                if video_response.status_code == 200:
                    video_data = video_response.json()
                    # Check for a video of type 'Trailer'
                    for video in video_data['results']:
                        if video['type'] == 'Trailer':
                            trailer_url = f"https://www.youtube.com/watch?v={video['key']}"
                            break
                    if not trailer_url:
                        trailer_url = 'Trailer not available.'
                else:
                    trailer_url = 'Unable to fetch trailer.'

                # Output the trailer URL
                self.stdout.write(f"Trailer URL: {trailer_url}")
            else:
                self.stdout.write(self.style.ERROR(f"Movie '{movie_title}' not found."))
        else:
            self.stdout.write(self.style.ERROR(f"Error: Unable to search for movie '{movie_title}'."))
