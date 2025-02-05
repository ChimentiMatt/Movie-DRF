from django.db import models
from movies.models import Movie 
from django.contrib.auth.models import User

# Create your models here.
class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    rating = models.FloatField()
    timestamp = models.DateTimeField()

    class Meta:
        unique_together = ('user', 'movie')  # Ensures one rating per user per movie

    def __str__(self):
        return f"{self.user.id} rated {self.movie.title} as {self.rating}"
