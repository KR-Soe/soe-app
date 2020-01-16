from django.contrib import admin
from .models import Player, Champ, Skin

@admin.register(Player)
class AdminPlayer(admin.ModelAdmin):
  list_display = (
    'id',
    'user',
    'summoner_name',
    'password',
    'email'
  )
  list_editable = ('user','summoner_name', 'password', 'email')

@admin.register(Champ)
class AdminChamp(admin.ModelAdmin):
  list_display = (
    'name',
    'lore'
  )

@admin.register(Skin)
class AdminSkin(admin.ModelAdmin):
  list_display = (
    'name',
    'champ'
  )