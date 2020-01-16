import os
import json
from .models import Champ

class ChampList():
  def __init__(self, champ):
    self.champ = champ
    print(champ.name)