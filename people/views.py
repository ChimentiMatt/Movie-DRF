import os
import requests
from rest_framework.response import Response
from django.http import JsonResponse
from .models import Person, MoviePerson
from movies.models import Movie
from movies.serializers import PersonMovieSerializer


def post_tmdb_data_to_person(person_data):
    '''Helper function to update or create person data in the DB'''
    person = Person.objects.filter(name=person_data['name']).first()

    if person:
        # Ensure all necessary fields are present
        if 'id' in person_data:
            person.tmdb_id = person_data['id']
        if 'biography' in person_data:
            person.biography = person_data['biography']
        if 'birthday' in person_data:
            person.birthday = person_data['birthday']
        if 'deathday' in person_data:
            person.deathday = person_data['deathday']
        if 'gender' in person_data:
            person.gender = person_data['gender']
        if 'place_of_birth' in person_data:
            person.place_of_birth = person_data['place_of_birth']
        if 'known_for_department' in person_data:
            person.known_for_department = person_data['known_for_department']
        if 'profile_path' in person_data:
            person.headshot_url = person_data['profile_path']

        try:
            person.save()
        except Exception as e:
            print(f"Error saving person data: {e}")

    return person

def get_person_data_from_api(name, api_key):
    """Fetch the person data from the TMDB API and return the person ID."""
    url = f'https://api.themoviedb.org/3/search/person?api_key={api_key}&query={name}'
    response = requests.get(url)
    data = response.json()

    if data.get('results'):
        person_id = data['results'][0]['id']
        return person_id
    else:
        print(f"No results found for {name}")
        return None

def get_person(request, name):
    """Retrieve and return person data either from the database or the TMDB API."""
    API_KEY = os.environ.get('TMDB_API_KEY')

    person = Person.objects.filter(name=name).first()
    if person and person.tmdb_id:
        person = {
            'id': person.tmdb_id,
            'name': person.name,
            'biography': person.biography,
            'gender': person.gender,
            'birthday': person.birthday,
            'deathday': person.deathday,
            'place_of_birth': person.place_of_birth,
            'known_for_department': person.known_for_department,
            'headshot_url': person.headshot_url,
        }
        return JsonResponse(person)  # Send the actor data as JSON
    
    actor_id = get_person_data_from_api(name, API_KEY)

    if actor_id:
        url = f'https://api.themoviedb.org/3/person/{actor_id}?api_key={API_KEY}'
        response = requests.get(url)
        data = response.json()
        person = post_tmdb_data_to_person(data)
        person_data = {
            'id': person.tmdb_id,
            'name': person.name,
            'biography': person.biography,
            'gender': person.gender,
            'birthday': person.birthday,
            'deathday': person.deathday,
            'place_of_birth': person.place_of_birth,
            'known_for_department': person.known_for_department,
            'headshot_url': person.headshot_url,
        }
        return JsonResponse(person_data)  # Send the actor data as JSON
    
    else:
        return JsonResponse({"error": f"Failed to retrieve actor details"}, status=404)

def get_persons_movies(request, name):
    person = Person.objects.get(name=name)
    serializer = PersonMovieSerializer(person)

    return JsonResponse(serializer.data)