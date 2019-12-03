from __future__ import unicode_literals
from django.db import models

class Player(models.Model):
  user = models.CharField(max_length=15)
  summoner_name = models.CharField(max_length=30)
  password = models.CharField(max_length=20)
  email = models.CharField(max_length=70)
  
  def __str__(self):
    return self.user
  
class Champ(models.Model):
  name = models.CharField(max_length=30)
  lore = models.CharField(max_length=500)
  
  def __str__(self):
    return self.name
  
class Skin(models.Model):
  name = models.CharField(max_length=20)
  champ = models.ForeignKey(Champ, on_delete=models.CASCADE)

