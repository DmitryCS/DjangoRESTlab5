from django.contrib import admin
from GameMap.models import Location


class Location_Admin(admin.ModelAdmin):
    list_display = ('locationId',)


admin.site.register(Location, Location_Admin)
