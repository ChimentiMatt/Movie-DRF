from django.db import models

# Create your models here.
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