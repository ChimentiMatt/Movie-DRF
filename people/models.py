from django.db import models
from django.contrib.auth.models import User

class Person(models.Model):
    name = models.CharField(max_length=255)
    
    # Values that originally come from TMDB API. On first get post to model
    biography = models.TextField(blank=True, null=True)
    gender = models.IntegerField(blank=True, null=True) # 1 - 4 from api
    birthday = models.DateField(blank=True, null=True)  # Example: "1944-05-14"
    deathday = models.DateField(blank=True, null=True)
    place_of_birth = models.CharField(max_length=255, blank=True, null=True)
    known_for_department = models.CharField(max_length=255, blank=True, null=True)
    headshot_url = models.CharField(max_length=255, blank=True, null=True)
    tmdb_id = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    person = models.OneToOneField("people.Person", on_delete=models.SET_NULL, null=True, blank=True, related_name="profile")

class MoviePerson(models.Model):  
    class Role(models.TextChoices):
        ACTOR = 'ACT', 'Actor'
        DIRECTOR = 'DIR', 'Director'
        CREW = 'CRW', 'Crew'
        PRODUCER = 'PRO', 'Producer'
        WRITER = 'WRT', 'Writer'
        OTHER = 'OTH', 'Other'

    movie = models.ForeignKey("movies.Movie", on_delete=models.CASCADE)
    person = models.ForeignKey("people.Person", on_delete=models.CASCADE)
    role = models.CharField(max_length=255, blank=True, null=True)  # Job title (for crew)
    department = models.CharField(max_length=255, blank=True, null=True)  # Department (for crew)
    job = models.CharField(
        max_length=3,
        choices=Role.choices,
        default=Role.OTHER,
    )

    class Meta:
        unique_together = ("movie", "person", "role", "job")  # Prevents duplicate entries

    def __str__(self):
        return f"{self.person.name} - {self.role or self.job} in {self.movie.title}"