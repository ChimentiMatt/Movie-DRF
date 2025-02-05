from django.db import models
from django.contrib.auth.models import User
from movies.models import Movie 

# Create your models here.
class Person(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)  # Link to User model
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
        