from rest_framework import serializers
from .models import Movie
from people.models import Person, MoviePerson

class MoviePersonSerializer(serializers.ModelSerializer):
    person_name = serializers.CharField(source='person.name')
    role = serializers.CharField()
    department = serializers.CharField()
    job = serializers.CharField()

    class Meta:
        model = MoviePerson
        fields = ['person_name', 'role', 'job', 'department']

class MovieSerializer(serializers.ModelSerializer):
    movie_person = MoviePersonSerializer(many=True, source='movieperson_set')
    class Meta:
        model = Movie
        fields = [
            'id', 
            'title', 
            'original_title', 
            'overview', 
            'release_date', 
            'runtime', 
            'budget', 
            'revenue', 
            'vote_average', 
            'vote_count', 
            'popularity', 
            'poster_path', 
            'homepage', 
            'status', 
            'tagline', 
            'adult', 
            'video', 
            'csv_id', 
            'people',  # Many-to-many relation with people
            'genres',   # Many-to-many relation with genres
            'movie_person'
        ]

class PersonMovieSerializer(serializers.ModelSerializer):
    movies = MovieSerializer(many=True) 
    movie_person = serializers.SerializerMethodField()  # Custom method to serialize movie_person data

    class Meta:
        model = Person
        fields = ['id', 'name', 'movies', 'movie_person']  # Include the relevant fields

    def get_movie_person(self, obj):
        movie_persons = MoviePerson.objects.filter(person=obj)
        return MoviePersonSerializer(movie_persons, many=True).data
