from django.db import models

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

    def __str__(self):
        return self.title

class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

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