import csv
import ast

# headers
[
    'adult', 'belongs_to_collection', 'budget', 'genres', 'homepage', 'id', 'imdb_id', 'original_language', 
    'original_title', 'overview', 'popularity', 'poster_path', 'production_companies', 'production_countries', 
    'release_date', 'revenue', 'runtime', 'spoken_languages', 'status', 'tagline', 'title', 'video', 'vote_average', 'vote_count'
]


# Function to safely parse values
def parse_value(value):
    """Convert values to the appropriate type."""
    if value in ["", "None", None]:  # Handle missing values
        return None
    try:
        # Attempt to convert numbers first
        if value.isdigit():
            return int(value)  # Convert to integer if it's a whole number
        if value.replace(".", "", 1).isdigit() and value.count(".") < 2:
            return float(value)  # Convert to float if it has a decimal point
        
        # Only attempt ast.literal_eval for JSON-like strings
        if (value.startswith("{") and value.endswith("}")) or (value.startswith("[") and value.endswith("]")):
            return ast.literal_eval(value)  # Safely convert lists/dicts

    except (ValueError, SyntaxError):
        pass  # If parsing fails, return the original value
    
    return value  # Return as-is if nothing worked

# List to store processed movie data
movies_list = []

with open("../csv/movies_metadata.csv", newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)  # Automatically maps headers to values
    
    for row in reader:
        movie_data = {key: parse_value(row.get(key, None)) for key in row.keys()}
        movies_list.append(movie_data)  # Store each parsed row in a list

# Print first processed movie to verify
print(movies_list[1]['title'])  # Prints the first row as a dictionary
print(len(movies_list))

'''
How to Structure the Database?
Instead of a single Movies table with all fields, you should create separate tables for entities that have a one-to-many or many-to-many relationship.

Recommended Database Model:
Movie (Main Table)

id (Primary Key)
title
original_title
overview
release_date
runtime
budget
revenue
vote_average
vote_count
popularity
poster_path
homepage
status
tagline
adult
video
imdb_id
original_language
Genre (Separate Table)

id (Primary Key)
name
Many-to-Many Relationship with Movie (Since a movie can have multiple genres)
Production Company (Separate Table)

id (Primary Key)
name
Many-to-Many Relationship with Movie (A movie can be produced by multiple companies)
Production Country (Separate Table)

id (Primary Key)
iso_3166_1 (Country Code)
name
Many-to-Many Relationship with Movie
Spoken Language (Separate Table)

id (Primary Key)
iso_639_1 (Language Code)
name
Many-to-Many Relationship with Movie
Collection (Separate Table)

id (Primary Key)
name
poster_path
backdrop_path
One-to-Many Relationship with Movie (A movie belongs to at most one collection)
'''


'''
from django.db import models

class Collection(models.Model):
    name = models.CharField(max_length=255)
    poster_path = models.URLField(blank=True, null=True)
    backdrop_path = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name

class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class ProductionCompany(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class ProductionCountry(models.Model):
    iso_3166_1 = models.CharField(max_length=10)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class SpokenLanguage(models.Model):
    iso_639_1 = models.CharField(max_length=10)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=255)
    original_title = models.CharField(max_length=255, blank=True, null=True)
    overview = models.TextField(blank=True, null=True)
    release_date = models.DateField(blank=True, null=True)
    runtime = models.FloatField(blank=True, null=True)
    budget = models.BigIntegerField(blank=True, null=True)
    revenue = models.BigIntegerField(blank=True, null=True)
    vote_average = models.FloatField(blank=True, null=True)
    vote_count = models.IntegerField(blank=True, null=True)
    popularity = models.FloatField(blank=True, null=True)
    poster_path = models.URLField(blank=True, null=True)
    homepage = models.URLField(blank=True, null=True)
    status = models.CharField(max_length=50, blank=True, null=True)
    tagline = models.TextField(blank=True, null=True)
    adult = models.BooleanField(default=False)
    video = models.BooleanField(default=False)

    imdb_id = models.CharField(max_length=20, unique=True, blank=True, null=True)
    tmdb_id = models.IntegerField(unique=True, blank=True, null=True)
    original_language = models.CharField(max_length=10, blank=True, null=True)

    belongs_to_collection = models.ForeignKey(Collection, on_delete=models.SET_NULL, blank=True, null=True)
    genres = models.ManyToManyField(Genre, blank=True)
    production_companies = models.ManyToManyField(ProductionCompany, blank=True)
    production_countries = models.ManyToManyField(ProductionCountry, blank=True)
    spoken_languages = models.ManyToManyField(SpokenLanguage, blank=True)
    ratings = models.ManyToManyField("User", through="Rating", blank=True)

    keywords = models.ManyToManyField(Keyword, blank=True)  # New Many-to-Many Relationship

    def __str__(self):
        return self.title


class Keyword(models.Model):
    name = models.CharField(max_length=255, unique=True)  # Unique keyword name

    def __str__(self):
        return self.name

class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    rating = models.FloatField()
    timestamp = models.DateTimeField()

    class Meta:
        unique_together = ('user', 'movie')  # Ensures one rating per user per movie

    def __str__(self):
        return f"{self.user.id} rated {self.movie.title} as {self.rating}"

class Person(models.Model):
    name = models.CharField(max_length=255)
    gender = models.IntegerField(blank=True, null=True)  # 0: Unknown, 1: Female, 2: Male
    profile_path = models.URLField(blank=True, null=True)  # Optional profile image

    def __str__(self):
        return self.name

class Cast(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    character = models.CharField(max_length=255, blank=True, null=True)  # Role played
    order = models.IntegerField(blank=True, null=True)  # Order in credits

    def __str__(self):
        return f"{self.person.name} as {self.character} in {self.movie.title}"

class Crew(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    job = models.CharField(max_length=255)  # Job title (e.g., Director, Writer)
    department = models.CharField(max_length=255)  # Department (e.g., Writing, Directing)

    def __str__(self):
        return f"{self.person.name} - {self.job} ({self.department}) in {self.movie.title}"
        
'''