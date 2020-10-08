from django.contrib import admin
from Player.models import Player


# admin.site.register(Player)
# Register your models here.
class Player_Admin(admin.ModelAdmin):
    list_display = ('name', 'playerclass', 'email', 'level', 'position')


admin.site.register(Player, Player_Admin)