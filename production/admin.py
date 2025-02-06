from django.contrib import admin

from .models import ProductionCompany, ProductionCountry, SpokenLanguage

admin.site.register(ProductionCompany)
admin.site.register(ProductionCountry)
admin.site.register(SpokenLanguage)