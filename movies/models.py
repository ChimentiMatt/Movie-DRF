from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=255)
    original_title = models.CharField(max_length=255, blank=True, null=True)
    overview = models.TextField(blank=True, null=True)
    release_date = models.DateField(blank=True, null=True)
    runtime = models.FloatField(blank=True, null=True)
    budget = models.IntegerField(blank=True, null=True)
    revenue = models.IntegerField(blank=True, null=True)
    vote_average = models.FloatField(blank=True, null=True)
    vote_count = models.IntegerField(blank=True, null=True)
    popularity = models.FloatField(blank=True, null=True)
    poster_path = models.CharField(max_length=200, blank=True, null=True)
    homepage = models.URLField(blank=True, null=True)
    status = models.CharField(max_length=50, blank=True, null=True)
    tagline = models.TextField(blank=True, null=True)
    adult = models.BooleanField(default=False)
    video = models.BooleanField(default=False)
    csv_id = models.IntegerField(blank=True, null=True)

    people = models.ManyToManyField("people.Person", through="people.MoviePerson", related_name="movies")
    genres = models.ManyToManyField(Genre, related_name="movies")

    def get_poster_url(self, size="w500"):
            """Returns a complete TMDB poster URL or a placeholder if not available."""
            if self.poster_path:
                return f"https://image.tmdb.org/t/p/{size}{self.poster_path}"
            return "https://via.placeholder.com/500x750?text=No+Image+Available"  # Default fallback

    def __str__(self):
        return self.title

class Collection(models.Model):
    name = models.CharField(max_length=255)
    poster_path = models.URLField(blank=True, null=True)
    backdrop_path = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name
    
class Keyword(models.Model):
    name = models.CharField(max_length=255, unique=True)  # Unique keyword name

    def __str__(self):
        return self.name