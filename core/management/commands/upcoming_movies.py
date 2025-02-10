from django.core.management.base import BaseCommand
import requests
import os

class Command(BaseCommand):
    help = "A proof of concept script to show getting upcoming movies with trailers"

    def handle(self, *args, **kwargs):
        # Get the TMDb API key from environment variable
        api_key = os.environ.get('TMDB_API_KEY')

        if not api_key:
            print("Error: TMDB_API_KEY is not set in environment variables.")
            return

        # TMDb base URL
        base_url = "https://api.themoviedb.org/3"
        image_base_url = "https://image.tmdb.org/t/p/w500"  # Base URL for movie posters

        # Upcoming Movies endpoint
        endpoint = "/movie/upcoming"
        url = f"{base_url}{endpoint}?api_key={api_key}&language=en-US&page=1"

        # Make the request to get upcoming movies
        response = requests.get(url)

        # Check if the request was successful
        if response.status_code == 200:
            data = response.json()
            
            # Loop through the results and get the movie details along with the cast, poster, genres, budget, runtime, and trailer
            for movie in data['results']:
                movie_title = movie['title']
                movie_release_date = movie['release_date']
                movie_overview = movie['overview']
                
                # Use the movie title to search for the movie details (in case you want to use titles)
                search_url = f"{base_url}/search/movie?api_key={api_key}&query={movie_title}&language=en-US"
                search_response = requests.get(search_url)
                
                if search_response.status_code == 200:
                    search_data = search_response.json()
                    if search_data['results']:
                        movie_details = search_data['results'][0]  # Assuming the first result is the correct movie
                        movie_id = movie_details['id']
                        movie_poster_path = movie_details.get('poster_path')

                        # Construct the full URL for the poster image
                        if movie_poster_path:
                            movie_poster_url = f"{image_base_url}{movie_poster_path}"
                        else:
                            movie_poster_url = None  # No poster available

                        # Get genres, budget, and runtime
                        genres = ", ".join([genre['name'] for genre in movie_details.get('genres', [])]) if movie_details.get('genres') else 'TBD'
                        
                        # Handle budget formatting safely
                        budget = movie_details.get('budget', 'TBD')
                        if isinstance(budget, int) and budget > 0:
                            budget = f"${budget:,}"  # Format budget with commas (e.g., $1,000,000)
                        else:
                            budget = 'TBD'  # Budget not available or 0

                        # Handle runtime formatting safely
                        runtime = movie_details.get('runtime', 'TBD')
                        if isinstance(runtime, int) and runtime > 0:
                            runtime = f"{runtime} minutes"
                        else:
                            runtime = 'TBD'  # Runtime not available or 0
                        
                        # Fetch trailer information
                        trailer_url = f"{base_url}/movie/{movie_id}/videos?api_key={api_key}&language=en-US"
                        trailer_response = requests.get(trailer_url)
                        trailer_video = None

                        if trailer_response.status_code == 200:
                            trailer_data = trailer_response.json()
                            # Check for trailer in the video list (usually of type 'Trailer')
                            for video in trailer_data.get('results', []):
                                if video['type'] == 'Trailer':
                                    trailer_video = f"https://www.youtube.com/watch?v={video['key']}"
                                    break
                            
                            if not trailer_video:
                                trailer_video = 'Trailer not available.'

                        else:
                            trailer_video = 'Unable to fetch trailer.'

                        # Print movie details including the trailer URL
                        print(f"Title: {movie_title}")
                        print(f"Release Date: {movie_release_date}")
                        print(f"Overview: {movie_overview}")
                        print(f"Poster URL: {movie_poster_url}")
                        print(f"Genres: {genres}")
                        print(f"Budget: {budget}")
                        print(f"Runtime: {runtime}")
                        print(f"Trailer: {trailer_video}")
                        
                        # Fetch cast information
                        cast_url = f"{base_url}/movie/{movie_id}/credits?api_key={api_key}&language=en-US"
                        cast_response = requests.get(cast_url)
                        
                        if cast_response.status_code == 200:
                            cast_data = cast_response.json()
                            print("Cast:")
                            for cast_member in cast_data['cast'][:5]:  # Show only the first 5 actors for brevity
                                print(f"  - {cast_member['name']} as {cast_member['character']}")
                        else:
                            print("Error: Unable to fetch cast information.")
                        
                        print("\n" + "="*40 + "\n")
                    else:
                        print(f"Error: Movie '{movie_title}' not found in the search results.")
                else:
                    print(f"Error: Unable to search for movie '{movie_title}'.")
        else:
            print(f"Error: Unable to fetch upcoming movies. Status code: {response.status_code}")

        print('len', len(data['results']))

'''
NOTES: 
will need to update after release 
Genres
Budget
Runtime

Response
========================================

Title: Flight Risk
Release Date: 2025-01-22
Overview: A U.S. Marshal escorts a government witness to trial after he's accused of getting involved with a mob boss, only to discover that the pilot who is transporting them is also a hitman sent to assassinate the informant. After they subdue him, they're forced to fly together after discovering that there are others attempting to eliminate them.
Poster URL: https://image.tmdb.org/t/p/w500/4cR3hImKd78dSs652PAkSAyJ5Cx.jpg
Genres: N/A
Budget: N/A
Runtime: N/A
Cast:
  - Michelle Dockery as Madolyn Harris
  - Mark Wahlberg as Daryl Booth
  - Topher Grace as Winston
  - Leah Remini as Caroline Van Sant (voice)
  - Paul Ben-Victor as Director Coleridge (voice)

========================================

Title: Lembayung
Release Date: 2024-09-19
Overview: Arum and Pica, who wanted to complete their internship at Lembayung hospital, had to face mysterious terror from a woman satan who was suspected of hanged herself in the bathroom. The situation became even more tense after they asked others for help to the point where they threatened their own lives and those closest to them.
Poster URL: https://image.tmdb.org/t/p/w500/5x9LrW0yvtt6S3XovIQHgXfYvLL.jpg
Genres: N/A
Budget: N/A
Runtime: N/A
Cast:
  - Taskya Namya as Pica
  - Yasamin Jasem as Arum
  - Arya Saloka as Doctor Teto
  - Anna Jobling as Tantri
  - Daffa Wardhana as Dimas



'''