from django.contrib import admin

from .models import MoviePerson, Profile, Person

admin.site.register(MoviePerson)
admin.site.register(Profile)
admin.site.register(Person)