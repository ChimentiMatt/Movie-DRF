from django.core.management.base import BaseCommand
import requests
import os

class Command(BaseCommand):
    help = "Runs a one-time script to import data from a CSV file"

    def handle(self, *args, **kwargs):
        print("Executing script1...")
        print(os.environ)  # Debug: print all environment variables

        try:
            API_KEY = os.environ.get('TMDB_API_KEY')
        except KeyError:
            print("TMDB_API_KEY not found in .env")
            return
        
        actor_name = 'Tom Hanks'
        actor_id = None

        url = f'https://api.themoviedb.org/3/search/person?api_key={API_KEY}&query={actor_name}'

        response = requests.get(url)
        data = response.json()

        # Check if any results are returned
        if data.get('results'):
            person_id = data['results'][0]['id']
            print(f"Actor's person_id: {person_id}")
            actor_id = person_id
        else:
            print(f"No results found for {actor_name}")

        if actor_id:
            url = f'https://api.themoviedb.org/3/person/{actor_id}?api_key={API_KEY}'
            response = requests.get(url)
            
            if response.status_code == 200:
                actor_data = response.json()
                print(actor_data)
            else:
                print(f"Failed to retrieve actor details. Status Code: {response.status_code}")
