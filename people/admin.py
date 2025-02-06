from django.contrib import admin

from .models import Person, Cast, Crew

admin.site.register(Person)
admin.site.register(Cast)
admin.site.register(Crew)